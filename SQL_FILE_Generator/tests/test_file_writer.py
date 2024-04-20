import unittest
from utils import file_writer
import os

class TestFileWriter(unittest.TestCase):

    def test_write_file(self):
        content = "CREATE TABLE test_table (col1 int, col2 text);"
        file_path = "test_directory/test_file.sql"

        file_writer.write_file(content, file_path)

        self.assertTrue(os.path.exists(file_path))

        with open(file_path, "r") as f:
            self.assertEqual(f.read(), content)

        # Clean up
        os.remove(file_path)
        os.rmdir("test_directory")
