#! /usr/bin/env python3
import sys

import src.utils.helpers as h
from src.api import APIDownload

if __name__ == '__main__':

    if len(sys.argv) == 1:

        # Search filters
        # You must passing these values if aren't using the command line args
        search = {
            'application': 1,
            'start_date': '2017-04-01',
            'end_date': '2017-04-23',
            'resolution': 1,
            'station': 1,
            'filter': None,
            'type': None,
            'network': None,
            'equipment': None
        }
        path_to_save = './tmp/magnetometer/'

    else:
        search, path_to_save = h.get_sys_args(sys.argv[1:])

    # The Api host address
    # e.g: http://datashare.ebrace.inpe.br
    host = ''

    # Credentials
    # the username key can be your username or e-mail
    login = {
        "username": "",
        "password": ""
    }

    download = APIDownload(credentials=login, host=host, path=path_to_save, **search)
    files = download.get_files_list()
    download.download_files(files)



