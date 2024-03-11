#!/usr/bin/python3
"""
Test suits for amenities
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class.
    """
    def setUp(self):
        """
        sets up Amenity instance
        """
        self.amenity = Amenity()

    def test_subclass(self):
        """
        Tests if Amenity is a subclass of BaseModel
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_default_values(self):
        """
        test default values of the attributes
        """
        self.assertEqual(self.amenity.name, "")

    def test_instance_of_class(self):
        """
        verifies that menity is an instance of Amenities
        """
        self.assertIsInstance(self.amenity, Amenity)
