#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
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
    record2 = connection.cursor()
    record.execute("SELECT * FROM cities JOIN states ORDER BY cities.id ASC")

    records = record.fetchall()
    m = []
    for i in records:
        if (i[4] == name and i[1] == i[3]):
            m.append(i[2])
    if (m == []):
        print()
    for a in m:
        if (a != m[-1]):
            print(a, end=", ")
        else:
            print(a)
