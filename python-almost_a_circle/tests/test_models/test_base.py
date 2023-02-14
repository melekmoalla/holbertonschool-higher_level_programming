import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_auto_id(self):
        """Test that new instances of Base have a unique ID assigned automatically"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_saving_the_ID_passed_exists(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)


if __name__ == '__main__':
    unittest.main()
