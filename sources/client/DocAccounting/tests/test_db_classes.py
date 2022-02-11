# coding: utf-8
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Testtable(Base):
    __tablename__ = 'testtable'

    value1 = Column(Text)
    id = Column(INTEGER(11), primary_key=True)
