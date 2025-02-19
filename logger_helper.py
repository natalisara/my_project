import logging
import functools
import os
import sys

# Create a logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "project.log")

# Create and configure a logger for our project
logger = logging.getLogger("my_project_logger")
logger.setLevel(logging.INFO)
logger.propagate = False  # Prevent log messages from being passed to the root logger

# Create a console handler that writes to sys.stdout
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(console_formatter)

# Create a file handler that writes to 'logs/project.log'
file_handler = logging.FileHandler(log_file, mode="a")
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test that the logger is working
logger.info("Logger configured successfully.")


def log_decorator(func):
    """Decorator to log the start and finish of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Finished '{func.__name__}'")
        return result

    return wrapper
