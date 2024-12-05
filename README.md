# File Organizer Project for Pythong Scripting

## Overview
The File Organizer is a Python-based application that categorizes and organizes files within a directory based on their file types. It includes features such as dynamic file category management, logging, and comprehensive error handling.

---

## Features
- Organizes files into subdirectories based on their extensions.
- Allows dynamic addition of new file categories during runtime.
- Logs operations and errors to a `file_organizer.log` file.
- Includes comprehensive unit tests for core functionality.

---

## Installation and Setup

# Step 1: Clone or Download the Repository**
- Clone the repository (if using Git):
  ```bash
  git clone <URL>


Or download the project files as a ZIP and extract them.

# Step 2 Install Dependencies
- Open a terminal or command prompt in the project directory.
Install pytest for running tests:

- install Pytest (in bash)

  ```pip install pytest```


# Usage Instructions

Running the Program:

Navigate to the project directory in the terminal and run main.py

Follow the on-screen prompts and 'Enter the directory to organize.'

# Configuration of defined files in config.py

File type mappings are defined in config.py:(you can add new file categories during runtime using the format .ext:Category )

FILE_TYPES = {```
    '.txt': 'TextFiles',
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
    '.docx': 'Documents',
    '.xlsx': 'Spreadsheets',
    '.exe': 'Applications',
    '.html': 'WebFiles',
    '.csv': 'DataFiles',
    '.pptx': 'Presentations',
    '.zip': 'CompressedFiles',
    '.md': 'MarkdownFiles',
}```


# Logs
All operations and errors are logged in the file_organizer.log file located in the project directory.

# Testing
To ensure the program functions correctly, run the included unit tests:

1. Open a terminal in the project directory.
2. Execute the tests(in bash)

   ```bash
   cd project directory
   pytest -v test_project.py

Expected output:

==================================================================================================================================== test session starts =====================================================================================================================================
platform win32 -- Python 3.11.9, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\Rizwan niaz\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Rizwan niaz\OneDrive - OsloMet\Semester 3\scripting\file_organizer
collected 8 items

test_project.py::test_file_sorter_organize_files PASSED                                                                                                                                                                                                                                 [ 12%]
test_project.py::test_file_sorter_invalid_directory PASSED                                                                                                                                                                                                                              [ 25%]
test_project.py::test_add_file_category PASSED                                                                                                                                                                                                                                          [ 37%]
test_project.py::test_add_existing_file_category PASSED                                                                                                                                                                                                                                 [ 50%]
test_project.py::test_check_directory_exists PASSED                                                                                                                                                                                                                                     [ 62%]
test_project.py::test_check_directory_does_not_exist PASSED                                                                                                                                                                                                                             [ 75%] 
test_project.py::test_check_directory_permissions PASSED                                                                                                                                                                                                                                [ 87%] 
test_project.py::test_logger PASSED                                                                                                                                                                                                                                                     [100%] 

===================================================================================================================================== 8 passed in 0.08s ====================================================================================================================================== 


# Troubleshooting

Invalid Directory:
Ensure the directory path exists and is accessible.
Check for typos in the directory path.


Dynamic Category Error:
Use the format .ext:Category when adding new categories dynamically.