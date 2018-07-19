from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:123@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    logger = Column(String)
    level = Column(String)
    trace = Column(String)
    msg = Column(String)
    extra = Column(String)
    created_at = Column(DateTime, default=func.now())

    def __init__(self, logger=None, level=None, trace=None, msg=None, extra=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg
        self.extra = extra

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])


Base.metadata.create_all(engine)
