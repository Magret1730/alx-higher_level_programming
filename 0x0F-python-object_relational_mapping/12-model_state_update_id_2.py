#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    updateState = session.query(State)\
        .filter(State.id == 2)\
        .first()

    if updateState:
        updateState.name = "New Mexico"

    session.commit()
    # print("{}: {}".format(updateState.id, updateState.name))

    session.close()
