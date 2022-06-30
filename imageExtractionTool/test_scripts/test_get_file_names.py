import unittest
import os
from imageExtractionTool.scripts.get_file_names import get_file_names
from imageExtractionTool.scripts.config_parser import get_config
from imageExtractionTool.scripts.create_logger import create_logger


class TestTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create CSVs for Test"""
        path = get_config()['PATHS']['csv_input']
        CSVs = ['format_0.csv',
                'format_1.csv',
                'format_2.csv',
                'format_3.csv',
                'format_error.csv'
                ]

        data = ['',
                '',
                '',
                '',
                'thisisntanimageformat.nef']

    @classmethod
    def tearDownClass(cls):
        """Delete CSVs for Test"""
        pass

    def setUp(self):
        """Create logger for Tests and get CSVS"""
        self.logger = create_logger('unittest.logs',__name__,'DEBUG')

    def tearDown(self):
        """Delete log file from tests"""
        os.remove('unittest.logs')

    def test_get_file_names_format_0(self):
        lst = get_file_names(self.logger, 'format_0.csv')

    def test_get_file_names_format_1(self):
        lst = get_file_names(self.logger, 'format_1.csv')

    def test_get_file_names_format_2(self):
        lst = get_file_names(self.logger, 'format_2.csv')

    def test_get_file_names_format_3(self):
        lst = get_file_names(self.logger, 'format_3.csv')

    def test_error_in_format(self):
        lst = get_file_names(self.logger, 'format_error.csv')


if __name__ == '__main__':
    unittest.main()
