# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Text
from sqlalchemy.dialects.mysql import INTEGER, LONGBLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CategoryDoc(Base):
    __tablename__ = 'category_docs'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)


class Department(Base):
    __tablename__ = 'departments'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)


class Developer(Base):
    __tablename__ = 'developers'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)
    comments = Column(Text)


class Position(Base):
    __tablename__ = 'positions'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)


class Regulation(Base):
    __tablename__ = 'regulations'

    code = Column(INTEGER(11), primary_key=True)
    category = Column(Text)
    title = Column(Text)
    docs = Column(LONGBLOB)
    docs_ext = Column(Text)
    url = Column(Text)


class Source(Base):
    __tablename__ = 'sources'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)


class StatusDoc(Base):
    __tablename__ = 'status_docs'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)
    description = Column(Text)


class ViewDoc(Base):
    __tablename__ = 'view_docs'

    code = Column(INTEGER(11), primary_key=True)
    title = Column(Text)
    description = Column(Text)


class Employee(Base):
    __tablename__ = 'employees'

    code = Column(INTEGER(11), primary_key=True)
    positions_code = Column(ForeignKey('positions.code'), index=True)
    departments_code = Column(ForeignKey('departments.code'), index=True)
    allnames = Column(Text)
    email = Column(Text)
    login = Column(Text)
    password = Column(Text)
    editable = Column(Text)
    reading = Column(Text)

    department = relationship('Department')
    position = relationship('Position')


class Doc(Base):
    __tablename__ = 'docs'

    code = Column(INTEGER(11), primary_key=True)
    category_code = Column(ForeignKey('category_docs.code'), index=True)
    view_code = Column(ForeignKey('view_docs.code'), index=True)
    employee_code = Column(ForeignKey('employees.code'), index=True)
    status_code = Column(ForeignKey('status_docs.code'), index=True)
    developer_code = Column(ForeignKey('developers.code'), index=True)
    source_code = Column(ForeignKey('sources.code'), index=True)
    title = Column(Text)
    date_loading = Column(DateTime)
    date_change = Column(DateTime)
    barcode = Column(Text)
    keywords = Column(Text)
    section_number = Column(INTEGER(11))
    pages = Column(INTEGER(11))
    copy_n = Column(INTEGER(11))
    cupboard = Column(Text)
    rack = Column(Text)
    description = Column(Text)
    docs = Column(LONGBLOB)
    docs_ext = Column(Text)
    sizeMB = Column(Text)

    category_doc = relationship('CategoryDoc')
    developer = relationship('Developer')
    employee = relationship('Employee')
    source = relationship('Source')
    status_doc = relationship('StatusDoc')
    view_doc = relationship('ViewDoc')
