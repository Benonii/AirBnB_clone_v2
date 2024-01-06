#!/usr/bin/python3
""" Place Module for HBNB project """
import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60, collation='latin1_swedish_ci'),
                     ForeignKey(City.id))
    user_id = Column(String(60), ForeignKey(User.id))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if storage_type == 'db':
        reviews = relationship('Review', backref='places', cascade='delete')
    else:
        def get_reviews(self, place_id):
            ''' Gets all reviews in which the place id is equal to the
                current Place.id '''

            reviews = [review for review in self.all(Review)
                       if review.place_id == Place.id]
            return reviews
