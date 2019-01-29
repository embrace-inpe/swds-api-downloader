#! /usr/bin/env python3
import logging
import sys

import settings
import src.utils.helpers as h
from src.api import APIDownload

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

    if len(sys.argv) == 1:
        search = settings.SEARCH
        path_to_save = settings.PATH_TO_SAVE

    else:
        search, path_to_save = h.get_sys_args(sys.argv[1:])

    host = settings.HOST

    login = {
        "username": settings.USERNAME,
        "password": settings.PASSWORD
    }

    download = APIDownload(credentials=login, host=host, path=path_to_save, **search)
    files = download.get_files_list()
    download.download_files(files)



