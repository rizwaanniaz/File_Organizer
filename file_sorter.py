import os
import shutil
import config
from logger import setup_logger
import re
from error_handler import check_directory_exists, check_directory_permissions, DirectoryError, PermissionError

class FileSorter:
    """
    A class for organizing files in a specified source directory into categorized subdirectories
    based on their file extensions.

    Attributes:
        source_dir (str): The source directory to organize.
        logger (logging.Logger): Logger instance for logging activities.
    """
    def __init__(self, source_dir):
        """
        Initializes the FileSorter with the source directory and sets up the logger.

        Parameters:
            source_dir (str): Path to the directory containing files to be organized.
        """
        self.source_dir = source_dir
        self.logger = setup_logger()
        # Validate directory during initialization
        check_directory_exists(self.source_dir)
        check_directory_permissions(self.source_dir)

    def organize_files(self):
        """
        Organizes files in the source directory into categorized subdirectories.

        Logs overall operations and handles exceptions gracefully.
        """
        try:
            check_directory_exists(self.source_dir)
            check_directory_permissions(self.source_dir)
            self.logger.info(f"Organizing files in {self.source_dir}")

            for filename in os.listdir(self.source_dir):
                file_path = os.path.join(self.source_dir, filename)
                if os.path.isfile(file_path):
                    try:
                        self._move_file(file_path, filename)
                    except PermissionError as e:
                        # Log permission issues as WARNING
                        self.logger.warning(f"Permission denied for {filename}: {e}")
                    except Exception as e:
                        # Log all other file-specific errors as ERROR
                        self.logger.error(f"Error processing {filename}: {e}")
        except Exception as e:
            self.logger.error(f"Failed to organize files: {e}")

    def _move_file(self, file_path, filename):
        """
        Moves a file to its categorized subdirectory based on its extension,
        handling naming conflicts by appending a numeric suffix.

        Logs INFO for successful movements, WARNING for skipped files (e.g., permission issues), and ERROR for critical failures.
        """
        try:
            file_ext = re.search(r'\.\w+$', filename)
            if not file_ext:
                self.logger.warning(f"Skipping file with no extension: {filename}")
                return

            file_ext = file_ext.group(0)
            file_category = config.FILE_TYPES.get(file_ext, "Others")
            dest_dir = os.path.join(self.source_dir, file_category)
            os.makedirs(dest_dir, exist_ok=True)

            dest_path = os.path.join(dest_dir, filename)
            base_name, ext = os.path.splitext(filename)

            # Handle naming conflicts
            counter = 1
            while os.path.exists(dest_path):
                new_filename = f"{base_name}({counter}){ext}"
                dest_path = os.path.join(dest_dir, new_filename)
                counter += 1

            shutil.move(file_path, dest_path)
            self.logger.info(f"Moved {filename} to {dest_dir}")
        except PermissionError as e:
            # Log permission issues as WARNING
            self.logger.warning(f"Permission denied for {filename}: {e}")
        except OSError as e:
            # Log other OS-related errors as ERROR
            self.logger.error(f"Critical error while processing {filename}: {e}")
        except Exception as e:
            # Log unexpected errors as ERROR
            self.logger.error(f"Unexpected error while moving {filename}: {e}")
