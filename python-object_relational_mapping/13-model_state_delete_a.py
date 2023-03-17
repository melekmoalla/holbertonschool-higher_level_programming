#!/usr/bin/python3
"""
deletes all State objects from the database that contain 'a'
using SQLAlchemy and importing State and Base from model_state
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            session.delete(state)

    session.commit()
