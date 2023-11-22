#!/usr/bin/python3
""" """

import unittest
from models.base_model import BaseModel
from models.state import State
from tests.test_models.test_base_model import TestBase_init


class test_state(TestBase_init):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def setUp(self):
        ''' Set up '''
        self.state = State()

    def tearDown(self):
        ''' Tear down '''
        del self.state

    def test_state_creation(self):
        ''' Tests if state is created and all elements are initialised properly
        '''

        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, None)

    def test_state_assignment(self):
        ''' Tests if name is assigned correctly '''

        self.state.name = "Dakota"

        self.assertEqual(self.state.name, "Dakota")

    def test_name3(self):
        """ """
        new = self.value()
        if new.name is not None:
            self.assertEqual(type(new.name), str)

if __name__ == "__main__":
    unittest.main()
