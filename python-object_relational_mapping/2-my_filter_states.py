#!/usr/bin/python3
"""
Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    pas = sys.argv[2]
    data = sys.argv[3]
    name = sys.argv[4]

    connection = MySQLdb.connect(
        host='localhost', port=3306, database=data, user=user, password=pas)

    record = connection.cursor()
    record.execute("SELECT * FROM states ORDER BY states.id ASC")
    recordS = record.fetchall()
    for i in recordS:
        if (i[1] == name):
            print(format(i))
