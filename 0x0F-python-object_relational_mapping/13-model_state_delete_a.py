#!/usr/bin/python3
"""Deletes State objects containing "a" in name from hbtn_0e_6_usa database
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

    """ Deletes fields
    """
    session.query(State).filter(State.name.like('%a%'))\
                        .delete(synchronize_session=False)
    session.commit()
    session.close()
