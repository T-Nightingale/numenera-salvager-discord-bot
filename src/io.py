class Loot:
    def __init__(self, task_result, task_difficulty, shins=0, parts=0, iotum=[]):
        self.task_result = task_result
        self.task_difficulty = task_difficulty
        self.shins = shins
        self.parts = parts
        self.iotum = iotum

    def message(self):
        message = '\n'.join(
            [self.task_result_message(), self.shins_message(), self.parts_message(), self.iotum_message()])
        return message

    def task_result_message(self):
        return 'Roll: ' + str(self.task_result) + '/' + str(self.task_difficulty)

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
