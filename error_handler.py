import os

# Custom exception for directory-related errors
class DirectoryError(Exception):
    """
    Custom error for handling issues related to directories.
    Raised when a directory does not exist.
    """
    pass

# Custom exception for permission-related errors
class PermissionError(Exception):
    """
    Custom error for handling permission-related issues.
    Raised when the program does not have write permissions for a directory.
    """
    pass

def check_directory_exists(directory):
    """
    Checks if the specified directory exists.
    
    Parameters:
        directory (str): Path to the directory to check.

    Raises:
        DirectoryError: If the specified directory does not exist.
    """
    if not os.path.exists(directory):  # Check if the directory path exists
        raise DirectoryError(f"Directory '{directory}' does not exist.")  # Raise a custom error if it doesn't

def check_directory_permissions(directory):
    """
    Checks if the program has write permissions for the specified directory.
    
    Parameters:
        directory (str): Path to the directory to check.

    Raises:
        PermissionError: If the program does not have write permissions for the directory.
    """
    if not os.access(directory, os.W_OK):  # Check if the directory is writable
        raise PermissionError(f"No write permission for directory '{directory}'.")  # Raise a custom error if not
