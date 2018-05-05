__author__ = 'Javood'

from point import Point

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

    def __init__(
        self,
        fuel_capacity=60,
        fuel_consumtion=0.6,
        location=Point(0, 0),
        model='Range Rover'
            ):

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

    @property
    def fuel_amount(self):
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        self._fuel_amount = value

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value):
        self._fuel_capacity = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self._fuel_consumption = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def __str__(self):
        return 'Model - {}, Location - {}'.format(self.model, self.location)

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
