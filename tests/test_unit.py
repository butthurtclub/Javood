__author__ = 'Javood'

from src.unit import *
import unittest


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
