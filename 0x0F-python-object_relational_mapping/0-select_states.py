#!/usr/bin/python3
"""List all states from the database.
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database

"""


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
    """Used to instantiate a MySQL cursor object."""

    sort = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sort)
    """Executes the given database operation (query or command)."""

    lists = cursor.fetchall()
    """Fetches all rows of a query result set and returns a list."""
    for row in lists:
        print(row)

    cursor.close()
    """
    Closes the cursor, resets all results, and ensures that the cursor object
    has no reference to its original connection object.
    """
    db.close()
