import os

def write_file(content, file_path):
    # Create directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write content to file
    with open(file_path, "w") as f:
        f.write(content)
