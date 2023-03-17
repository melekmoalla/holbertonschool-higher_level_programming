#!/usr/bin/python3
"""
 Write a script that deletes all State objects with a
 name containing the letter a from the database hbtn_0e_6_usa
"""
import MySQLdb
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
class state(Base):
    """
    Write a script that deletes all State objects with a
    name containing the letter a from the database hbtn_0e_6_usa
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Create the engine and connect to the MySQL server
engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

# Create the table if it does not exist
Base.metadata.create_all(engine)
