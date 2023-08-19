#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name
                  FROM cities
                  INNER JOIN states
                  ON cities.state_id = states.id
                  WHERE states.name = %s
                  ORDER BY cities.id ASC""", (state,))

    rows = cur.fetchall()

    for row in rows:
        print(row[1])

    db.close()
