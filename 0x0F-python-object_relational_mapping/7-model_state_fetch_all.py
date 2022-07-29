#!/usr/bin/python3
"""
This module uses sqlalchemy to print table
"""
import sys
import MySQLdb as sql
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def sqlalchemies():
    """This method connects to a database using sqlalchemy"""
    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        username, passwd, host, port, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    new_session = Session()
    states = new_session.query(State).order_by(State.id).all()
    new_session.close()
    engine.dispose()

    for state in states:
        print(str(state.id) + ": " + state.name)


if __name__ == '__main__':
    sqlalchemies()
