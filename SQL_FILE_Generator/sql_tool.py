from utils import input_validator, file_writer

def generate_sql_file(table_name, columns, data_types, file_path):
    # Validate input
    if not input_validator.validate_input(table_name, columns, data_types):
        print("Invalid input. Please check your input and try again.")
        return

    # Generate SQL file content
    sql_content = f"CREATE TABLE {table_name} (\n"
    for col, data_type in zip(columns, data_types):
        sql_content += f"    {col} {data_type},\n"
    sql_content = sql_content.rstrip(",\n") + "\n);"

    # Write SQL file
    file_writer.write_file(sql_content, file_path)
    print(f"SQL file generated successfully: {file_path}")

if __name__ == "__main__":
    table_name = input("Enter table name: ")
    columns = input("Enter columns (comma-separated): ").split(",")
    data_types = input("Enter data types (comma-separated): ").split(",")
    file_path = input("Enter file path to save SQL file: ")

    generate_sql_file(table_name, columns, data_types, file_path)
