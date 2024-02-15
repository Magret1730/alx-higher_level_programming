#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
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

    firstState = session.query(State).order_by(State.id).first()
    if firstState:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")

    session.close()
