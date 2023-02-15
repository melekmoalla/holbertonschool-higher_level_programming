#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_new_Rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 2)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

        r5 = Rectangle("1", 2)
        self.assertEqual(r5.id, 3)

        r6 = Rectangle(1, "2")
        self.assertEqual(r6.id, 4)

        r7 = Rectangle(1, 2, "3")
        self.assertEqual(r7.x, '3')

        r8 = Rectangle(1, 2, 3, "4")
        self.assertEqual(r8.y, '4')

        r9 = Rectangle(-1, 2)
        self.assertEqual(r9.width, -1)
