#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from tests.test_models.test_base_model import TestBase_init


class TestCity(unittest.TestCase):
    ''' Tests the class City '''

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def setUp(self):
        ''' Set up '''
        self.city = City()
        self.state = State()

    def tearDown(self):
        ''' Tear down '''
        del self.city
        del self.state

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_city_creation(self):
        ''' Tests if city is created and all elements are initialised properly
        '''

        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_assignment(self):
        ''' Tests if things are assigned properly '''

        self.city.state_id = self.state.id
        self.city.name = "Zootopia"

        self.assertEqual(self.city.state_id, self.state.id)
        self.assertEqual(self.city.name, "Zootopia")


if __name__ == "__main__":
    unittest.main()
