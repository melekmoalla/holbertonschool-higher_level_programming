#!/usr/bin/python3
"""
 Write a script that deletes all State objects with a
 name containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    """
    Write a script that deletes all State objects with a
    name containing the letter a from the database hbtn_0e_6_usa
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


