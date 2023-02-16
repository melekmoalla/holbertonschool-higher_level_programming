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
        self.assertEqual(r5.width, '1')

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
        self.assertEqual(r11.height, 0)

    def test_area(self):
        r12 = Rectangle(8, 7, 0, 0, 12)
        r12.area(), 6

    def test_str(self):
        r13 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r13, r13)

    def test_to_to_dictionary(self):
        s55 = Rectangle(10, 2, 1)
        s1_d = s55.to_dictionary()
        a = {'x': 1, 'y': 0, 'id': 12, 'height': 2, 'width': 10}
        self.assertEqual(s1_d, a)

    def test_update(self):
        s15 = Rectangle(5, 5)
        s15.update()
        self.assertEqual(s15.id, 13)

        s18 = Rectangle(5, 5)
        s18.update(89)
        self.assertEqual(s18.id, 89)

        s16 = Rectangle(5, 5)
        s16.update(89, 1)
        self.assertEqual(s16.width, 1)

        s17 = Rectangle(5, 5)
        s17.update(89, 1, 2)
        self.assertEqual(s17.height, 2)

        s19 = Rectangle(5, 5)
        s19.update(89, 1, 2, 3)
        self.assertEqual(s19.x, 3)

        s20 = Rectangle(5, 5)
        s20.update(89, 1, 2, 3, 4)
        self.assertEqual(s20.y, 4)


if __name__ == '__main__':
    unittest.main()
