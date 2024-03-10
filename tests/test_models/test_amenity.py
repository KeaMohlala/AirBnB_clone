#!/usr/bin/python3
"""
Test suits for amenities
"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class.
    """

    def test_instance(self):
        """
        Test if instance is created successfully.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """
        Test if the attributes of Amenity class are correct.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """
        Test the __str__ method of Amenity class.
        """
        amenity = Amenity()
        self.assertEqual(str(amenity), "")

    def test_to_dict(self):
        """
        Test the to_dict method of Amenity class.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['name'], "")
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
