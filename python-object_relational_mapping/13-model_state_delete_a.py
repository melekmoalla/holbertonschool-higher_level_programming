#!/usr/bin/python3
"""Write a script that deletes all State objects
with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sqlalchemy
import MySQLdb
import sys
if __name__ == "__main__":
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
    for i in result:
        if ('a' in i[1]):
            m = i[0]
            cur.execute(f"DELETE FROM states  WHERE states.id = {m}")
            db.commit()
