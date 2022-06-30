import unittest
import os

from imageExtractionTool.scripts.create_logger import create_logger
from imageExtractionTool.scripts.get_file_paths import (extract_path,
                                                        connect_single,
                                                        get_file_paths_backup,
                                                        get_file_paths)



class TestTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """Create logger for Tests and get CSVS"""
        self.logger = create_logger('unittest.logs', __name__, 'DEBUG')

    def tearDown(self):
        os.remove('unittest.logs')

    def test_extract_path(self):
        pass

    def test_function_1(self):
        pass

    def test_function_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
