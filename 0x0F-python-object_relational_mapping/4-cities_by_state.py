#!/usr/bin/python3

"""
 script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb as db

if __name__ == "__main__":
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states \
                        ON cities.state_id = states.id \
                        ORDER BY cities.id ASC")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
