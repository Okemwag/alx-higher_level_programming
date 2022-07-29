#!/usr/bin/python3
"""
This module uses the MySQLdb module to execute SQL commands.
(Best way to access database in python)
It does operations on cities Table
"""
import sys
import MySQLdb as sql


def select_cities():
    """This method Uses mySQL queries to select cities"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    connection = sql.connect(host=host, user=user,
                             passwd=passwd, db=sys.argv[3], port=port)
    cur = connection.cursor()
    sql_cmd1 = 'SELECT cities.id, cities.name, states.name FROM cities LEFT '
    sql_cmd2 = 'JOIN states ON cities.state_id = states.id ORDER BY cities.id;'
    cur.execute(sql_cmd1 + sql_cmd2)
    result = cur.fetchall()

    if result:
        for states in result:
            print(states)
    cur.close()
    connection.close()


if __name__ == '__main__':
    select_cities()
