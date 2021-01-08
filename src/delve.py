from src.die_roller import DieRoller
from src.io import Loot
from src.io_generator import IoGenerator


# noinspection PyMethodMayBeStatic
class Delve:
    def __init__(self, area_level, task_difficulty, die_roller=DieRoller(), io_generator=None):
        if io_generator is not None:
            self.io_generator = io_generator
        else:
            self.io_generator = IoGenerator(area_level, die_roller)

        self.task_difficulty = task_difficulty
        self.die_roller = die_roller

    def salvage(self):
        task_result = self.die_roller.d20()
        if self.task_successful(task_result):
            salvage_discovery_result = self.die_roller.d6()
            shins = self._salvage_shins()
            iotum = self._salvage_iotum(salvage_discovery_result)
            parts = self._salvage_parts(salvage_discovery_result, iotum)
            return Loot(task_result, shins, parts, iotum)

        return Loot(task_result)

    def _salvage_shins(self):
        return self.die_roller.d10()

    def _salvage_parts(self, salvage_discovery_roll, iotum):
        parts = 0
        if salvage_discovery_roll <= 3:
            parts = 1
        else:
            for io in iotum:
                parts += io.level

        return parts

    def _salvage_iotum(self, salvage_discovery_roll):
        iotum = []

        if salvage_discovery_roll >= 4:
            iotum.append(self.io_generator.generate())
        if salvage_discovery_roll >= 5:
            iotum.append(self.io_generator.generate())
        if salvage_discovery_roll >= 6:
            iotum.append(self.io_generator.generate())

        return iotum

    def task_successful(self, task_result):
        return task_result >= self.target_number()

    def target_number(self):
        return self.task_difficulty * 3
