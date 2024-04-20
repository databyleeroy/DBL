# SQL File Generator

## Overview
The SQL File Generator is a Python tool that generates SQL files based on user input for table name, columns, and data types.

## Usage
1. Run `sql_file_generator.py` to generate an SQL file.
2. Enter the table name, columns, data types, and file path as prompted.
3. The generated SQL file will be saved to the specified file path.

## Project Structure
- `sql_file_generator.py`: Main Python script for SQL file generation.
- `utils/`
  - `input_validator.py`: Utility module for input validation.
  - `file_writer.py`: Utility module for file writing.
- `tests/`
  - `test_input_validator.py`: Unit tests for `input_validator.py`.
  - `test_file_writer.py`: Unit tests for `file_writer.py`.
- `README.md`: Project documentation and instructions.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignore file.
