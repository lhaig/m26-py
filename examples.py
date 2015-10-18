import json

from m26.m26_age import M26Age
from m26.m26_age_calculator import M26AgeCalculator
from m26.m26_distance import M26Distance
from m26.m26_elapsed_time import M26ElapsedTime
from m26.m26_run_walk_calculator import M26RunWalkCalculator
from m26.m26_speed import M26Speed


if __name__ == "__main__":
    a = M26AgeCalculator.calculate('1960-10-01', '2015-10-18')
    print(a)
    print("a, value: {0}".format(a.value))

    d = M26Distance(26.2)
    print(d)
    print("d, as_miles:      {0}".format(d.as_miles()))
    print("d, as_kilometers: {0}".format(d.as_kilometers()))
    print("d, as_yards:      {0}".format(d.as_yards()))

    t = M26ElapsedTime('3:47:30')
    print(t)
    print("t, hhmmss, secs, hours: {0} {1} {2}".format(t.as_hhmmss(), t.secs, t.hours()))

    s = M26Speed(d, t)
    print(s)
    print("s, mph: {0}".format(s.mph()))
    print("s, kph: {0}".format(s.kph()))
    print("s, yph: {0}".format(s.yph()))
    print("s, spm: {0}".format(s.seconds_per_mile()))
    print("s, ppm: {0}".format(s.pace_per_mile()))

    d2 = M26Distance(31.0)
    hhmmss_simple = s.projected_time(d2)
    hhmmss_riegel = s.projected_time(d2, 'riegel')
    print("proj time, simple: {0}".format(hhmmss_simple))
    print("proj time, riegel: {0}".format(hhmmss_riegel))

    a2 = M26Age(58.1)
    graded = s.age_graded(a, a2)
    print("age graded: {0} {1} -> {2} {3}".format(
        t.as_hhmmss(), a.value, graded.etime.as_hhmmss(), a2.value))

    result = M26RunWalkCalculator.calculate('2:30', '9:16', '0:45', '17:00', 31.0)
    print(json.dumps(result, sort_keys=True, indent=2))
