#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(query.format(state_name))

    rows = cursor.fetchone()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
