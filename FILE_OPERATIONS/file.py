def read_file(file_path):
    """
    Read the contents of a file and return as a string.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write_file(file_path, content):
    """
    Write the given content to a file.
    """
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    """
    Append the given content to the end of a file.
    """
    with open(file_path, 'a') as file:
        file.write(content)


def copy_file(source_path, destination_path):
    """
    Copy a file from the source path to the destination path.
    """
    with open(source_path, 'rb') as source_file:
        with open(destination_path, 'wb') as destination_file:
            destination_file.write(source_file.read())


def delete_file(file_path):
    """
    Delete a file from the file system.
    """
    import os
    os.remove(file_path)


if __name__ == '__main__':
    # Example usage
    file_path = 'example.txt'

    # Read the contents of a file
    content = read_file(file_path)
    print(content)

    # Write content to a file
    new_content = 'This is the new content.'
    write_file(file_path, new_content)

    # Append content to a file
    appended_content = 'This is the appended content.'
    append_to_file(file_path, appended_content)

    # Copy a file to a new location
    destination_path = 'copy_example.txt'
    copy_file(file_path, destination_path)

    # Delete a file
    delete_file(file_path)
