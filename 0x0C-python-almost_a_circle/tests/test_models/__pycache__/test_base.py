#!/usr/bin/python3
"""Unittest base.
Test cases for Base class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_17_0' for the first test of task 17)
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """Create new instances: check for id."""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(927)
        self.assertEqual(b4.id, 927)
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def test_1_1(self):
        """Test for type and instance."""

        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))

    def test_15_0(self):
        """Test static method to_json_string with regular dict."""

        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
            json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

    def test_15_1(self):
        """Test static method to_json_string with wrong types."""

        with self.assertRaises(TypeError) as x:
