from unittest import TestCase

from src.api import APIDownload


class ApiDownloadHostTest(TestCase):
    def test_host_not_empty(self):
        """The host cannot be empty"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={}, host='')
        error_msg = 'The variable host needs an URL value'
        self.assertEqual(cm.exception.args[0].msg, error_msg)

    def test_host_is_a_url(self):
        """The host must be a URL"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={}, host='www.1')
        error_msg = 'The variable host is not a valid URL e.g: "http://apidomain.com"'
        self.assertEqual(cm.exception.args[0].msg, error_msg)

    def test_host_is_valid(self):
        """The host must be a valid host"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={}, host='http://www.donotexistdomainbyswds.com')
        error_msg = 'The variable host is not a valid URL e.g: "http://apidomain.com"'
        self.assertEqual(cm.exception.args[0].msg, error_msg)


class ApiDownloadCredentialsTest(TestCase):
    def test_credentials_has_username_key(self):
        """The credentials must has the username key"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={'password': 'mypass'}, host='http://google.com')
        error_msg = 'The login dictonary must has a key called username'
        self.assertEqual(cm.exception.args[0].msg, error_msg)

    def test_credentials_username_key_not_empty(self):
        """The credentials username key must be not empty"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={'password': 'mypass', 'username': ''}, host='http://google.com')
        error_msg = 'The username key on login dictonary cannot be empty'
        self.assertEqual(cm.exception.args[0].msg, error_msg)

    def test_credentials_has_password_key(self):
        """The credentials must has the password key"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={'username': 'myname'}, host='http://google.com')
        error_msg = 'The login dictonary must has a key called password'
        self.assertEqual(cm.exception.args[0].msg, error_msg)

    def test_credentials_password_key_not_empty(self):
        """The credentials password key must be not empty"""
        with self.assertRaises(SystemExit) as cm:
            APIDownload(credentials={'password': '', 'username': 'myname'}, host='http://google.com')
        error_msg = 'The password key on login dictonary cannot be empty'
        self.assertEqual(cm.exception.args[0].msg, error_msg)

