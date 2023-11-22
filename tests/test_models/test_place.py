#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from tests.test_models.test_base_model import TestBase_init


class test_Place(TestBase_init):
    """a class to test the place model"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def setUp(self):
        ''' Set up '''
        self.place = Place()
        self.city = City()
        self.user = User()
        self.amenity = Amenity()

    def tearDown(self):
        ''' Tear down '''
        del self.place
        del self.user

    def test_place_creation(self):
        ''' Tests if Place is created and all elements are initialised
            properly '''

        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.city_id, None)
        self.assertEqual(self.place.user_id, None)
        self.assertEqual(self.place.name, None)
        self.assertEqual(self.place.description, None)
        self.assertEqual(self.place.number_rooms, None)
        self.assertEqual(self.place.number_bathrooms, None)
        self.assertEqual(self.place.max_guest, None)
        self.assertEqual(self.place.price_by_night, None)
        self.assertEqual(self.place.latitude, None)
        self.assertEqual(self.place.longitude, None)

    def test_place_assignment(self):
        ''' Tests if things are assigned properly '''

        self.place.city_id = self.city.id
        self.place.user_id = self.user.id
        self.place.name = "Ethiopia"
        self.place.description = "The best place on Earth"
        self.place.number_rooms = 10
        self.place.number_bathrooms = 4
        self.place.max_guest = 3
        self.place.price_by_night = 50
        self.place.latitude = 34.0
        self.place.longitude = 33.7
        self.place.amenity_ids.append(self.amenity.id)

        self.assertEqual(self.place.city_id, self.city.id)
        self.assertEqual(self.place.user_id, self.user.id)
        self.assertEqual(self.place.name, "Ethiopia")
        self.assertEqual(self.place.description, "The best place on Earth")
        self.assertEqual(self.place.number_rooms, 10)
        self.assertEqual(self.place.number_bathrooms, 4)
        self.assertEqual(self.place.max_guest, 3)
        self.assertEqual(self.place.price_by_night, 50)
        self.assertEqual(self.place.latitude, 34.0)
        self.assertEqual(self.place.longitude, 33.7)
        self.assertEqual(self.place.amenity_ids, [self.amenity.id])

    def test_city_id(self):
        """ """
        new = self.value()
        if new.city_id is not None:
            self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if new.user_id is not None:
            self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if new.name is not None:
            self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        if new.description is not None:
            self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        if new.number_rooms is not None:
            self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        if new.number_bathrooms is not None:
            self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        if new.max_guest is not None:
            self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        if new.price_by_night is not None:
            self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        if new.latitude is not None:
            self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        if new.amenity_ids is not None:
            self.assertEqual(type(new.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
