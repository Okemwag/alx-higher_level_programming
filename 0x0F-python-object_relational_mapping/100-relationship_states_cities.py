#!/usr/bin/python3
"""Creating a state and
a city in the dtatabase
"""

from relationship_state import State, Base
from relationship_city import City
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
                           username, password, host, port, db_name
                           ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    obj_session = Session()

    first_state = State(name='California')
    first_city = City(name='San Francisco')
    first_state.cities.append(first_city)

    obj_session.add(first_state)
    obj_session.add(first_city)
    obj_session.commit()

    obj_session.close()
    engine.dispose()
