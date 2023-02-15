#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):


    def test_base_id(self):

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

if __name__ == "__main__":
    unittest.main()




