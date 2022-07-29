#!/usr/bin/python3
""" This module creates a relationship with the State
for the cities
"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    This is the class for city - with id and name
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
