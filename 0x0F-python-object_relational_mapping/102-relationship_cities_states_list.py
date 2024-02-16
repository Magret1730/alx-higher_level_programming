#!/usr/bin/python3
"""
A script that lists all City from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cityState = session.query(City).order_by(City.id).all()
    for city in cityState:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    session.close()
