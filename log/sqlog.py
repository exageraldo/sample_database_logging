import logging
from .sql.handler import SQLAlchemyHandler

from . import logging_level

"""
https://docs.python.org/3.6/library/logging.html
"""
LEVEL_DICT = {
    'CRITICAL': logging.CRITICAL,  # 50
    'ERROR': logging.ERROR,  # 40
    'WARNING': logging.WARNING,  # 30
    'INFO': logging.INFO,  # 20
    'DEBUG': logging.DEBUG,  # 10
    'NOTSET': logging.NOTSET  # 0
}

logger = logging.getLogger('doutorfacil')

logger.setLevel(LEVEL_DICT[logging_level])

logger.addHandler(
    SQLAlchemyHandler()
    )
