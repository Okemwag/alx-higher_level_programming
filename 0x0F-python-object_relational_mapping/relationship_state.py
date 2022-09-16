#!/usr/bin/python3
""" State class model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

""" State class
"""


class State(Base):
    """ State class inherits Base sqlalchemy call
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state")
