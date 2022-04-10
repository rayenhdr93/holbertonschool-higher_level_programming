#!/usr/bin/python3
'''Des'''


from sys import argv
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first = session.query(State).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
