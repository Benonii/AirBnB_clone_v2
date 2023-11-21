#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemny import String, Column, ForeignKey


class Amenity(BaseModel), Base:
    ''' Table for amenities '''

    __tablename__ = "amenities"
    name = Column(String(128), nullable=Flase)
