#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
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

    states = session.query(State).order_by(State.id).all()
    """
    for row in states:
        print(row.__dict__)
    """
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
