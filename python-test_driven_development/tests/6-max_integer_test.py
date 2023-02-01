#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
    
    def test_mixed_integers(self):
        self.assertEqual(max_integer([]), 0)

if __name__ == '__main__':
    unittest.main()
