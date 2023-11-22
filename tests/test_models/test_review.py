#!/usr/bin/python3
""" """

import unittest
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User
from tests.test_models.test_base_model import TestBase_init


class test_review(TestBase_init):
    """a class to test review class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def setUp(self):
        ''' Set up '''
        self.review = Review()
        self.place = Place()
        self.user = User()

    def tearDown(self):
        ''' Tear down '''
        del self.review
        del self.place
        del self.user

    def test_review_creation(self):
        ''' Tests if Review is created and all elements are initialised
            properly '''

        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_assignment(self):
        ''' Tests if everything is assigned properly '''

        self.review.place_id = self.place.id
        self.review.user_id = self.user.id
        self.review.text = "Great place"

        self.assertEqual(self.review.place_id, self.place.id)
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.text, "Great place")

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

if __name__ == "__main__":
    unittest.main()
