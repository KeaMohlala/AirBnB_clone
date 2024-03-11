#!/usr/bin/python3
"""
tests for User
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    unit tests for User class
    """
    def setUp(self):
        """
        set up user insstance
        """
        self.user = User()

    def test_subclasss(self):
        """
        verifies that User is a subclass of BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_default_values(self):
        """
        test default values of the attributes
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_instance_of_class(self):
        """
        verifies that user is an instance of the class
        """
        self.assertIsInstance(self.user, User)
