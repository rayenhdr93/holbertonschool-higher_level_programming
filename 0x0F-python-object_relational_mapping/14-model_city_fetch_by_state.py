#!/usr/bin/python3
'''Des'''


from sys import argv
import sqlalchemy
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    q = session.query(City, State).join(State).order_by(State.id).all()
    for city, state in q:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
