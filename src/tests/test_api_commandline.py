from unittest import TestCase
import src.utils.helpers as h


class APIDownloadCommandLine(TestCase):
    def test_help_h(self):
        """Must return exit code 1 when given a -h"""
        with self.assertRaises(SystemExit) as cm:
            h.get_sys_args(['-h'])
        self.assertEqual(cm.exception.args[0], 1)

    def test_help_H(self):
        """Must return exit code 1 when given a -H"""
        with self.assertRaises(SystemExit) as cm:
            h.get_sys_args(['-H'])
        self.assertEqual(cm.exception.args[0], 1)

    def test_help_help(self):
        """Must return exit code 1 when given a --help"""
        with self.assertRaises(SystemExit) as cm:
            h.get_sys_args(['--help'])
        self.assertEqual(cm.exception.args[0], 1)

    def test_invalid_args(self):
        """Must return exit code 2 when given a wrong arg"""
        with self.assertRaises(SystemExit) as cm:
            h.get_sys_args(['--heklp'])
        self.assertEqual(cm.exception.args[0], 2)

    def test_path_args(self):
        """Must return exit code 3 when it hasn't the args -p or --path"""
        with self.assertRaises(SystemExit) as cm:
            h.get_sys_args(['--app', 1])
        self.assertEqual(cm.exception.args[0], 3)

    def test_all_args(self):
        """Must return a list with 1 dict and str"""
        search, path = h.get_sys_args([
            '--app', 1,
            '-p', './tmp/'
        ])
        self.assertIsInstance(search, dict)
        self.assertIsInstance(path, str)
        self.assertTrue('application' in search)
        self.assertEqual(search['application'], 1)
        self.assertEqual(path, './tmp/')
