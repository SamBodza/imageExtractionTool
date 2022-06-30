import unittest
from unittest.mock import patch


# inherits from unittest.TestCase
class TestTemplate(unittest.TestCase):

    # runs at initialisation of script
    # could be used to populate DB or create files
    @classmethod
    def setUpClass(cls):
        pass

    # runs at end of script
    # could be used to remove anything hanging
    @classmethod
    def tearDownClass(cls):
        pass

    # runs at start of every test
    # inbuilt function to keep code DRY (Don't Repeat Yourself)
    def setUp(self):
        pass

    # runs at end of every test
    def tearDown(self):
        pass

    # function tests are not run in order!
    # so test must be isolated from each other

    # tests function 0
    def test_function_0(self):
        pass

    # tests function 1
    def test_function_1(self):
        pass

    # tests function 2
    def test_function_2(self):
        pass


# runs all test inside class
if __name__ == '__main__':
    unittest.main()