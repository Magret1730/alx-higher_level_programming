#!/usr/bin/python3
"""
python file that contains the class definition of a State and an
instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base

    Attributes:
    id = Not Null, Autoincrements
    name = String and not not null
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
