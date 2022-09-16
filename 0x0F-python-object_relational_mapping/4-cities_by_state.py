#!/usr/bin/python3
""" Lists all cities from databse hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb as sdb
    from sys import argv
    # argv[1] = username, [2] = password, [3] = database, [4] = name
    db = sdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    # host="localhost"(default), port=3306(default)
    cur = db.cursor()
    cur.execute("\
    SELECT c.id, c.name, s.name FROM cities AS c\
    JOIN states AS s\
    ON s.id = c.state_id\
    ORDER BY c.id ASC\
    ")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
