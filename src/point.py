__author__ = 'Javood'

from math import hypot

__all__ = (
    'Point',
)


class Point():
    """
    A class for Point(x,y) representing.
    Supported types: integer, floating.

    Usage:
    >>> a = Point()
    >>> a
    (0, 0)
    >>> b = Point(0, 2)
    >>> b
    (0, 2)
    >>> a.distance(b)
    2.0
    >>> a == b
    False
    >>> a = b
    >>> a == b
    >>> True
    """

    def __init__(self, x=0.0, y=0.0):
        """
        The initializer.
        :param x: x-coordinate. Possible values: float, integer.
        :param y: y-coordinate. Possible values: float, integer.
        """

        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def distance(self, other):
        """
        Counts distance between two points.
        :param other: Point.
        :return: float.
        """

        return hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
