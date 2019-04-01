#! /usr/bin/env python3
import sys

import settings
import src.utils.helpers as h
from src.api import APIDownload


def main(argv):
    h.log_config()

    if len(argv) == 1:
        search = settings.SEARCH
        path_to_save = settings.PATH_TO_SAVE

    else:
        search, path_to_save = h.get_sys_args(argv[1:])

    host = 'http://www2.inpe.br/climaespacial/SpaceWeatherDataShare'

    login = {
        "username": settings.USERNAME,
        "password": settings.PASSWORD
    }

    download = APIDownload(credentials=login, host=host, path=path_to_save, **search)
    files = download.get_files_list()
    download.download_files(files)


if __name__ == '__main__':
    main(sys.argv)




