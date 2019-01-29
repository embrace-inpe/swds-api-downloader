import os
import shutil
from unittest import TestCase

import settings
from src.api import APIDownload


class APIDownloadTest(TestCase):
    def setUp(self):
        search = settings.SEARCH
        path_to_save = './tmp-tests/'
        login = {
            "username": settings.USERNAME,
            "password": settings.PASSWORD
        }
        host = settings.HOST
        self.download = APIDownload(credentials=login, host=host, path=path_to_save, **search)

    def test_login(self):
        """The login must return a token"""
        token = self.download.get_token()
        self.assertIsInstance(token, str)
        self.assertEqual(len(token), 200)

    def test_token_format(self):
        """The token needs be with a Bearer prefix"""
        bearer_token =self.download.get_authorization()
        bearer = bearer_token.split(' ')[0]
        self.assertEqual('Bearer', bearer)

    def test_get_files_list(self):
        """Must return a files urls list"""
        files = self.download.get_files_list()
        self.assertTrue(len(files) > 0)

    def test_download_files(self):
        """Must download the file to path"""
        files = self.download.get_files_list()
        file = [files[0]]
        file_name = '/'.join(files[0]['url'].split('/')[-3:])
        self.download.download_files(file)
        from pathlib import Path
        relative_path = self.download.path + file_name
        tmp_file = Path(relative_path)
        self.assertTrue(tmp_file.exists())
        shutil.rmtree(os.path.dirname(os.path.abspath(self.download.path)) + self.download.path[1:])

    def test_download_files_not_exist(self):
        """Must log info when the download a file fails"""
        file = [{'url': self.download.host + '/api/download/SJC/2017/NotExist.m'}]
        with self.assertLogs(level='INFO'):
            self.download.download_files(file)





