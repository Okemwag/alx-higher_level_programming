#!/usr/bin/python3
"""Adds State object "Louisiana" to hbtn_0e_6_usa database
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

    """ Adding user
    """
    new_state = State(name='Louisiana')
    session.add(new_state)
    query = session.query(State).filter_by(name='Louisiana')
    for row in query.all():
        print("{}".format(row.id))
    session.commit()
    session.close()
