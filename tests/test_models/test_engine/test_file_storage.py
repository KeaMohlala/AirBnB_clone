#!/usr/bin/python3
"""
test cases for FileStorage class
"""

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    tests for FileStorage Class
    """
    def test_init(self):
        """
        tests initiliazation of instance
        """
        self.assertIsInstance(storage, FileStorage)

    def test_new(self):
        """
        verifies that the new method correctly adds
        an object to the storage
        """
        user = User()
        storage.new(user)
        self.assertIn(
                f"{user.__class__.__name__}.{user.id}",
                storage.all()
        )

    def test_save(self):
        """
        ensures the save method correctly serializes
        objects to a JSON file
        """
        user = User()
        storage.new(user)
        storage.save()
        json_file_path = "file.json"
        with open(
                json_file_path,
                'r',
                encoding='utf-8'
        ) as f:
            data = json.load(f)
        self.assertIn(f"{user.__class__.__name__}.{user.id}", data)

    def test_reload(self):
        """
        confirms that the reload method correctly deserializes
        objects from a JSON file
        """
        user = User()
        storage.new(user)
        storage.save()
        storage.reload()
        self.assertIn(
                f"{user.__class__.__name__}.{user.id}",
                storage.all()
        )
