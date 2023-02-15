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
        b3 = Base(89)
        self.assertEqual(b3.id, 89)
