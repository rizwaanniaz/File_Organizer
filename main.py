import sys
import os
from colorama import Fore, Style, init
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Add current directory to the system path

from file_sorter import FileSorter
from logger import setup_logger
from meta_handler import add_file_category
from error_handler import check_directory_exists, check_directory_permissions, DirectoryError, PermissionError
import config

# Initialize colorama for colored console output
init(autoreset=True)

# Display welcome message
print("\n" + Fore.WHITE + "*" * 45)  # Non-bold white asterisks
print(Fore.RED + "\tWELCOME TO FILE ORGANIZER")  # Bold red welcome text
print(Fore.WHITE + "*" * 45 + Style.RESET_ALL)  # Non-bold white asterisks

print("This File Organizer script is useful to organize files in a directory based on their file types.")

def get_valid_directory():
    """
    Prompt the user to enter a valid directory path, re-prompting if necessary.
    Allows the user to exit by pressing Enter without input.

    Returns:
        str: Valid directory path with write permissions.
    """
    while True:
        # Prompt user for directory input
        source_dir = input(Fore.RED + "\nPlease enter the directory to organize or press Enter to exit: ").strip()

        if source_dir == "":
            # Exit the program if the user presses Enter without input
            print(Fore.WHITE + "Exiting program.\n")
            exit(0)
        try:
            # Validate directory existence and permissions
            check_directory_exists(source_dir)
            check_directory_permissions(source_dir)
            return source_dir  # Return the valid directory path
        except DirectoryError as e:
            # Handle and display directory-related errors
            print(f"Error: {e}")
        except PermissionError as e:
            # Handle and display permission-related errors
            print(f"Error: {e}")

def main():
    """
    Main function for the File Organizer script.

    Steps:
    1. Set up the logger for tracking events.
    2. Prompt the user for a valid source directory.
    3. Organize files in the directory by their types.
    4. Allow the user to dynamically add new file categories.
    """
    # Setup logger for logging events
    logger = setup_logger()

    # Get a valid directory from the user
    source_dir = get_valid_directory()

    # Organize files in the directory
    try:
        sorter = FileSorter(source_dir)  # Initialize the FileSorter with the source directory
        sorter.organize_files()  # Perform file organization
    except Exception as e:
        # Log and display unexpected errors
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

    # Allow the user to add new file categories dynamically
    try:
        while True:
            # Prompt user to add a new file category
            new_category = input(Fore.RED + "Add a new file category (e.g., '.xyz:CustomType') or press Enter to skip: ").strip()
            if new_category == "":
                logger.info("User exited category addition.")  # Log the exit
                print(Fore.GREEN + "Exiting category addition.")
                break  # Exit the loop if the user presses Enter without input

            if ":" not in new_category or not new_category.startswith("."):
                # Log invalid input attempt
                logger.warning(f"Invalid input for new category: {new_category}")
                print(Fore.RED + "Invalid input! Please provide in the format '.xyz:CustomType'")
                continue  # Re-prompt the user

            # Split the input into extension and category
            extension, category = new_category.split(":", 1)
            # Add the new file category
            add_file_category(extension.strip(), category.strip())
            logger.info(f"Added new category: {extension.strip()} -> {category.strip()}")  # Log the addition
            print(Fore.GREEN + f"Category '{category.strip()}' for extension '{extension.strip()}' added successfully.")
    except Exception as e:
        # Log and display unexpected errors
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
