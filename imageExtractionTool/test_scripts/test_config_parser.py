import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from imageExtractionTool.scripts.config_parser import get_config


class TestConfigParser(unittest.TestCase):

    def setUp(self):
        self.config = get_config()

    def test_logging_level(self):
        self.assertEqual(self.config['LOGGING']['LOGGING_LEVEL'],
                         'INFO')

    def test_paths_img_src(self):
        self.assertEqual(self.config['PATHS']['img_src'],
                         '/mnt/imageExtraction/prodrun003')

    def test_paths_img_dst(self):
        self.assertEqual(self.config['PATHS']['img_dst'],
                         '/mnt/imageExtraction/jpgExtractionTool/output')

    def test_paths_csv_input(self):
        self.assertEqual(self.config['PATHS']['csv_input'],
                         '/mnt/imageExtraction/jpgExtractionTool/input')

    def test_db_db_backup(self):
        self.assertEqual(self.config['DB']['db_backup'],
                         '/mnt/imageExtraction/jpgExtractionTool/Documentation/jpgstock.csv')

    def test_exif_config(self):
        self.assertEqual(self.config['EXIF']['config'],
                         '/usr/exiftool_config')


if __name__ == '__main__':
    unittest.main()
