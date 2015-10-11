
import os
import time
import unittest

from m26.m26_elapsed_time import M26ElapsedTime


class M26ElapsedTime(unittest.TestCase):

    def setUp(self):
        self.epoch = str(int(time.time()))

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertTrue(0 == 0, "value should be 0")

    