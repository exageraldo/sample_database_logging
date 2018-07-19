import logging
from .models import Log, session
import traceback
import json


class SQLAlchemyHandler(logging.Handler):
    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc(exc)
        log = Log(
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg'],)
        if hasattr(record, 'extra'):
            log.extra = json.dumps(record.extra)
        session.add(log)
        session.commit()
