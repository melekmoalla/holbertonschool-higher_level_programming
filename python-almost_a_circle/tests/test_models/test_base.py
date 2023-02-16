#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_new_instance_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, b2.id)

    def test_specified_id(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_none(self):
        rjson = Base.to_json_string(None)
        self.assertEqual(rjson, '[]')

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        json_dictionary = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_dictionary, '[{"id": 12}]')

    def test_from_json_string(self):
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])
    
    def test_display_exit(self):
        with self.assertRaises(TypeError) as e:
            r = Base(2, 3)
            r.display()
        self.assertEqual(str(
            e.exception), "__init__() takes from 1 to 2 positional arguments but 3 were given")


if __name__ == '__main__':
    unittest.main()