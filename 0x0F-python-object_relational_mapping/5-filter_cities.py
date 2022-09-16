#!/usr/bin/python3
""" Lists all cities from databse hbtn_0e_0_usa by state """

if __name__ == "__main__":
    import MySQLdb as sdb
    from sys import argv
    # argv[1] = username, [2] = password, [3] = database, [4] = state name
    db = sdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    # host="localhost"(default), port=3306(default)
    cur = db.cursor()
    if "'" not in argv[4]:
        cur.execute("\
    SELECT c.name FROM cities AS c\
    JOIN states AS s\
    ON s.id = c.state_id\
    WHERE s.name='{}'\
    ORDER BY c.id ASC\
    ".format(argv[4]))
        query_rows = cur.fetchall()
        print(", ".join(row[0] for row in query_rows))
        # str2 = ""
        # for row in query_rows:
        #     str = ''.join(row)
        #     str2 += str + ', '
        #     str3 = str2.rstrip(', ')
        # print(str3)
    cur.close()
    db.close()
