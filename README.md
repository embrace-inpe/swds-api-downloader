# Downloading files from Space Weather Data Share API
This is a python app sample to help users to automatically download files through Space Weather Data Share API.


Configuration
-----------------
First, you must download this source and edit the `main.py` file variables with your personal information:

- **host** `(Api host address)`
- **search** `(Search parameters)`
- **login** `(Username Or E-mail and password)`
- **path_to_save** `(Path to save the files)`

```python
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
        "username": "your-username or your-email",
        "password": "your-password"
    }
    # Path to save the files
    path_to_save = './tmp/magnetometer/'

    download = APIDownload(credentials=login, host=host, path=path_to_save, **search)
    files = download.get_files_list()
    download.download_files(files)
```
Run the program
-----------------
Then, you can run the program on terminal as following

```bash
python main.py
```

The console output will show all information about the download stage, e.g.:

```console
    *****************************************************
    
    Start Download the files from Space Weather Data Share API
    Total: 2 file(s)
    
    *****************************************************
    
   Downloading the file: sjc23apr.17m to ./tmp/magnetometer/SJC/2017/sjc23apr.17m
   Downloading the file: sjc22apr.17m to ./tmp/magnetometer/SJC/2017/sjc22apr.17m


    *****************************************************

    Done! All files are in your path ./tmp/magnetometer/
```
Custom script
-----------------
This page is an example of how to download files from EMBRACE/INPE service (SW Data Share). Please, fell free to customize your own script with different applications, dates and filters.

Help
-----------------
Any question or suggestion, please, contact our support sending an email to [desenvolvimento.emabrace@inpe.br](mailto:desenvolvimento.emabrace@inpe.br).

