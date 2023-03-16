#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user='root',
        passwd='root',
        db='hbtn_0e_0_usa')

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    records = cur.fetchall()
    for i in records:
        print(i)
