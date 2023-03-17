#!/usr/bin/python3
"""
deletes all State objects from the database that contain 'a'
using SQLAlchemy and importing State and Base from model_state
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).filter(State.name.like('%a%')).all():
    session.delete(state)     
    
session.commit()