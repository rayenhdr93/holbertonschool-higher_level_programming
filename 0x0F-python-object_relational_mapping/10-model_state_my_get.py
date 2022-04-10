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
    i = 0
    for state in session.query(State).order_by(State.id).all():
        if (argv[4] == state.name):
            print(state.id)
            i = 1
    if (i == 0):
        print('Not found')
    session.close()
