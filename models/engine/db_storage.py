#!/usr/bin/python3

''' Handles the database storage of HBnB '''

import os
import sys
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    ''' db storage class '''

    __engine = None
    __session = None

    def __init__(self):
        ''' Instantization '''
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        storage_type = os.environ.get('HBNB_TYPE_STORAGE')
        env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.dro_all(self.__engine)

    def all(self, cls=None):
        ''' Query on the current database session all objects dependant on
            the class cls '''
        objcts = dict()

        if cls is None:
            results = (
                self.__session.query(User).all() +
                self.__session.query(State).all() +
                self.__session.query(City).all() +
                self.__session.query(Amenity).all() +
                self.__session.query(Place).all() +
                self.__session.query(Review).all()
            )

            for row in results:
                key = f"{row.__class__.__name__}.{row.id}"
                objcts[key] = row

        else:
            if type(cls) is str:
                cls = eval(cls)

            result = self.__session.query(cls)

        for row in result:
            key = "{}.{}".format(type(row).__name__, row.id)
            objcts[key] = row

        return objcts

    def new(self, obj):
        ''' Adds a new object to the session '''
        self.__session.add(obj)

    def save(self):
        ''' Saves the object to the session '''
        self.__session.commit()

    def delete(self, obj):
        ''' deletes object from the current database option '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' Creats all tables in the database and the current db session '''
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.remove()
