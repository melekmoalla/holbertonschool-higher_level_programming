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

        s4 = Square("1")
        self.assertEqual(s4.width, '1')

        s5 = Square(1, "2")
        self.assertEqual(s5.x, '2')

        s6 = Square(1, 2, 3, 4)
        self.assertEqual(s6.id, 4)

        s7 = Square(-1)
        self.assertEqual(s7.height, -1)

        s8 = Square(1, -2)
        self.assertEqual(s8.x, -2)

        s9 = Square(1, 2, -3)
        self.assertEqual(s9.y, -3)

        s10 = Square(0)
        self.assertEqual(s10.width, 0)

        
