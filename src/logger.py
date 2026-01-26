# logger.py
import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = 'logs'  # Your log folder name

def setup_logger(module_name, log_file=None, level=logging.INFO):
    """
    Setup a logger for a specific module with its own log file
    
    Args:
        module_name: Name of the module (use __name__)
        log_file: Optional custom log filename (defaults to module_name.log)
        level: Logging level
    """
    # Create logs directory if it doesn't exist
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Use module name for log file if not specified
    if log_file is None:
        log_file = f"{module_name.replace('.', '_')}.log"
    
    log_path = os.path.join(LOG_DIR, log_file)
    
    # Get logger for this module
    logger = logging.getLogger(module_name)
    logger.setLevel(level)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # File handler - specific to this module
    file_handler = RotatingFileHandler(
        log_path, 
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter('%(levelname)s - %(name)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger