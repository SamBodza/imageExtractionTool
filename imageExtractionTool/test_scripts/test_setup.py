import unittest
from shutil import rmtree
import os

from imageExtractionTool.scripts.config_parser import get_config
from imageExtractionTool.scripts.setup import mk_dirs


class TestSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Deletes all folders at the start of the test"""
        path = get_config()['PATHS']['csv_input']
        for fldr in os.listdir(path):
            if 'unittest' in fldr:
                rmtree(os.path.join(path, fldr))

    @classmethod
    def tearDownClass(cls):
        """Deletes all folders at the end of the test"""
        path = get_config()['PATHS']['csv_input']
        for fldr in os.listdir(path):
            if 'unittest' in fldr:
                rmtree(os.path.join(path, fldr))

    def setUp(self):
        """Raises exception if folders with unittest exist"""
        path = get_config()['PATHS']['csv_input']
        for fldr in os.listdir(path):
            if 'unittest' in fldr:
                raise PermissionError(f'unittest folders still exist')

    def tearDown(self):
        """Deletes all folders at the end of every test"""
        path = get_config()['PATHS']['csv_input']
        for fldr in os.listdir(path):
            if 'unittest' in fldr:
                rmtree(os.path.join(path, fldr))

    def test_mk_dirs_GETNAMES(self):
        """Test to check only correct directories made"""
        _, fldr_path = mk_dirs('GETNAMES_unittest.csv')
        paths = [fldr_path,
                 os.path.join(fldr_path, 'csv'),
                 os.path.join(fldr_path, 'logs')
                 ]

        for path in paths:
            self.assertTrue(os.path.exists(path))

    def test_mk_dirs_GETIMAGES(self):
        """Test to check only correct directories made"""
        _, fldr_path = mk_dirs('GETIMAGES_unittest.csv')
        paths = [fldr_path,
                 os.path.join(fldr_path, 'csv'),
                 os.path.join(fldr_path, 'logs'),
                 os.path.join(fldr_path, 'images')
                 ]

        for path in paths:
            self.assertTrue(os.path.exists(path))

    def test_mk_dirs_GETEXIF(self):
        """Test to check only correct directories made"""
        _, fldr_path = mk_dirs('GETEXIF_unittest.csv')
        paths = [fldr_path,
                 os.path.join(fldr_path, 'csv'),
                 os.path.join(fldr_path, 'logs'),
                 os.path.join(fldr_path, 'images'),
                 os.path.join(fldr_path, 'logs', 'failed_exif'),
                 os.path.join(fldr_path, 'logs', 'exif')
                 ]

        for path in paths:
            self.assertTrue(os.path.exists(path))

    def test_mk_dirs_GETSAMPLE(self):
        """Test to check only correct directories made"""
        _, fldr_path = mk_dirs('GETSAMPLE_unittest.csv')
        paths = [fldr_path,
                 os.path.join(fldr_path, 'csv'),
                 os.path.join(fldr_path, 'logs'),
                 os.path.join(fldr_path, 'logs', 'sample_internal'),
                 os.path.join(fldr_path, 'logs', 'sample_external')
                 ]

        for path in paths:
            self.assertTrue(os.path.exists(path))

    def test_mk_dirs(self):
        """Test to check only correct directories made"""
        _, fldr_path = mk_dirs('unittest.csv')
        paths = [fldr_path,
                 os.path.join(fldr_path, 'csv'),
                 os.path.join(fldr_path, 'logs'),
                 os.path.join(fldr_path, 'images'),
                 os.path.join(fldr_path, 'logs', 'failed_exif'),
                 os.path.join(fldr_path, 'logs', 'exif'),
                 os.path.join(fldr_path, 'logs', 'sample_internal'),
                 os.path.join(fldr_path, 'logs', 'sample_external')
                 ]

        for path in paths:
            self.assertTrue(os.path.exists(path))


# runs all test inside class
if __name__ == '__main__':
    unittest.main()
