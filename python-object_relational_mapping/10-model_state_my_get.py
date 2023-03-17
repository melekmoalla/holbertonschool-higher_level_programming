#!/usr/bin/python3
"""
Write a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""
import sqlalchemy
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    result = cur.fetchall()
    b = 0
    for row in result:
        if (name == row[1]):
            print(row[0])
            b = 1
    if b == 0:
        print("Not found")
