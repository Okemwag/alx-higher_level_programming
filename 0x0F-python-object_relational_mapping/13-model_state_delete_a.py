#!/usr/bin/python3
'''This deletes a state'''

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
    local_session = Session()
    states = local_session.query(State).filter(
                           State.name.op('regexp')('.*a+.*')
                           )

    for state in states:
        local_session.delete(state)
    local_session.commit()

    local_session.close()
    engine.dispose()
