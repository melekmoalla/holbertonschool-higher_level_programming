#!/usr/bin/python3
"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys
if __name__ == "__main__":

    user = sys.argv[1]
    pas = sys.argv[2]
    data = sys.argv[3]

    connection = MySQLdb.connect(
        host='localhost', port=3306, database=data, user=user, password=pas)

    record = connection.cursor()
    record.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' AND name NOT LIKE 'n%' ORDER BY states.id ASC")

    records = record.fetchall()
    for i in records:
        print(i)
