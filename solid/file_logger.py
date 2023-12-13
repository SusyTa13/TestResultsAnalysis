import logging
from iLogger import ILogger


class FileLogger(ILogger):
    def __init__(self, filename: str):
        self.filename = filename
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Log to a file
        file_handler = logging.FileHandler(self.filename)
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

    def error(self, message: str):
        self.logger.error(message)