#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usA
"""

import MySQLdb

if __name__ == "__main__":
    import sys

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
