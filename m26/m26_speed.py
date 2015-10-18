__author__ = 'cjoakim'

import math

# from .m26_distance import M26Distance
from .m26_elapsed_time import M26ElapsedTime


class M26Speed(object):

    def __init__(self, d, et):
        self.dist = d    # an instance of M26Distance
        self.etime = et  # an instance of M26ElapsedTime

    def mph(self):
        return self.dist.as_miles() / self.etime.hours()

    def kph(self):
        return self.dist.as_kilometers() / self.etime.hours()

    def yph(self):
        return self.dist.as_yards() / self.etime.hours()

    def pace_per_mile(self):
        spm = self.seconds_per_mile()
        mm = math.floor(spm / 60.0)
        ss = spm - (mm * 60.0)

        if ss < 10:
            ss = "0{0}".format(ss)
        else:
            ss = "{0}".format(ss)

        if len(ss) > 5:
            ss = ss[0:5]

        return "{0}:{1}".format(mm, ss)

    def seconds_per_mile(self):
        return float(self.etime.secs / self.dist.as_miles())

    def projected_time(self, another_distance, algorithm='simple'):
        if algorithm is 'riegel':
            t1 = float(self.etime.secs)
            d1 = self.dist.as_miles()
            d2 = another_distance.as_miles()
            t2 = t1 * math.pow(float(d2 / d1), float(1.06))
            et = M26ElapsedTime(t2)
            return et.as_hhmmss()
        else:
            secs = float(self.seconds_per_mile() * another_distance.as_miles())
            et = M26ElapsedTime(secs)
            return et.as_hhmmss()

    def age_graded(self, event_age, graded_age):
        pass

#   projected_time: (another_distance, algorithm='simple') ->
#     if algorithm is 'riegel'
#       t1 = @et.secs
#       d1 = @d.as_miles()
#       d2 = another_distance.as_miles()
#       # t2 = t1.to_f * ((d2.to_f / d1.to_f) ** pow)   Math.pow(3,3)
#       t2 = t1 * Math.pow((d2 / d1), 1.06)
#       et = new ElapsedTime(t2);
#       return et.as_hhmmss()
#     else
#       secs = @seconds_per_mile() * another_distance.as_miles()
#       et = new ElapsedTime(secs);
#       return et.as_hhmmss()

#   age_graded: (event_age, graded_age) ->
#     ag_factor = event_age.max_pulse() / graded_age.max_pulse()
#     event_secs = this.et.seconds()
#     graded_secs = event_secs * ag_factor
#     graded_et   = new ElapsedTime(graded_secs)
#     new Speed(this.d, graded_et)
