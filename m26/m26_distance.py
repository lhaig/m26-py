__author__ = 'cjoakim'

from .m26_constants import M26Constants


class M26Distance(object):

    def __init__(self, dist=0.0, uom=M26Constants.uom_miles()):
        self.value = float(dist)
        self.uom   = self.unit_of_measure(uom)

    def unit_of_measure(self, s):
        u = str(s).strip().lower()
        if u == 'k':
            return M26Constants.uom_kilometers()
        elif u == 'y':
            return M26Constants.uom_yards()
        else:
            return M26Constants.uom_miles()

    def is_miles(self):
        return self.uom == M26Constants.uom_miles()

    def is_kilometers(self):
        return self.uom == M26Constants.uom_kilometers()

    def is_yards(self):
        return self.uom == M26Constants.uom_yards()

    def as_miles(self):
        if self.is_miles():
            return self.value
        elif self.is_kilometers():
            return self.value / M26Constants.kilometers_per_mile()
        else:
            return self.value / M26Constants.yards_per_mile()

    def as_kilometers(self):
        if self.is_miles():
            return self.value * M26Constants.kilometers_per_mile()
        elif self.is_kilometers():
            return self.value
        else:
            return self.value / M26Constants.yards_per_kilometer()

    def as_yards(self):
        if self.is_miles():
            return self.value * M26Constants.yards_per_mile()
        elif self.is_kilometers():
            return self.value * M26Constants.yards_per_kilometer()
        else:
            return self.value

    def add(self, another_instance):
        if self.is_miles():
            self.value = self.value + another_instance.as_miles()
        elif self.is_kilometers():
            self.value = self.value + another_instance.as_kilometers()
        else:
            self.value = self.value + another_instance.as_yards()

    def subtract(self, another_instance):
        if self.is_miles():
            self.value = self.value - another_instance.as_miles()
        elif self.is_kilometers():
            self.value = self.value - another_instance.as_kilometers()
        else:
            self.value = self.value - another_instance.as_yards()
 