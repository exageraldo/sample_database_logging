import os
import logging
from log4mongo.handlers import MongoHandler

"""
https://docs.python.org/3.6/library/logging.html
"""
LEVEL_DICT = {
    'CRITICAL': logging.CRITICAL, # 50
    'ERROR': logging.ERROR, # 40
    'WARNING': logging.WARNING, # 30
    'INFO': logging.INFO, # 20
    'DEBUG': logging.DEBUG, # 10
    'NOTSET': logging.NOTSET # 0
}

level = os.environ.get('LOG_LEVEL', 'DEBUG')

logger = logging.getLogger('doutorfacil')

logger.setLevel(LEVEL_DICT[level])

logger.addHandler(
        MongoHandler(
            host='localhost'
            )
        )
