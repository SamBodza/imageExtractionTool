import unittest
import os
import csv
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from imageExtractionTool.scripts.get_file_names import get_file_names
from imageExtractionTool.scripts.config_parser import get_config
from imageExtractionTool.scripts.create_logger import create_logger


class TestFileNames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create CSVs for Test"""
        path = get_config()['PATHS']['csv_input']

        CSVs = ['unittest_format_0.csv',
                'unittest_format_1.csv',
                'unittest_format_2.csv',
                'unittest_format_3.csv',
                'unittest_format_error.csv'
                ]

        data = ['filestorage://[SERVER]/[PATH]/Img_cee0d57f-b66c-4913-beda-25705b710fee?Full=jpg;Thumbnail=jpg',
                'Img_cee0d57f-b66c-4913-beda-25705b710fee_Full.jpg',
                'Img_cee0d57f-b66c-4913-beda-25705b710fee',
                'cee0d57f-b66c-4913-beda-25705b710fee',
                'this-isnt-an-image-format.nef'
                ]

        for file_name, csv_file in zip(data, CSVs):
            csv_path = os.path.join(path, csv_file)
            with open(csv_path, "w") as file:
                writer = csv.writer(file)
                writer.writerow([file_name])

    @classmethod
    def tearDownClass(cls):
        """Delete CSVs for Test"""
        path = get_config()['PATHS']['csv_input']
        for file in os.listdir(path):
            if 'unittest_format_' in file:
                os.remove(os.path.join(path, file))

    def setUp(self):
        """Create logger for Tests and get CSVS"""
        self.logger = create_logger('unittest.logs', __name__, 'DEBUG')
        self.result = 'Img_cee0d57f-b66c-4913-beda-25705b710fee_Full.jpg'

    def tearDown(self):
        """Delete log file from tests"""
        os.remove('unittest.logs')

    def test_get_file_names_format_0(self):
        lst = get_file_names(self.logger, 'unittest_format_0.csv')
        self.assertEqual(lst[0], self.result)

    def test_get_file_names_format_1(self):
        lst = get_file_names(self.logger, 'unittest_format_1.csv')
        self.assertEqual(lst[0], self.result)

    def test_get_file_names_format_2(self):
        lst = get_file_names(self.logger, 'unittest_format_2.csv')
        self.assertEqual(lst[0], self.result)

    def test_get_file_names_format_3(self):
        lst = get_file_names(self.logger, 'unittest_format_3.csv')
        self.assertEqual(lst[0], self.result)

    def test_error_in_format(self):
        self.assertRaises(ValueError, get_file_names, self.logger, 'unittest_format_error.csv')


if __name__ == '__main__':
    unittest.main()
