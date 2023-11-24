#!/usr/bin/python3
"""
Class definition of a City that inherits from Base
"""
from sqlalchemy import Integer, String, Column
from model_state import Base


class City(Base):
    """
    City class for usage with SQLAlchemy inherited from declarative_base() in State class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)