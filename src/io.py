class Loot:
    def __init__(self, shins=0, parts=0, iotum=[]):
        self.shins = shins
        self.parts = parts
        self.iotum = iotum

    def message(self):
        message = '\n'.join([self.shins_message(), self.parts_message(), self.iotum_message()])
        return message

    def parts_message(self):
        return str(self.parts) + ' part' + self.pluralizer(self.parts)


    def shins_message(self):
        return str(self.shins) + ' shin' + self.pluralizer(self.shins)

    def pluralizer(self, number):
        return '' if number == 1 else 's'

    def iotum_message(self):
        if len(self.iotum) > 0:
            return '\n'.join([io.message() for io in self.iotum])
        else:
            return ''


class Io:
    def __init__(self, name, level, units):
        self.name = name
        self.level = level
        self.units = units

    def message(self):
        return "%d %s (level %d)" % (self.units, self.name, self.level)
