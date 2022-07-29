#!/usr/bin/python3
"""
This module uses the MySQLdb module to execute SQL commands.
(Best way to access database in python)
It does operations on @cities and @states Table
"""
import sys
import MySQLdb as sql


def filter_cities():
    """This method Uses mySQL queries to filter cities"""
    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    connection = sql.connect(host=host, user=username,
                             passwd=passwd, db=database, port=port)
    cur = connection.cursor()
    sql_cmd1 = 'SELECT cities.name FROM cities INNER '
    sql_cmd2 = 'JOIN states ON states.id = cities.state_id '
    sql_cmd3 = 'WHERE states.name = %s ORDER BY cities.id;'
    cur.execute(sql_cmd1 + sql_cmd2 + sql_cmd3, [sys.argv[4]])
    result = cur.fetchall()

    print(', '.join(map(lambda x: x[0], result)))
    cur.close()
    connection.close()


if __name__ == '__main__':
    filter_cities()
