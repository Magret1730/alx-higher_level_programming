#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_remove = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # for states in states_to_remove:
    # print("{}: {}".format(states.id, states.name))

    if states_to_remove:
        for states in states_to_remove:
            session.delete(states)

    session.commit()

    session.close()
