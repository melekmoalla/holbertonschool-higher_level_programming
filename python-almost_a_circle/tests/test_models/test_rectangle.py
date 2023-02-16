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

        with self.assertRaises(TypeError) as e:
            r5 = Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            r6 = Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            r7 = Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            r8 = Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            r9 = Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r10 = Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r11 = Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_area(self):
        r12 = Rectangle(8, 7, 0, 0, 12)
        r12.area()

    def test_str(self):
        r13 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r13, r13)

    def test_to_to_dictionary(self):
        s55 = Rectangle(10, 2, 1)
        s1_d = s55.to_dictionary()
        a = {'x': 1, 'y': 0, 'id': 5, 'height': 2, 'width': 10}
        self.assertEqual(s1_d, a)

    def test_update(self):
        s15 = Rectangle(5, 5)
        s15.update()
        self.assertEqual(s15.id, 6)

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
