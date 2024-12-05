import config
from colorama import Fore, init


def add_file_category(extension, category):
    """
    Dynamically add a new file type and its associated category to the configuration.

    Parameters:
        extension (str): The file extension to add (e.g., ".txt").
        category (str): The category name to associate with the file extension.

    Behavior:
        - If the extension already exists in the configuration, a message is displayed, and no changes are made.
        - If the extension is new, it is added to the `FILE_TYPES` dictionary and saved persistently.
    """
    if extension in config.FILE_TYPES:
        # Notify the user if the extension already exists in the configuration
        print(f"{extension} already exists in the configuration.")
    else:
        # Add the new file extension and category to the dictionary
        config.FILE_TYPES[extension] = category
        print(Fore.GREEN + f"Added new category: {extension.strip()} -> {category.strip()}")

        # Save the updated configuration to the `config.py` file
        save_file_types()

def save_file_types():
    """
    Save the updated FILE_TYPES dictionary back to the `config.py` file.

    This function writes the `FILE_TYPES` dictionary in a human-readable format.
    It ensures that changes made to the configuration during runtime are persistently stored.

    Steps:
        1. Open `config.py` in write mode.
        2. Write a header comment for context.
        3. Write the updated `FILE_TYPES` dictionary line by line.
        4. Close the file automatically using a context manager.
    """
    with open("config.py", "w") as config_file:
        config_file.write("# Configuration for file types\n")
        config_file.write("FILE_TYPES = {\n")
        # Iterate through the dictionary and write each key-value pair
        for ext, folder in config.FILE_TYPES.items():
            config_file.write(f"    '{ext}': '{folder}',\n")
        # Close the dictionary
        config_file.write("}\n")
