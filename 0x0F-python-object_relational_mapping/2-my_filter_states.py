#!/usr/bin/python3
""" Lists all states from database hbtn_0e_0_usa by name """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # argv[1] = username, [2] = password, [3] = database, [4] = name
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    # host="localhost"(default), port=3306(default)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                .format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][:] == argv[4]:
            print(row)
    cur.close()
    db.close()
