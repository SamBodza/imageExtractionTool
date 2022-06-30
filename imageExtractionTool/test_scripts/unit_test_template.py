import unittest
from unittest.mock import patch


# inherits from unittest.TestCase
class TestTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_function_0(self):
        pass

    def test_function_1(self):
        pass

    def test_function_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
