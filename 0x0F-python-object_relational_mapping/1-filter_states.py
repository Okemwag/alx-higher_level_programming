#!/usr/bin/python3
""" Lists all states from database hbtn_0e_0_usa starting with N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # argv[1] = username, [2] = password, [3] = database
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    # host="localhost"(default), port=3306(default)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    db.close()

# if __name__ == "__main__":
#     # argv[1] = username, [2] = password, [3] = database
#     db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
#                          host="localhost", port=3306)
#     # host="localhost"(default), port=3306(default)
#     cur = db.cursor()
#     cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
#     query_rows = cur.fetchall()
#     for row in query_rows:
#         print('{}'.format(row))
#     cur.close()
#     db.close()
