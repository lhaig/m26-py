
import os
import time
import unittest

from m26.m26_age_calculator import M26AgeCalculator


class M26AgeCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.epoch = str(int(time.time()))

    def tearDown(self):
        pass

    def test_milliseconds_per_year(self):
        self.assertTrue(M26AgeCalculator.milliseconds_per_year() == 31557600000.0, "value should be 31557600000.0")

    def test_calculate(self):
        a1 = M26AgeCalculator.calculate('1960-10-01', '2015-10-01')
        actual = 54.997946611909654
        self.assertTrue(a1.value > (actual - 0.000001), "value is too small")
        self.assertTrue(a1.value < (actual + 0.000001), "value is too large")
