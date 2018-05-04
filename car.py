__author__ = 'Javood'

from point import Point
import unittest

__all__ = (
    'Car',
)

class OutOfFuelException(Exception):
    """The fuel is over"""
    pass
    
class Car:
    """
    A class for Car representing.
    
    Use types: string, integer, Point().
    
    Usage:
    >>> car = Car()
    >>> print(car)
    Model - Range Rover, Location - (0, 0)
    >>> destination = Point(1, 1)
    >>> car.drive(destination)
    >>> print(car)
    Model - Range Rover, Location - (1, 1)
    """
    def __init__(self, fuel_capacity = 60, fuel_consumtion = 0.6, location = Point(0, 0), model = 'Range Rover'):
        """
        The initializer.
        
        :param fuel_capacity: Possible values: integer, float.
        :param fuel_consumption: Possible values: integer, float.
        :param location: Possible values: Point().
        :param model: Possible values: string.
        """
        self._fuel_capacity = fuel_capacity
        self._fuel_consumption = fuel_consumtion
        self._location = location
        self._model = model
        self._fuel_amount = 0

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @model.getter
    def model(self):
        return self._model

    @property
    def fuel_amount(self):
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        self._fuel_amount = value

    @fuel_amount.getter
    def fuel_amount(self):
        return self._fuel_amount

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value):
        self._fuel_capacity = value

    @fuel_capacity.getter
    def fuel_capacity(self):
        return self._fuel_capacity

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self._fuel_consumption = value

    @fuel_consumption.getter
    def fuel_consumption(self):
        return self._fuel_consumption

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @location.getter
    def location(self):
        return self._location

    def __str__(self):
        return 'Model - {}, Location - {}'.format(self.model, self.location)

    def __repr__(self):
        return 'Car ' + str(self)


    def drive(self, destination):
        """
        Drives car from current location to destination.
        
        :param destination: final point.
        :type destination: Point().
        """
        
        fuel_need = destination.distance(self.location) * self.fuel_consumption
        new_fuel_amount = self.fuel_amount - fuel_need

        if new_fuel_amount < 0:
            raise OutOfFuelException('Out of fuel')
        self.fuel_amount = new_fuel_amount
        self.location = destination

    def refill(self, fuel):
        """
        Refills car fuel tank.
        
        :param fuel: fuel amount for refueling the car.
        :type fuel: integer, float.
        """
        self.fuel_amount = self.fuel_amount + fuel
        if self.fuel_amount > self.fuel_capacity:
            self.fuel_amount = self.fuel_capacity


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