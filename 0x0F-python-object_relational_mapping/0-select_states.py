#!/usr/bin/python3
""" Lists all states from databse hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # argv[1] = username, [2] = password, [3] = database
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    # host="localhost"(default), port=3306(default)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
