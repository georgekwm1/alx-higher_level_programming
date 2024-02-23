#!/usr/bin/python3
import unittest
add_integer = __import__('0-add_integer').add_integer

class TestAddInteger(unittest.TestCase):
    def test_add_integer(self):
        self.assertEqual(add_integer(1,2), 3)
        self.assertEqual(add_integer(100, -2), 98)
        self.assertEqual(add_integer(2), 100)
        self.assertEqual(add_integer(100.3, -2), 98)
        self.assertEqual(add_integer(4, "School"), "b must be an integer")
    