#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128, collation='latin1_swedish_ci'), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'fs':
        @property
        def cities(self):
            ''' Gets all cities associated with the current state '''
            storage = FileStorage()
            city_list = list()
            storage.reload()
            all_cities = storage.all(City)

            for key, obj in all_cities.items():
                if obj.state_id == self.id:
                    city_list.append(obj)
            return city_list

    else:
        cities = relationship("City", backref="states", cascade="delete")
