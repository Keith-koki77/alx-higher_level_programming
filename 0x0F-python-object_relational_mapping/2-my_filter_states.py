#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def main():
    """
    displays all values in thr states table of the database
    where name matches
    """
    if len(sys.argv) != 5:
        return

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.exec
