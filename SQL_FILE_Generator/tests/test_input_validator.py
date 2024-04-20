import unittest
from utils import input_validator

class TestInputValidator(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(input_validator.validate_input("table_name", ["col1", "col2"], ["int", "text"]))

    def test_invalid_table_name(self):
        self.assertFalse(input_validator.validate_input("", ["col1", "col2"], ["int", "text"]))

    def test_invalid_columns_data_types_length(self):
        self.assertFalse(input_validator.validate_input("table_name", ["col1", "col2"], ["int"]))

    def test_empty_columns_data_types(self):
        self.assertFalse(input_validator.validate_input("table_name", ["col1", ""], ["int", ""]))
