#!/usr/bin/python3
"""
 script that takes in arguments and displays all values in the
 states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (state, ))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

db.close()
