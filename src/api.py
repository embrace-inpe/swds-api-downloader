import json
import logging
import os
import urllib.parse
import urllib.request
from urllib.error import URLError

import src.utils.helpers as h
from src.utils.error import SwdsError


class APIDownload:
    """
    Simple app to download files from Space Weather Data Share API

    """
    host = ''
    credentials = {}
    path = ''
    token = None

    def __init__(self, credentials, host, path='./tmp/', **kwargs):
        self.path = path if path.endswith('/') else path + '/'
        self.variables_verify(host, credentials)
        self.host = host
        self.credentials = credentials
        default = dict(
            application=None,
            start_date=None,
            end_date=None,
            resolution=None,
            station=None,
            swfilter=None,
            swtype=None,
            network=None,
            equipment=None
        )
        self.data = dict(default, **kwargs)

    def get_token(self):
        """
        Get the token from /api/auth/login/ end point using the credentials
        :return: A token
        """
        data = urllib.parse.urlencode(self.credentials)
        data = data.encode('ascii')

        request = urllib.request.Request(self.host + '/api/auth/login/', data)
        with urllib.request.urlopen(request) as response:
            response = json.loads(response.read().decode('utf-8'))
            self.token = response['token']
            return self.token

    def get_authorization(self):
        """
        Verify if the token exists, if it doesn't, it logs in and return a bearer string format
        :return: A string with a Bearer format
        """
        bearer = 'Bearer '
        if self.token:
            return bearer + self.token
        return bearer + self.get_token()

    def mount_query(self):
        """
        Mount the query string to /api/files/ end point

        :return: A query string as key=value&key2=value2
        """
        query = []
        for key, value in self.data.items():
            if value:
                query.append('%s=%s' % (key, value))
        return '&'.join(query)

    def get_files_list(self):
        """
        Get the list of files from /api/files/ endpoint

        :return: A list of files
        """
        api = '/api/files/'
        query = self.mount_query()
        request_files = urllib.request.Request('%s%s?%s' % (self.host, api, query))
        request_files.add_header('Authorization', self.get_authorization())

        with urllib.request.urlopen(request_files) as response:
            list_files = json.loads(response.read().decode('utf-8'))
            return list_files

    def download_files(self, list_files):
        """
        Downloading the files fom API
        It will save the files in the path set in path_to_save on main.py

        :param list_files:
        :return: Print download status
        """
        logging.info(h.initial_msg(len(list_files)))
        countsuccess = 0
        countfails = 0
        for file in list_files:

            _, _, _, _, _, *file_path, file_name = file['url'].split('/')
            file_path = '/'.join(file_path) + '/'
            filename = self.path + file_path + file_name
            logging.info("""   Downloading file: {} to {}""".format(file_name, filename))

            request = urllib.request.Request(file['url'])
            request.add_header('Authorization', self.get_authorization())
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    with open(filename, 'wb+') as out_file:
                        data = response.read()  # a `bytes` object
                        out_file.write(data)
                        countsuccess = countsuccess + 1
            except Exception as error:
                logging.error(h.log_error_file_msg(file_name))
                logging.info(h.error_msg(file_name, error))
                countfails = countfails + 1
        logging.info(h.final_msg(self.path, countsuccess, countfails))

    def variables_verify(self, host, login):
        """
        Verify the variables host and login

        :param host: must be a valid URL
        :param login: Must be a dict with username and password keys
        :return: raise Exception
        """
        self._host_verify(host)
        self._login_verify(login)

    def _host_verify(self, host):
        """
        Verify the host variable it cannot to empty and needs be a valid URL

        :param host: must be a valid URL
        :return: raise Exception
        """
        if host == '':
            raise SwdsError('The variable host needs an URL value')

        try:
            import urllib
            urllib.request.urlopen(host)
        except (ValueError, URLError) as e:
            raise SwdsError('The variable host is not a valid URL e.g: "http://apidomain.com"')

    def _login_verify(self, login):
        """
        Verify the dictionary login it must has the username and password keys

        :param login: Must be a dict with username and password keys
        :return: raise Exception
        """
        if 'username' not in login:
            raise SwdsError('The login dictonary must has a key called username')
        elif login['username'] == '':
            raise SwdsError('The username key on login dictonary cannot be empty')
        elif 'password' not in login:
            raise SwdsError('The login dictonary must has a key called password')
        elif login['password'] == '':
            raise SwdsError('The password key on login dictonary cannot be empty')
