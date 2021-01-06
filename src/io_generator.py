from src.io import Io


# noinspection PyMethodMayBeStatic
class IoGenerator:
    def __init__(self, area_level, die_roller):
        self.area_level = area_level
        self.die_roller = die_roller

    def generate(self):
        iotum_roll = self.die_roller.d100()
        if (iotum_roll <= 12):
            return Io('Io', 1,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 24):
            return Io('Responsive Synth', 2,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 32):
            return Io('Apt Clay', 3,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 38):
            return Io('Bio-Circuitry', 4,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 44):
            return Io('Synthsteel', 4,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 50):
            return Io('Pliable Metal', 4,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 55):
            return Io('Azure Steel', 5,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 60):
            return Io('Mimetic Gel', 5,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 65):
            return Io('Quantium', 5,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 69):
            return Io('Amber Crystal', 6,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 71):
            return Io('Protomatter (if salvage source is less than 40ft. on a side, 1d6 Thaum Dust instead)', 6,  1)
        elif (iotum_roll <= 75):
            return Io('Thaum Dust', 6,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 78):
            return Io('Smart Tissue', 7,  self.die_roller.d6() + self.area_level)
        elif (iotum_roll <= 81):
            return Io('Psiranium', 7,  2)
        elif (iotum_roll <= 84):
            return Io('Kaon Dot', 7,  2)
        elif (iotum_roll <= 86):
            return Io('Plan Seed', 1,  1)
        elif (iotum_roll <= 89):
            return Io('Monopole', 7,  2)
        elif (iotum_roll <= 91):
            return Io('Midnight Stone', 8,  2)
        elif (iotum_roll <= 93):
            return Io('Oraculum', 8,  1)
        elif (iotum_roll <= 95):
            return Io('Virtuon Particle', 8,  1)
        elif (iotum_roll <= 96):
            return Io('Tamed Iron', 9,  1)
        elif (iotum_roll <= 97):
            return Io('Philosophine', 9,  1)
        elif (iotum_roll <= 98):
            return Io('Data Orb', 9,  1)
        elif (iotum_roll <= 99):
            return Io('Scalar Boson Rod', 9,  1)
        elif (iotum_roll <= 100):
            return Io('Cosmic Foam', 10,  1)
