import logging

def setup_logger():
    """
    Sets up a singleton logger instance to prevent duplicate handlers.
    """
    logger = logging.getLogger("FileOrganizer")
    if not logger.handlers:  # Ensure handlers are attached only once
        logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)

        # File handler
        file_handler = logging.FileHandler("file_organizer.log")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)

        # Attach handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
