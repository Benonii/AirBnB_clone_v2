#!/usr/bin/python3
""" Review module for the HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.place import Place
from models.user import User


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey(Place.id))
    user_id = Column(String(60), ForeignKey(User.id))
    text = Column(String(1024), nullable=False)
