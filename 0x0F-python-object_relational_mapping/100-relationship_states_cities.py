#!/usr/bin/python3
"""
City Relationship
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    nstate = "California"
    ncity = "San Francisco"

    newState = State(name=nstate)

    session.add(newState)

    newCity = City(name=ncity, state_id=newState.id)

    session.add(newCity)

    session.commit()

    session.close()
