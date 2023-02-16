#!/usr/bin/python3

import unittest
from models.square import Square


class Testsquare(unittest.TestCase):

    def test_square(self):
        s1 = Square(1)
        self.assertEqual(s1.width, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)

        with self.assertRaises(TypeError) as e:
            s4 = Square("1")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            s5 = Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

        s6 = Square(1, 2, 3, 4)
        self.assertEqual(s6.id, 4)

        with self.assertRaises(ValueError) as e:
            s7 = Square(-1)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            s8 = Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            s9 = Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as e:
            s10 = Square(0)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(TypeError) as e:
            s11 = Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")
