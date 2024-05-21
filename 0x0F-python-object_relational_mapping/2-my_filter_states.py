#!/usr/bin/python3
"""Lists all states from the database Start with N."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Get the statesfrom the database."""
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                states.id ASC".format(argv[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
