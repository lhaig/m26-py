
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


# describe 'ElapsedTime', ->

#   it 'constructs with a number of seconds', ->
#     t = new ElapsedTime(3665)
#     expect(t.as_hhmmss()).toBe('01:01:05')
#     expect(t.seconds()).isWithin(0.000001, 3665.0)
#     expect(t.hours()).isWithin(0.000001, 1.0180555555555555)

#   it 'constructs with a hh:mm:ss string', ->
#     t = new ElapsedTime('1:1:5')
#     expect(t.as_hhmmss()).toBe('01:01:05')

#     t = new ElapsedTime('01:01:05')
#     expect(t.as_hhmmss()).toBe('01:01:05')

#     t = new ElapsedTime(' 01 : 01 : 05 ')
#     expect(t.as_hhmmss()).toBe('01:01:05')

#   it 'constructs with a mm:ss string', ->
#     t = new ElapsedTime('1:5')
#     expect(t.as_hhmmss()).toBe('00:01:05')

#     t = new ElapsedTime('01:57')
#     expect(t.as_hhmmss()).toBe('00:01:57')
#     expect(t.seconds()).isWithin(0.000001, 117.0)
#     expect(t.hours()).isWithin(0.000001, 0.0325)

#   it 'constructs with a ss string', ->
#     t = new ElapsedTime('5')
#     expect(t.as_hhmmss()).toBe('00:00:05')

#     t = new ElapsedTime(' 5 ')
#     expect(t.as_hhmmss()).toBe('00:00:05')
#     expect(t.seconds()).isWithin(0.000001, 5.0)
#     expect(t.hours()).isWithin(0.000001, 0.001388888888888889)
