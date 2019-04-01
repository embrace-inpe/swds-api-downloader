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
        host = "http://www2.inpe.br/climaespacial/SpaceWeatherDataShare"
        self.download = APIDownload(credentials=login, host=host, path=path_to_save, **search)

    def test_login(self):
        """The login must return a token"""
        token = self.download.get_token()
        self.assertIsInstance(token, str)

    def test_token_format(self):
        """The token needs be with a Bearer prefix"""
        bearer_token =self.download.get_authorization()
        bearer = bearer_token.split(' ')[0]
        self.assertEqual('Bearer', bearer)

    def test_get_files_list(self):
        """Must return a files urls list"""
        files = self.download.get_files_list()
        self.assertTrue(len(files) > 0)
