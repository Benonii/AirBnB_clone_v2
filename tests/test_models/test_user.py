#!/usr/bin/python3
""" """

import unittest
from models.base_model import BaseModel
from models.user import User
from tests.test_models.test_base_model import TestBase_init


class test_User(TestBase_init):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
    
    def setUp(self):
        ''' Set up '''
        self.user = User()

    def tearDown(self):
        ''' Tear down '''
        del self.user

    def test_user_creation(self):
        ''' Tests if user is created and all elements are empty strings '''
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.first_name, None)
        self.assertEqual(self.user.last_name, None)
        self.assertEqual(self.user.email, None)
        self.assertEqual(self.user.password, None)

    def test_user_assignment(self):
        ''' Tests if things are assigned correctly '''

        self.user.first_name = "Benoni"
        self.user.last_name = "Esckinder"
        self.user.email = "Benoni123@email.com"
        self.user.password = "########"

        self.assertEqual(self.user.first_name, "Benoni")
        self.assertEqual(self.user.last_name, "Esckinder")
        self.assertEqual(self.user.email, "Benoni123@email.com")
        self.assertEqual(self.user.password, "########")

    def test_first_name(self):
        """ """
        new = self.value()
        if new.first_name is not None:
            self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        if new.last_name is not None:
            self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        if new.email is not None:
            self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        if new.password is not None:
            self.assertEqual(type(new.password), str)

if __name__ == "__main__":
    unittest.main()
