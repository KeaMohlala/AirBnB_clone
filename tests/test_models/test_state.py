#!/usr/bin/python3
"""
tests for State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    unit tests State class
    """
    def setUp(self):
        """
        set up state insstance
        """
        self.state = State()

    def test_subclasss(self):
        """
        verifies that State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_default_values(self):
        """
        test default values of the attributes
        """
        self.assertEqual(self.state.name, "")

    def test_instance_of_class(self):
        """
        verifies that state is an instance of the class
        """
        self.assertIsInstance(self.state, State)
