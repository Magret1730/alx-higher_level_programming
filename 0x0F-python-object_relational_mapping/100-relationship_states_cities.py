#!/usr/bin/python3
"""
script that creates the State 'California' with the City
'San Francisco' from the database hbtn_0e_100_usa
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

    # california = State(name='California')
    # san_francisco = City(name='San Francisco', state=california)

    # session.add(california)
    # session.add(san_francisco)

    session.add(City(name="San Francisco", state=State(name="California")))

    session.commit()

    session.close()
