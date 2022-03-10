import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class Images(Base):
    __tablename__ = 'images'

    title = Column(VARCHAR(255), nullable=False)
    image = Column(VARCHAR(255), nullable=False)
    user_id = Column(Integer, nullable=False)
    chat_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())  # Column(TIMESTAMP, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now())  # Column(TIMESTAMP, nullable=False)
    is_converted = Column(Boolean, default=False)
    pdf_file = Column(Integer, ForeignKey('pdf_file.id', ondelete='CASCADE'), nullable=False, index=True)


class PdfFiles(Base):
    __tablename__ = 'pdf_file'

    title = Column(VARCHAR(255), nullable=False)
    user_id = Column(Integer, nullable=False)
    chat_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())  # Column(TIMESTAMP, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now())  # Column(TIMESTAMP, nullable=False)
    to_delete = Column(Boolean, default=False)
