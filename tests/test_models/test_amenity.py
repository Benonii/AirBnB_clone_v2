#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBase_init


class test_Amenity(TestBase_init):
    """a class to test Amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def setUp(self):
        ''' Set up '''
        self.amenity = Amenity()

    def tearDown(self):
        ''' Tear down '''
        del self.amenity

    def test_amenity_creation(self):
        ''' Tests if Amenity is created and all elements are initialised
            properly '''

        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "")

    def test_amenity_assignment(self):
        ''' Tests if things are assigned properly '''

        self.amenity.name = "Couch"

        self.assertEqual(self.amenity.name, "Couch")

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == "__main__":
    unittest.main()
