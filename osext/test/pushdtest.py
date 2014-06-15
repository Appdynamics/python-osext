import os
import unittest
import osext

from osext.pushdcontext import pushd

class TestFunctions(unittest.TestCase):
    def test_pushd_usage(self):
        try:
            os.makedirs('__test_dir__')
        except OSError:
            os.rmdir('__test_dir__')
            os.makedirs('__test_dir__')

        self.assertNotIn('__test_dir__', os.getcwd())

        with pushd('./__test_dir__'):
            self.assertIn('__test_dir__', os.getcwd())

        self.assertNotIn('__test_dir__', os.getcwd())

        os.rmdir('__test_dir__')
