from unittest import TestCase
from src.delve import Delve
from src.die_roller import DieRoller


class MockDieRoller(DieRoller):
    def __init__(self):
        super().__init__()
        self.__d6_result = None
        self.__d10_result = None
        self.__d20_result = None
        self.__d100_result = None

    def d6(self):
        return self.__d6_result

    def set_d6(self, d6_result):
        self.__d6_result = d6_result

    def d10(self):
        return self.__d10_result

    def set_d10(self, d10_result):
        self.__d10_result = d10_result

    def d20(self):
        return self.__d20_result

    def set_d20(self, d20_result):
        self.__d20_result = d20_result

    def d100(self):
        return self.__d100_result

    def set_d100(self, d100_result):
        self.__d100_result = d100_result


class TestDelve(TestCase):
    def test_salvage_failure(self):
        die_roller = MockDieRoller()
        delve = Delve(5, 5, die_roller)

        die_roller.set_d20(1)

        loot = delve.salvage()

        self.assertEqual(0, loot.shins)
        self.assertEqual(0, loot.parts)
        self.assertEqual(0, len(loot.iotum))

    def test_salvage_shins(self):
        die_roller = MockDieRoller()
        delve = Delve(2, 2, die_roller)

        die_roller.set_d20(2 * 3)
        die_roller.set_d6(2)
        die_roller.set_d10(3)

        loot = delve.salvage()

        self.assertEqual(3, loot.shins)

    def test_salvage_parts_no_iotum(self):
        die_roller = MockDieRoller()
        delve = Delve(5, 5, die_roller)

        die_roller.set_d20(5 * 3)

        die_roller.set_d6(1)
        self.assertEqual(1, delve.salvage().parts)

        die_roller.set_d6(2)
        self.assertEqual(1, delve.salvage().parts)

        die_roller.set_d6(3)
        self.assertEqual(1, delve.salvage().parts)

    def test_salvage_parts_from_iotum(self):
        die_roller = MockDieRoller()
        delve = Delve(5, 5, die_roller)

        die_roller.set_d20(5 * 3)
        die_roller.set_d100(50)  # pliable metal level 4

        die_roller.set_d6(6)
        self.assertEqual(4 * 3, delve.salvage().parts)

    def test_salvage_iotum(self):
        die_roller = MockDieRoller()
        delve = Delve(5, 5, die_roller)

        die_roller.set_d20(5 * 3)
        die_roller.set_d100(100)  # cosmic foam, level 10, 1 unit

        die_roller.set_d6(4)
        self.assertEqual(1, len(delve.salvage().iotum))

        die_roller.set_d6(5)
        self.assertEqual(2, len(delve.salvage().iotum))

        die_roller.set_d6(6)
        self.assertEqual(3, len(delve.salvage().iotum))
        salvage_result = delve.salvage()
        self.assertEqual('Cosmic Foam', salvage_result.iotum[0].name)
        self.assertEqual(10, salvage_result.iotum[0].level)
        self.assertEqual(1, salvage_result.iotum[0].units)
