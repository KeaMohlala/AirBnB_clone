#!/usr/bin/python3
"""
tests for Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    unit tests for Place class
    """
    def setUp(self):
        """
        set up place insstance
        """
        self.place = Place()

    def test_subclasss(self):
        """
        verifies that Place is a subclass of BaseModel
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_default_values(self):
        """
        test default values of the attributes
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, "")

    def test_instance_of_class(self):
        """
        verifies that place is an instance of the class
        """
        self.assertIsInstance(self.place, Place)
