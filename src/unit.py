__author__ = 'Javood'

__all__ = (
    'Unit',
)


class UnitIsDeadException(Exception):
    """Unit is dead"""
    pass


class Unit():
    """
    A class for unit representing.

    Usage:
    >>>unit = Unit("Warrior", 100, 20)
    >>>print(unit)
    Name - Warrior, Hit Points - 100, Damage - 20
    >>> unit.hp_limit
    100
    >>>unit2 = Unit("Rogue", 80, 30)
    >>> unit2.attack(unit1)
    >>>print(unit)
    Name - Warrior, Hit Points - 70, Damage - 20
    >>>unit2.hit_points
    70
    >>> unit.add_hit_points(100)
    >>> print(unit)
    Name - Warrior, Hit Points - 100, Damage - 20
    """

    def __init__(self, name, hit_points, dmg):
        """
        The initializer

        :param name: Unit name
        :type name: string
        :param hit_points: Unit hit points
        :type hit_points: integer, float
        :param hp_limit: Unit hit points limit
        :type hp_limit: integer, float
        :param dmg: Unit damage
        :type dmg: integer, float
         """
        self._name = name
        self._hit_points = hit_points
        self._hp_limit = hit_points
        self._dmg = dmg

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = value

    @property
    def hp_limit(self):
        return self._hp_limit

    @hp_limit.setter
    def hp_limit(self, value):
        self._hp_limit = value

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._dmg = value

    def __str__(self):
        return 'Name - {}, Hit Points - {}, Damage - {}'.format(self.name, self.hit_points, self.dmg)

    def ensure_is_alive(self):
        """
        Checks if the unit is alive or dead.

        :raise UnitIsDeadException: If unit are not with us allready.
        """
        if self.hit_points == 0:
            raise UnitIsDeadException('Unit is dead')

    def take_damage(self, dmg):
        """
        Unit take damage
        :param dmg: the number of damage
        :type dmg: integer, float
        :raise: UnitIsDeadException: If Unit is allready dead
        """
        self.ensure_is_alive()
        self.hit_points -= dmg
        if self.hit_points < 0:
            self.hit_points = 0
            raise UnitIsDeadException("Unit is dead")

    def add_hit_points(self, hp):
        """
        Adds hit points to the unit.
        :param hit_points: the number of the health points to add.
        :type hit_points: integer, float.
        """
        self.ensure_is_alive()

        new_hp = self.hit_points + hp

        if new_hp > self.hp_limit:
            new_hp = self.hp_limit

        self.hit_points = new_hp

    def attack(self, enemy):
        """
        Attack enemy unit.

        :param enemy: Enemy unit.
        :type enemy: Unit().
        :raise UnitIsDeadException: When trying to access a dead unit.
        """
        enemy.ensure_is_alive()
        self.ensure_is_alive()

        enemy.take_damage(self.dmg)
        enemy.counter_attack(self)

    def counter_attack(self, enemy):
        """
        Counter attack unit.

        :param enemy: Unit to be counterattacked.
        :type enemy: Unit().
        """
        self.ensure_is_alive()
        enemy.take_damage(self.dmg / 2)
