import os
import urllib.parse
import urllib.request
import json

import src.utils.helpers as h


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
        self.host = host
        self.credentials = credentials
        default = dict(
            application=None,
            start_date=None,
            end_date=None,
            resolution=None,
            station=None,
            filter=None,
            type=None,
            network=None,
            equipment=None
        )
        self.data = dict(default, **kwargs)

    def login(self):
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

    def get_token(self):
        """
        Verify if the token exists, if it doesn't, it logs in and return a bearer string format
        :return: A string with a Bearer format
        """
        auth = 'Bearer '
        if self.token:
            return auth + self.token
        return auth + self.login()

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
        request_files.add_header('Authorization', self.get_token())

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
        h.initial_msg(len(list_files))
        countsuccess = 0
        countfails = 0
        for file in list_files:

            _, _, _, _, _, *file_path, file_name = file['url'].split('/')
            file_path = '/'.join(file_path) + '/'
            filename = self.path + file_path + file_name
            print("""   Downloading the file: {} to {}""".format(file_name, filename))

            request = urllib.request.Request(file['url'])
            request.add_header('Authorization', self.get_token())
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            try:
                with urllib.request.urlopen(request) as response, open(filename, 'wb+') as out_file:
                    data = response.read()  # a `bytes` object
                    out_file.write(data)
                    countsuccess = countsuccess + 1
            except Exception as error:
                h.error_msg(file_name, error)
                countfails = countfails + 1
        h.final_msg(self.path, countsuccess, countfails)
        return exit(0)
