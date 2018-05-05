__author__ = 'Javood'

from src.car import *
from src.point import *
import unittest


class TestCar(unittest.TestCase):

    def test_initialize_car(self):
        car = Car(100, 0.5, Point(10, 0), 'Porshe')
        self.assertEqual(car.fuel_capacity, 100)
        self.assertEqual(car.fuel_consumption, 0.5)
        self.assertEqual(car.location.x, 10)
        self.assertEqual(car.location.y, 0)
        self.assertEqual(car.model, 'Porshe')

    def testRefillCar(self):
        car = Car(100, 0.5, Point(10, 0), 'Porshe')

        car.refill(40)
        self.assertEqual(car.fuel_amount, 40)
        car.refill(50)
        self.assertEqual(car.fuel_amount, 90)

    def test_drive_car(self):
        car = Car(100, 0.5, Point(10, 0), 'Porshe')
        car.refill(40)
        destination = Point(5, 0)

        car.drive(destination)

        self.assertEqual(car.fuel_amount, 37.5)
        self.assertEqual(car.location.x, 5)
        self.assertEqual(car.location.y, 0)

    def test_notenough_fuel(self):
        car = Car()
        car.refill(10)

        destination = Point(23, 0)
        with self.assertRaises(OutOfFuelException):
            car.drive(destination)

        self.assertEqual(car.fuel_amount, 10)
        self.assertEqual(car.location. x, 0)
        self.assertEqual(car.location.y, 0)


if __name__ == '__main__':
    unittest.main()
