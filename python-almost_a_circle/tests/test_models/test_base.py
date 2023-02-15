# tests/test_base.py

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_new_instance_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_specified_id(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_multiple_specified_ids(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(13)
        self.assertEqual(b5.id, 13)
