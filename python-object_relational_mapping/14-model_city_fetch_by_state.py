#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instante in session.query(City).order_by(City.id):
        for state in session.query(State):
            if (instante.state_id == state.id):
                print(f"{state.name}: ({instante.id}) instante.name}")
