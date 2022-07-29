#!/usr/bin/python3
"""this module looks for a state that contains 'a' in its name"""
from model_state import State, Base
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
                           username, password, host, port, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_in_states = session.query(State).filter(
               State.name.op('regexp')('.*a+.*')
               ).order_by(State.id)
    session.close()
    engine.dispose()

    if a_in_states:
        for state in a_in_states:
            print('{}: {}'.format(state.id, state.name))
