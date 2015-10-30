
import pdb
import inspect
import json

import m26
from m26.age import Age
from m26.age_calculator import AgeCalculator
from m26.constants import Constants
from m26.distance import Distance
from m26.elapsed_time import ElapsedTime
from m26.run_walk_calculator import RunWalkCalculator
from m26.speed import Speed

if __name__ == "__main__":

    d1 = Distance(26.2)
    print(d1)
    print("d1, as_miles:      {0}".format(d1.as_miles()))
    print("d1, as_kilometers: {0}".format(d1.as_kilometers()))
    print("d1, as_yards:      {0}".format(d1.as_yards()))

    print('')
    d2 = Distance(50.0, Constants.uom_kilometers())
    print(d2)
    print("d2, as_miles:      {0}".format(d2.as_miles()))
    print("d2, as_kilometers: {0}".format(d2.as_kilometers()))
    print("d2, as_yards:      {0}".format(d2.as_yards()))

    print('')
    d3 = Distance(7040, Constants.uom_yards())
    print(d3)
    print("d3, as_miles:      {0}".format(d3.as_miles()))
    print("d3, as_kilometers: {0}".format(d3.as_kilometers()))
    print("d3, as_yards:      {0}".format(d3.as_yards()))

    print('')
    d4 = Distance(10.0, Constants.uom_kilometers())
    print(d4)

    print('')
    d4.add(d1)
    print(d4)

    print('')
    d4.subtract(d3)
    print(d4)

    print('')
    t1 = ElapsedTime('3:47:30')
    print(t1)
    print("t1 hours: {0}".format(t1.hours()))

    print('')
    t2 = ElapsedTime(3662)
    print(t2)
    print("t2 hours: {0}".format(t2.hours()))

    print('')
    s = Speed(d1, t1)
    print(s)
    print("s, mph: {0}".format(s.mph()))
    print("s, kph: {0}".format(s.kph()))
    print("s, yph: {0}".format(s.yph()))
    print("s, spm: {0}".format(s.seconds_per_mile()))
    print("s, ppm: {0}".format(s.pace_per_mile()))

    hhmmss_simple = s.projected_time(d2)
    hhmmss_riegel = s.projected_time(d2, 'riegel')
    print("projected_time, simple: {0}".format(hhmmss_simple))
    print("projected_time, riegel: {0}".format(hhmmss_riegel))

    print('')
    a = AgeCalculator.calculate('1960-10-01', '2015-10-18')
    print(a)

    print('')
    a2 = Age(58.1)
    graded = s.age_graded(a, a2)
    print("age graded: {0} {1} -> {2} {3}".format(
        t1.as_hhmmss(), a.value, graded.etime.as_hhmmss(), a2.value))
    zones = a2.training_zones()
    print(zones)

    print('')
    result = RunWalkCalculator.calculate('2:30', '9:16', '0:45', '17:00', 31.0)
    print(result)
    print('')