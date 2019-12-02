import os
import subprocess
from unittest import TestCase
from app.settings import TEMP, EXAMPLE_SOURCE
from app.manage import download_repo, get_data_from_repo


class TestEndToEnd(TestCase):
    def setUp(self):
        subprocess.run(["rm", "-r", TEMP])

    def tearDown(self):
        subprocess.run(["rm", "-r", TEMP])

    def test_download_repo(self):
        self.assertFalse(os.path.exists(TEMP))
        self.assertFalse(os.path.exists(EXAMPLE_SOURCE))
        download_repo()
        self.assertTrue(os.path.exists(TEMP))
        self.assertTrue(os.path.exists(EXAMPLE_SOURCE))

    def test_data_from_repo(self):
        download_repo()
        self.assertTrue(len(get_data_from_repo()) > 0)

        self.tearDown()
        with self.assertRaises(FileNotFoundError):
            get_data_from_repo()
