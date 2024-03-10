#!/usr/bin/python3
"""
Test cases for BaseModel class
"""

import datetime
import unittest
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests for base class
    """

    def setUp(self):
        """
        initialize objects from BaseModel
        """
        self.model_1 = BaseModel()
        self.model_2 = BaseModel()

    def test_instance_inheritence(self):
        """
        tests to ensure classes inherit from base class
        """
        obj = storage.all()

        for objects in obj.values():
            self.assertTrue(isinstance(objects, BaseModel))
            if objects.__class__.__name__ != "BaseModel":
                self.assertTrue(issubclass(objects.__class__, BaseMode))

    def test_attribute_type(self):
        """
        tests the data type of the base class attributes
        """
        self.assertEqual(type(self.model_1.created_at), datetime.datetime)
        self.assertEqual(type(self.model_1.updated_at), datetime.datetime)

    def test_same_created_at_updated_at(self):
        """"
        tests that created_at and updated_at attributes are the same
        """
        self.assertEqual(self.model_1.created_at, self.model_1.updated_at)

    def test_strmethod(self):
        """
        tests the printed output of the str method
        """
        self.assertEqual(
                str(self.model_1),
                f"[BaseModel] ({self.model_1.id}) {self.model_1.__dict__}",
        )

    def test_id(self):
        """
        test to see if a unique id is created
        """
        self.assertNotEqual(self.model_1.id, self.model_2.id)

    def test_new_attributes(self):
        """
        tests if you are able to add new atttributes to the object
        """
        self.model_1.name = "My First Model"
        self.model_1.my_number = 89

        self.assertEqual(self.model_1.name, "My First Model")
        self.assertEqual(self.model_1.my_number, 89)

    def test_updated_at_changes(self):
        """
        tests whether updated_at changes
        """
        old_updated_at = self.model_1.updated_at
        prev_updated_at = self.model_2.updated_at
        self.model_1.my_number = 91
        self.model_2.save()

        self.assertEqual(old_updated_at, self.model_1.updated_at)
        self.assertNotEqual(self.model_2.updated_at, prev_updated_at)

    def test_iso_format_after_to_dict(self):
        """
        ensure 'created_at' and 'updated_at' are in ISO format
        """
        expected_output_1 = self.model_2.updated_at.isoformat()
        expected_output_2 = self.model_2.created_at.isoformat()

        model_dict = self.model_2.to_dict()
        self.assertEqual(model_dict["updated_at"], expected_output_1)
        self.assertEqual(model_dict["created_at"], expected_output_2)


class TestRecreateInstanceusingDictionary(unittest.TestCase):
    """
    Tests to re-create an instance using a dictionary representation
    """
    def setUp(self):
        """
        set up base class instances
        """
        self.model_3 = BaseModel()
        self.model_4 = BaseModel()

    def test_same(self):
        """
        tests if the uuid and createion times are the same
        """
        new_model1 = BaseModel(**self.model_3.to_dict())
        new_model2 = BaseModel(**self.model_4.to_dict())

        self.assertEqual(new_model1.id, self.model_3.id)
        self.assertEqual(new_model2.created_at, self.model_4.created_at)

    def test_type(self):
        """
        tests the type of the updated_at and created_at types
        """
        new_model1 = BaseModel(**self.model_3.to_dict())
        new_model2 = BaseModel(**self.model_4.to_dict())

        self.assertEqual(type(new_model1.updated_at), datetime.datetime)
        self.assertEqual(type(new_model2.created_at), datetime.datetime)

    def return_type(self):
        """
        return type should be a dictionary
        """
        self.assertEqual(type(self.model_3.to_dict()), dict)

    def test_instantiation_from_dict(self):
        """
        recreate model from dict
        """
        new_model1 = BaseModel(**self.model_3.to_dict())

        self.assertEqual(type(new_model1).__name__, BaseModel.__name__)

    def test_ISOformat(self):
        """
        tests the dates in the dictionary are strings
        """
        self.assertIsInstance(self.model_3.to_dict()["updated_at"], str)
        self.assertIsInstance(self.model_3.to_dict()["created_at"], str)
