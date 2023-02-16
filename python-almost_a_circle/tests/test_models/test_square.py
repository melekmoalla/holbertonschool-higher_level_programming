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
        self.assertEqual(s1_dictionary, s1_dictionary)

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
        s27.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s27, s27)

    def test_square_create(self):
        with self.assertRaises(TypeError) as e:
            r28 = Square.create(**{'id': 89})
        self.assertEqual(
            str(e.exception), "__init__() missing 1 required positional argument: 'size'")

        s29 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s29, s29)

        s30 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s30, s30)

        s31 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s31, s31)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", mode="r") as file:
            contents = file.read()
            self.assertEqual(contents, '[]')

    def test_save_to_file_square(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, contents)

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(), '[{"id": 22, "x": 0, "size": 1, "y": 0}]')

        Square.save_to_file(None)
        with open("Square.json", mode="r") as file:
            contents = file.read()
            self.assertEqual(contents, '[]')

    def test_load_from_file(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, list_squares_output)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str_method(self):
        s1 = Square(4, 2, 1, 12)
        expected_output = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s1), expected_output)

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        expected_output = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(s1.to_dictionary(), expected_output)

    def test_display_exit(self):
        r = Square(2, 3)
        r.display()
        self.assertEqual(r.display(), None)
