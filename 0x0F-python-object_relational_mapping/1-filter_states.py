#!/usr/bin/python3
"""List all states with a name starting with upper N."""

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    """Connect to a MySQL server."""

    cursor = db.cursor()

    upper = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(upper)
    lists = cursor.fetchall()
    for rows in lists:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
