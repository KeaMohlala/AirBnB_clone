#!/usr/bin/python3
"""
tests city class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    unit tests for City class
    """
    def setUp(self):
        """
        set up city insstance
        """
        self.city = City()

    def test_subclasss(self):
        """
        verifies that City is a subclass of BaseModel
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_default_values(self):
        """
        test default values of the attributes
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_instance_of_class(self):
        """
        verifies that city is an instance of the class
        """
        self.assertIsInstance(self.city, City)
