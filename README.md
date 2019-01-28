# Downloading files from Space Weather Data Share API
This is a python app sample to help users to automatically download files through Space Weather Data Share API.


Configuration
-----------------
Exist two ways to set the search values, by command line args or setting the variables values in code.

Set the `host` and `login` variables on the code for both cases.
After this you can choice the best way for you use it.

1. ### By Command Line
This way require the command line args as bellow:

```bash
python swds-downloader.py -a 1 -i 2017-04-01 -e 2017-04-23 -r 1 -s 1 -p ./tmp/magnetometer/
```
See the avaliables args:
```text
** Filters
    
-a --app = An integer Application ID (Required)
-s --station = An integer Station ID (Optional)
-r --resolution = An integer  Resolution ID (Optional)
-f --filter = An integer  Filter ID (Optional)
-t --type = An integer  Type ID (Optional)
-n --network = An integer  Network ID (Optional)
-q --equipment = An integer  Equipment ID (Optional)

** Dates
-i --start_date = A string with format yyyy-mm-dd (Required)
-e --end_date = A string with format yyyy-mm-dd (Required)

** Path to save the files
-p --path = A string with the a absolute path to save the files (Required)
```


2. ### Setting Variables in Code
For run the program without command line args you must edit the `swds-downloader.py` file variables with your personal information:

- **search** `(Search parameters)`
- **path_to_save** `(Path to save the files)`

```python
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
```
Then, you can run the program on terminal as following

```bash
python swds-downloader.py
```

Run the program
-----------------

The console output will show all information about the download stage, e.g.:

```console
    *****************************************************
    
    Start Download the files from Space Weather Data Share API
    Total: 2 file(s)
    
    *****************************************************
    
   Downloading the file: sjc23apr.17m to ./tmp/magnetometer/SJC/2017/sjc23apr.17m
   Downloading the file: sjc22apr.17m to ./tmp/magnetometer/SJC/2017/sjc22apr.17m


    *****************************************************
    Download success: 2
    Download Failed: 1 

    Done! All files are in your path ./tmp/magnetometer/
```
Custom script
-----------------
This page is an example of how to download files from EMBRACE/INPE service (SW Data Share). Please, fell free to customize your own script with different applications, dates and filters.

Help
-----------------
Any question or suggestion, please, contact our support sending an email to [desenvolvimento.emabrace@inpe.br](mailto:desenvolvimento.emabrace@inpe.br).

