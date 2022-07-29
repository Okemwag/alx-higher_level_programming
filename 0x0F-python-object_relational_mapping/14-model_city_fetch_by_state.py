#!/usr/bin/python3
"""This module gets city by state"""

from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, database
                           ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local = Session()
    result = local.query(City, State).filter(
                           City.state_id == State.id
                           ).order_by(City.id).all()

    for row in result:
        print('{}: ({}) {}'.format(row[1].name, row[0].id, row[0].name))

    local.close()
    engine.dispose()
