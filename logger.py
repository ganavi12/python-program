import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=3)
for _ in range(10000):
    logger.warning("this is warning message")
    logger.error("this is error message")
