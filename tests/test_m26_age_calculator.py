
import os
import time
import unittest

from m26.m26_age_calculator import M26AgeCalculator


class M26AgeCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.epoch = str(int(time.time()))

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertTrue(0 == 0, "value should be 0")

    
# describe 'AgeCalculator', ->

#   it "should define milliseconds_per_year", ->
#     expect(AgeCalculator.milliseconds_per_year()).toEqual(31557600000)

#   it "should calculate and construct and Age", ->
#     a1 = AgeCalculator.calculate('1960-10-01', '2014-10-01')
#     a2 = AgeCalculator.calculate('2013-11-01')
#     expect(a1.val()).isWithin(0.01, 54.0)
#     expect(a2.val()).toBeGreaterThan(0.999)
#     expect(a2.val()).toBeLessThan(2) # TODO - update before November 2015
