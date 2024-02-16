#!/usr/bin/python3
"""
class City that inherits from Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
