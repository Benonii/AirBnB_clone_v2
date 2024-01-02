#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        ''' Gets all cities associated with the current state '''
        cities = []
        for city_id, city_obj in FileStorage().all(City).items():
            if city_obj.state_id == self.id:
                city_list.append(city_obj)
        return cities
