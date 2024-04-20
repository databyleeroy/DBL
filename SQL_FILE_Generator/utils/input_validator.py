def validate_input(table_name, columns, data_types):
    # Check if table name is valid
    if not table_name:
        return False

    # Check if columns and data types have the same length
    if len(columns) != len(data_types):
        return False

    # Check if columns and data types are not empty
    if not all(columns) or not all(data_types):
        return False

    return True
