__author__ = 'Javood'

import unittest

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

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.getter
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = value

    @property
    def hp_limit(self):
        return self._hp_limit

    @hp_limit.getter
    def hp_limit(self):
        return self._hp_limit

    @hp_limit.setter
    def hp_limit(self, value):
        self._hp_limit = value

    @property
    def dmg(self):
        return self._dmg

    @dmg.getter
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._dmg = value

    def __str__(self):
        return 'Name - {}, Hit Points - {}, Damage - {}'.format(self.name, self.hit_points, self.dmg)

    def __repr__(self):
        return 'Unit ' + str(self)

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

class TestUnit(unittest.TestCase):
    def test_init(self):
        warrior = Unit("warrior", 100, 20)
        rogue = Unit("rogue", 80, 30)
        self.assertEqual(warrior.name, 'warrior')
        self.assertEqual(rogue.name, "rogue")
        self.assertEqual(warrior.hit_points, 100)
        self.assertEqual(rogue.hit_points, 80)
        self.assertEqual(warrior.hp_limit, 100)
        self.assertEqual(rogue.hp_limit, 80)
        self.assertEqual(warrior.dmg, 20)
        self.assertEqual(rogue.dmg, 30)

    def test_ensure_is_alive(self):
        warrior = Unit("warrior", 0, 20)
        rogue = Unit("rogue", 80, 30)

        self.assertEqual(rogue.ensure_is_alive(), None)

        with self.assertRaises(UnitIsDeadException):
            warrior.ensure_is_alive()

    def test_take_damage(self):
        warrior = Unit("warrior", 100, 20)
        rogue = Unit("rogue", 80, 30)

        with self.assertRaises(UnitIsDeadException):
            warrior.take_damage(1100)

        rogue.take_damage(20)
        self.assertEqual(rogue.hit_points, 60)
        rogue.take_damage(20)
        self.assertEqual(rogue.hit_points, 40)
        rogue.take_damage(20)
        self.assertEqual(rogue.hit_points, 20)

    def test_add_hit_points(self):
        warrior = Unit("warrior", 100, 20)

        self.assertEqual(warrior.hit_points, 100)
        warrior.take_damage(90)
        warrior.add_hit_points(10)
        self.assertEqual(warrior.hit_points, 20)
        warrior.add_hit_points(10)
        self.assertEqual(warrior.hit_points, 30)
        warrior.add_hit_points(10)
        self.assertEqual(warrior.hit_points, 40)
        warrior.add_hit_points(10000)
        self.assertEqual(warrior.hit_points, 100)

    def test_attack(self):
        rogue = Unit("rogue", 80, 30)
        warrior = Unit("warrior", 100, 20)

        rogue.attack(warrior)
        self.assertEqual(rogue.hit_points, 70)
        self.assertEqual(warrior.hit_points, 70)

        warrior.attack(rogue)
        self.assertEqual(warrior.hit_points, 55)
        self.assertEqual(rogue.hit_points, 50)

    def test_counter_attack(self):
        rogue = Unit("rogue", 80, 30)
        warrior = Unit("warrior", 100, 20)

        rogue.counter_attack(warrior)
        self.assertEqual(rogue.hit_points, 80)
        self.assertEqual(warrior.hit_points, 85)

        warrior.counter_attack(rogue)
        self.assertEqual(warrior.hit_points, 85)
        self.assertEqual(rogue.hit_points, 70)

if __name__ == '__main__':
    unittest.main()