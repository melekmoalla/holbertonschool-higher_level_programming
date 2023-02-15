import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_constructor_no_id(self):
        """Test that the Base constructor sets id attribute
        to the expected value when no id is passed as argument.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_constructor_with_id(self):
        """Test that the Base constructor sets id attribute
        to the expected value when an id is passed as argument.
        """
        b1 = Base(10)
        b2 = Base(20)
        b3 = Base(30)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)
        self.assertEqual(b3.id, 30)
