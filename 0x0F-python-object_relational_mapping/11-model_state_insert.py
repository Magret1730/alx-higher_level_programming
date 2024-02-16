#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
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

    addObject = State(name="Louisiana")
    session.add(addObject)

    session.commit()

    print(addObject.id)

    """
    state_to_remove = session.query(State)
        .filter(State.name == "Louisiana").first()

    if state_to_remove:
        # Remove the State object from the session
        session.delete(state_to_remove)

        # Commit the changes to the database
        session.commit()
        print("State 'Louisiana' removed successfully.")
    else:
        print("State 'Louisiana' not found.")
    """

    session.close()
