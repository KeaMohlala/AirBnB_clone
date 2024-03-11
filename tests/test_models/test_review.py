#!/usr/bin/python3
"""
tests for Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    unit tests Review class
    """
    def setUp(self):
        """
        set up review insstance
        """
        self.review = Review()

    def test_subclasss(self):
        """
        verifies that Review is a subclass of BaseModel
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_default_values(self):
        """
        test default values of the attributes
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_instance_of_class(self):
        """
        verifies that review is an instance of the class
        """
        self.assertIsInstance(self.review, Review)
