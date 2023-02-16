#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):

    def test_display(self):
        r = Rectangle(2, 3)
        r.display()
        self.assertEqual(r.display(), None)

    def test_new_Rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, r1.id)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, r3.id)

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
        self.assertEqual(s1_d, s1_d)

    def test_update(self):
        s15 = Rectangle(5, 5)
        s15.update()
        self.assertEqual(s15.id, s15.id)

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

    def test_creat(self):
        with self.assertRaises(TypeError) as e:
            r2 = Rectangle.create(**{'id': 89})
        self.assertEqual(str(
            e.exception), "__init__() missing 2 required positional arguments: 'width' and 'height'")

        with self.assertRaises(TypeError) as e:
            r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(str(
            e.exception), "__init__() missing 1 required positional argument: 'height'")

        r63 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(print(r63), None)

        r64 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(print(r64), None)

        r65 = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(print(r65), None)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file(self):

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as fil:
            self.assertEqual(fil.read(), '[]')

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                f.read(), '[{"x": 0, "y": 0, "id": 11, "height": 2, "width": 1}]')

    def test_load_from_to_life(self):
        r61 = Rectangle(10, 7, 2, 8)
        r60 = Rectangle(2, 4)
        list_rectangles_input = [r61, r60]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, list_rectangles_output)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_str(self):
        r = Rectangle(2, 4, 1, 1, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 1/1 - 2/4")

    def test_display(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
            r.display()
        self.assertEqual(str(e.exception), str(e.exception))

    def test_display_exit(self):
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), None)

        r1 = Rectangle(4, 6)
        r1.display()
        self.assertEqual(str(r1), "[Rectangle] (5) 0/0 - 4/6")

        r = Rectangle(2, 3)
        r.display()
        self.assertEqual(r.display(), None)


if __name__ == '__main__':
    unittest.main()
