from src.api import APIDownload

if __name__ == '__main__':
    # Api host address
    host = 'http://127.0.0.1:8000'
    # Search filters
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
    # Credentials
    # the username key can be your username or e-mail
    login = {
        "username": "",
        "password": ""
    }
    # Path to save the files
    path_to_save = './tmp/magnetometer/'

    download = APIDownload(credentials=login, host=host, path=path_to_save, **search)
    files = download.get_files_list()
    download.download_files(files)



