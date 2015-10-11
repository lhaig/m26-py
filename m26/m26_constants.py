__author__ = 'cjoakim'


class M26Constants(object):

    @classmethod
    def uom_miles(cls):
        return 'm'

    @classmethod
    def uom_kilometers(cls):
        return 'k'

    @classmethod
    def uom_yards(cls):
        return 'y'

    @classmethod
    def units_of_measure(cls):
        return ('m', 'k', 'y')

    @classmethod
    def kilometers_per_mile(cls):
        return 1.609344

    @classmethod
    def miles_per_kilometer(cls):
        return 0.621371192237334

    @classmethod
    def yards_per_kilometer(cls):
        return 1093.6132983377076

    @classmethod
    def feet_per_kilometer(cls):
        return 3280.839895013123

    @classmethod
    def feet_per_meter(cls):
        return 3.280839895013123

    @classmethod
    def yards_per_mile(cls):
        return 1760.0   

    @classmethod
    def seconds_per_hour(cls):
        return 3600.0   

    @classmethod
    def miles_per_marathon(cls):
        return 26.2
