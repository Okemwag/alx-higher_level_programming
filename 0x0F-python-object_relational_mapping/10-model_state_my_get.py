#!/usr/bin/python3
"""Prints State object id with name passed in as arg
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

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
    if "'" not in sys.argv[4]:
        check = session.query(State).filter_by(name=sys.argv[4]).scalar()
        if check is None:
            print("Not found")
        else:
            query = session.query(State).filter_by(name=sys.argv[4])
            for row in query.all():
                print("{}".format(row.id))

    session.close()
