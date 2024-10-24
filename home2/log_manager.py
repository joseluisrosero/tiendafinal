import logging
from logging.handlers import RotatingFileHandler

class LogManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LogManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, logfile='app.log', max_bytes=1024*1024, backup_count=3):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger('AppLogger')
            self.logger.setLevel(logging.DEBUG)
            handler = RotatingFileHandler(logfile, maxBytes=max_bytes, backupCount=backup_count)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)
