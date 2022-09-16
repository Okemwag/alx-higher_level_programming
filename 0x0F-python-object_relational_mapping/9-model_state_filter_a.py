#!/usr/bin/python3
"""Lists all State objects from database hbtn_0e_6_usa containing "a"
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Engine connection
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """ Session handling
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query
    """

    for state in session.query(State)\
                        .order_by(State.id)\
                        .filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

        session.close()
