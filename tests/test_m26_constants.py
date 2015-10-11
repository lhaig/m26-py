
import os
import time
import unittest

from m26.m26_constants import M26Constants


class M26ConstantsTest(unittest.TestCase):

  def setUp(self):
    self.epoch = str(int(time.time()))

  def tearDown(self):
    pass

  def test_miles_per_marathon(self):
    n = M26Constants.miles_per_marathon()
    self.assertTrue(str(n) == '26.2', "miles_per_marathon should be 26.2")

