
import os
import time
import unittest

from m26.m26_age import M26Age


class M26AgeTest(unittest.TestCase):

    def setUp(self):
        self.epoch = str(int(time.time()))

    def tearDown(self):
        pass

    def test_constructor(self):
        a = M26Age()
        self.assertTrue(a.value == 0, "value should be 0")

    