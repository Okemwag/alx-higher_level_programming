#!/usr/bin/python3
""" Lists all states from databse hbtn_0e_0_usa with name """

if __name__ == "__main__":
    import MySQLdb as sdb
    from sys import argv
    # argv[1] = username, [2] = password, [3] = database, [4] = name
    db = sdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    # host="localhost"(default), port=3306(default)
    cur = db.cursor()
    if "'" not in argv[4]:
        cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                    .format(argv[4]))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    cur.close()
    db.close()
