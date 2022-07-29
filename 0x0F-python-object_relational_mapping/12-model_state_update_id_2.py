#!/usr/bin/python3
'''search through the states, if id == 2, rename'''

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local = Session()
    state = local.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    local.commit()

    local.close()
    engine.dispose()
