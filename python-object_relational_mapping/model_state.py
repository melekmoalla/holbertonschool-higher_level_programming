#!/usr/bin/python3
"""
defines State class that inherits from Base = declarative_base()
and links to MySQL table states using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class state(Base):
    import sys
    """
    Write a script that deletes all State objects with a
    name containing the letter a from the database hbtn_0e_6_usa
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

Base.metadata.create_all(engine)
