"""
logging_ file Designed by Anurag Gupta
 :date:  04-02-2024
 :author: Anurag Gupta
"""
import logging
import inspect
import path
from lib.utils import read_test_data_file
TEST_FILE = read_test_data_file(r"\test_data\log.json")


def get_logger(level: int = logging.INFO):
    # Getting Function name
    function_name = inspect.stack()[1][3]
    # module_name = inspect.stack()[1][3]

    # Getting logger with function name
    logger = logging.getLogger(name=function_name)

    # Setting Logger level
    logger.setLevel(level)

    # Getting Logger handler (Console and file)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=f"{path.get_project_path()}/logs/{function_name}.log", mode='a')

    # Setting log level for File and Console handler
    console_handler.setLevel(level=logging.ERROR)
    file_handler.setLevel(level=level)

    # Log formatter
    formatter_ = logging.Formatter(fmt=TEST_FILE["log_format"], datefmt="%dd-%b-%YYYY T %H:%M:%SS")

    # Setting log formatter to file and console handler
    file_handler.setFormatter(formatter_)
    console_handler.setFormatter(formatter_)

    # Adding Handlers to loggers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
