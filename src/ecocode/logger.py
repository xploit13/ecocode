# logger.py
# Extended implementation for logging operations in EcoCode

import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(log_file="ecocode.log", level=logging.INFO, max_size=5 * 1024 * 1024, backup_count=5):
    """
    Configure logging for EcoCode with enhanced features.

    Args:
        log_file (str): Path to the log file.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        max_size (int): Maximum size of the log file in bytes before rotation.
        backup_count (int): Number of backup log files to retain.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("EcoCodeLogger")
    logger.setLevel(level)

    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Console handler for real-time logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Rotating file handler for persistent logs
    file_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    file_handler.setLevel(level)
    file_formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s (%(filename)s:%(lineno)d)')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger
