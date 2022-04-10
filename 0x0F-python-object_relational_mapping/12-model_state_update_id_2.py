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
    obj = session.query(State).get(2)
    obj.name = 'New Mexico'
    session.commit()
    session.close()
