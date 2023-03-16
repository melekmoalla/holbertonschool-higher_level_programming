#!/usr/bin/python3
"""
list list 
"""
# mmmm
from model_state import Base, State
from sqlalchemy import create_engine

import MySQLdb
import sys
"""
list list 
"""
if __name__ == "__main__":
    """
    list list 
    """
    username, password, database = sys.argv[1:]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Base.metadata.create_all(engine)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    result = cur.fetchall()
    for row in result:
        print(row[0], end="")
        print(": ", end="")
        print(row[1])
