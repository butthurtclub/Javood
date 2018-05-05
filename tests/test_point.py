__author__ = 'Javood'

from src.point import *
import unittest


class PointTest(unittest.TestCase):
    def test_initial(self):
        first = Point(4, 2)
        self.assertIsInstance(first, Point)
        self.assertEqual(first.x, 4)
        self.assertEqual(first.y, 2)
        self.assertEqual((first.x, first.y), (4, 2))

    def test_distance(self):
        first = Point(4, 0)
        second = Point(0, 0)
        self.assertEqual(first.distance(second), 4)

    def test_equal(self):
        first = Point(4, 2)
        second = Point(4, 2)
        self.assertEqual(first, second)

    def test_not_equal(self):
        first = Point(4, 2)
        second = Point(4, 3)
        self.assertNotEqual(first, second)


if __name__ == '__main__':
    unittest.main()
