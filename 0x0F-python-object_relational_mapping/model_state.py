#!/usr/bin/python3
'''Des'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Des'''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
