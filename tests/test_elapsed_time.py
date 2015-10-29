
import os
import time
import unittest

from m26.elapsed_time import ElapsedTime


class ElapsedTimeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor_with_number(self):
        t = ElapsedTime(3665)
        self.assertAlmostEqual(t.hh,      1.0000)
        self.assertAlmostEqual(t.mm,      1.0000)
        self.assertAlmostEqual(t.ss,      5.0000)
        self.assertAlmostEqual(t.secs,    3665.0000)
        self.assertAlmostEqual(t.hours(), 1.0180555555555555)
        self.assertTrue(t.as_hhmmss() == '01:01:05', "as_hhmmss is incorrect")

    def test_constructor_with_string(self):
        t = ElapsedTime('3:47:30')
        self.assertAlmostEqual(t.hh,      3.0000)
        self.assertAlmostEqual(t.mm,      47.0000)
        self.assertAlmostEqual(t.ss,      30.0000)
        self.assertAlmostEqual(t.secs,    13650.0000)
        self.assertAlmostEqual(t.hours(), 3.7916666666666665)
        self.assertTrue(t.as_hhmmss() == '03:47:30', "as_hhmmss is incorrect")

    def test_constructor_with_empty_string(self):
        t = ElapsedTime('')
        self.assertAlmostEqual(t.hh,      0.0000)
        self.assertAlmostEqual(t.mm,      0.0000)
        self.assertAlmostEqual(t.ss,      00.0000)
        self.assertAlmostEqual(t.secs,    00.0000)
        self.assertAlmostEqual(t.hours(), 0.0)
        self.assertTrue(t.as_hhmmss() == '00:00:00', "as_hhmmss is incorrect")

    def test_constructor_with_malformed_string(self):
        t = ElapsedTime('3:xx:q')
        self.assertAlmostEqual(t.hh,      3.0000)
        self.assertAlmostEqual(t.mm,      0.0000)
        self.assertAlmostEqual(t.ss,      0.0000)
        self.assertAlmostEqual(t.secs,    10800.0000)
        self.assertAlmostEqual(t.hours(), 3.000)
        self.assertTrue(t.as_hhmmss() == '03:00:00', "as_hhmmss is incorrect")
