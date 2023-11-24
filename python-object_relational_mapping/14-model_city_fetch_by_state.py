#!/usr/bin/python3
"""
Prints all cities objects from db
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    """sql server"""
    # argument vector vars
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    # database url
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db))
    # custom session object class from db engine
    Session = sessionmaker(bind=engine)
    # instance
    session = Session()
    # table query
    cities = session.query(State.name, City.id, City.name).join(
        City, City.state_id == State.id).order_by(City.id)
    # print state, city name & id
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
