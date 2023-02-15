#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_new_Rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 4)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

        r5 = Rectangle("1", 2)
        self.assertEqual(r5.id, 5)

        r6 = Rectangle(1, "2")
        self.assertEqual(r6.height, '2')

        r7 = Rectangle(1, 2, "3")
        self.assertEqual(r7.x, '3')

        r8 = Rectangle(1, 2, 3, "4")
        self.assertEqual(r8.y, '4')

        r9 = Rectangle(-1, 2)
        self.assertEqual(r9.width, -1)

        r10 = Rectangle(0, 2)
        self.assertEqual(r10.width, 0)

        r11 = Rectangle(1, 0)
        self.assertEqual(r11.width, 1)


if __name__ == '__main__':
    unittest.main()
