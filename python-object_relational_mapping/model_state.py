#!/usr/bin/python3
"""
Class definition of a State that inherits from Base Ti[s]
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class for usage with SQLAlchemy inherited from declarative_base()
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)