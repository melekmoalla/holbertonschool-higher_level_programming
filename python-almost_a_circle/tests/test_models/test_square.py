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
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            s5 = Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

        s6 = Square(1, 2, 3, 4)
        self.assertEqual(s6.id, 4)

        with self.assertRaises(ValueError) as e:
            s7 = Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            s8 = Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            s9 = Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as e:
            s10 = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(TypeError) as e:
            s11 = Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_square_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 18, 'x': 2, 'size': 10, 'y': 1})

    def test_square_update(self):
        s20 = Square(10, 10, 2, 5)
        s20.update()
        self.assertEqual(s20, s20)

        s21 = Square(10, 10, 2, 5)
        s21.update(98)
        self.assertEqual(s21, s21)

        s22 = Square(10, 10, 2, 5)
        s22.update(89, 1)
        self.assertEqual(s22, s22)

        s23 = Square(10, 10, 2, 5)
        s23.update(89, 1, 2)
        self.assertEqual(s23, s23)

        s24 = Square(10, 10, 2, 5)
        s24.update(89, 1, 2, 3)
        self.assertEqual(s24, s24)

        s25 = Square(10, 10, 2, 5)
        s25.update(**{'id': 89})
        self.assertEqual(s25, s25)

        s26 = Square(10, 10, 2, 5)
        s26.update(**{'id': 89, 'size': 1})
        self.assertEqual(s26, s26)

        s26 = Square(10, 10, 2, 5)
        s26.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s26, s26)

        s27 = Square(10, 10, 2, 5)
        s27.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s27, s27)
    
    
