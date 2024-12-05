import pytest
import os
from file_sorter import FileSorter
from meta_handler import add_file_category
from error_handler import check_directory_exists, check_directory_permissions, DirectoryError, PermissionError
from logger import setup_logger
import config

# Test 1:  the FileSorter class for organization of files into categorized subdirectories
def test_file_sorter_organize_files(tmp_path):
    """
    Test the `organize_files` method of the FileSorter class.

    Steps:
    1. Create a temporary directory and populate it with test files.
    2. Instantiate the FileSorter and call `organize_files`.
    3. Verify that files are moved to the correct subdirectories.
    """
    # Create a temporary test directory and sample files
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "test.txt").write_text("Sample text file")
    (test_dir / "test.pdf").write_text("Sample PDF file")
    (test_dir / "test.jpg").write_text("Sample image file")
    
    # Initialize FileSorter and organize files
    sorter = FileSorter(test_dir)
    sorter.organize_files()
    
    # Assert that files are moved to their respective categories
    assert (test_dir / "TextFiles" / "test.txt").exists()
    assert (test_dir / "PDFs" / "test.pdf").exists()
    assert (test_dir / "Images" / "test.jpg").exists()

# Test 2:  handling of invalid directories
def test_file_sorter_invalid_directory():
    """
    Test that FileSorter raises a DirectoryError for an invalid directory.
    """
    invalid_dir = "non_existent_directory"  # Path does not exist
    with pytest.raises(DirectoryError):  # Expect DirectoryError
        sorter = FileSorter(invalid_dir)  # Instantiate FileSorter

# Test 3: the meta_handler module for dynamically adding a new file category
def test_add_file_category():
    """
    Test dynamically adding a new file category using `add_file_category`.

    Asserts:
    - The new file category is added to the configuration.
    """
    add_file_category(".testext", "TestFiles")
    assert config.FILE_TYPES[".testext"] == "TestFiles"

# Test 4: testing the duplicate file category and ensuring a warning is issued
def test_add_existing_file_category(capfd):
    """
    Test attempting to add a duplicate file category using `add_file_category`.

    Asserts:
    - The function outputs a warning about the existing category.
    """
    add_file_category(".txt", "Duplicate")
    captured = capfd.readouterr()  # Capture stdout
    assert "already exists in the configuration" in captured.out

# Test 5: validation of an existing directory.
def test_check_directory_exists(tmp_path):
    """
    Test `check_directory_exists` for an existing directory.
    
    Asserts:
    - No exception is raised for a valid directory.
    """
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    try:
        check_directory_exists(test_dir)  # Should pass without exceptions
    except DirectoryError:
        pytest.fail("DirectoryError raised unexpectedly")

# Test 6: validation of a non-existent directory
def test_check_directory_does_not_exist():
    """
    Test `check_directory_exists` for a non-existent directory.
    
    Asserts:
    - A DirectoryError is raised for an invalid directory.
    """
    invalid_dir = "non_existent_directory"
    with pytest.raises(DirectoryError):
        check_directory_exists(invalid_dir)

# Test 7: checking write permission checks for a directory
def test_check_directory_permissions(tmp_path):
    """
    Test `check_directory_permissions` for a writable directory.

    Asserts:
    - No exception is raised for a directory with write permissions.
    """
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    try:
        check_directory_permissions(test_dir)  # Should pass without exceptions
    except PermissionError:
        pytest.fail("PermissionError raised unexpectedly")

# Test 8: testing the proper initialization of logger setup
def test_logger():
    """
    Test the `setup_logger` function.

    Asserts:
    - Logger is correctly initialized with a name and handlers.
    """
    logger = setup_logger()
    assert logger.name == "FileOrganizer"  # Logger name should match
    assert len(logger.handlers) > 0  # Logger should have at least one handler
