#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        s1 = State()
        s3 = State("hello", "wait", "in")

        k = f"{type(s1).__name__}.{s1.id}"
        self.assertIsInstance(s1.name, str)
        self.assertEqual(s3.name, "")
        s1.name = "Chicago"
        self.assertEqual(s1.name, "Chicago")
        self.assertIn(k, storage.all())

    def test_init(self):
        """Test method for public instances"""
        s1 = State()
        s2 = State(**s1.to_dict())
        self.assertIsInstance(s1.id, str)
        self.assertIsInstance(s1.created_at, datetime)
        self.assertIsInstance(s1.updated_at, datetime)
        self.assertEqual(s1.updated_at, s2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        s1 = State()
        string = f"[{type(s1).__name__}] ({s1.id}) {s1.__dict__}"
        self.assertEqual(s1.__str__(), string)


