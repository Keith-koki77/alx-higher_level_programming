#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usA
"""

import MySQLdb

if __name__ == "__main__":
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                            user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
