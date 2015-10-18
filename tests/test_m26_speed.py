
import os
import time
import unittest

from m26.m26_age          import M26Age
from m26.m26_distance     import M26Distance
from m26.m26_elapsed_time import M26ElapsedTime
from m26.m26_speed        import M26Speed


class M26SpeedTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_a_walk_with_round_numbers(self):
        d = M26Distance(2.0)
        t = M26ElapsedTime('30:00')
        s = M26Speed(d, t)
        self.assertAlmostEqual(s.mph(), 4.0000)
        self.assertAlmostEqual(s.kph(), 6.437376)
        self.assertAlmostEqual(s.yph(), 7040.0000)
        self.assertAlmostEqual(s.seconds_per_mile(), 900.0)
        self.assertTrue(s.pace_per_mile() == '15:00.0', "pace_per_mile is incorrect")

    def test_a_marathon_with_fractional_numbers(self):
        d = M26Distance(26.2)
        t = M26ElapsedTime('3:47:30')
        s = M26Speed(d, t)
        ppm = s.pace_per_mile()

        self.assertAlmostEqual(s.mph(), 6.90989010989011)
        self.assertAlmostEqual(s.kph(), 11.120390189010989)
        self.assertAlmostEqual(s.yph(), 12161.4065934066)
        self.assertAlmostEqual(s.seconds_per_mile(), 520.992366412214)
        self.assertTrue(ppm == '8:40.99', "pace_per_mile is incorrect; {0}".format(ppm))

    def test_project_time_with_linear_formula(self):
        d = M26Distance(10.0)
        t = M26ElapsedTime('1:30:0')
        s = M26Speed(d, t)
        spm = s.seconds_per_mile()
        ppm = s.pace_per_mile()
        self.assertAlmostEqual(spm, 540.0)
        self.assertTrue(ppm == '9:00.0', "pace_per_mile is incorrect; {0}".format(ppm))

        d2 = M26Distance(20.0)
        hhmmss = s.projected_time(d2)
        self.assertTrue(hhmmss == '03:00:00', "projected_time is incorrect; {0}".format(hhmmss))

    def test_project_time_with_exponential_formula(self):
        d = M26Distance(10.0)
        t = M26ElapsedTime('1:30:0')
        s = M26Speed(d, t)
        spm = s.seconds_per_mile()
        ppm = s.pace_per_mile()
        self.assertAlmostEqual(spm, 540.0)
        self.assertTrue(ppm == '9:00.0', "pace_per_mile is incorrect; {0}".format(ppm))

        d2 = M26Distance(20.0)
        hhmmss = s.projected_time(d2, 'riegel')
        self.assertTrue(hhmmss == '03:07:38', "projected_time is incorrect; {0}".format(hhmmss))

    def test_age_graded_time(self):
        d = M26Distance(26.2)
        t = M26ElapsedTime('3:47:30')
        s1 = M26Speed(d, t)
        a1 = M26Age(42.5)
        a2 = M26Age(43.5)
        a3 = M26Age(57.1)
        s2 = s1.age_graded(a1, a2)
        s3 = s1.age_graded(a1, a3)

        self.assertAlmostEqual(s1.mph(), 6.90989010989011)
        self.assertAlmostEqual(s2.mph(), 6.870961151524531)
        self.assertAlmostEqual(s3.mph(), 6.341527317752669)

#   it 'should calculate an age_graded Speed', ->
#     d  = new Distance(26.2)
#     t  = new ElapsedTime('3:47:30')
#     s1 = new Speed(d, t)
#     a1 = new Age(42.5)
#     a2 = new Age(43.5)
#     a3 = new Age(57.1)
#     expect(s1.mph()).isWithin(0.000001, 6.90989010989011)
#     s2 = s1.age_graded(a1, a2)
#     s3 = s1.age_graded(a1, a3)
#     expect(s2.mph()).isWithin(0.000001, 6.870961151524531)
#     expect(s3.mph()).isWithin(0.000001, 6.341527317752669)
