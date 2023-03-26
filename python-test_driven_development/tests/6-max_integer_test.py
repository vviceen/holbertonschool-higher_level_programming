#!/usr/bin/python3
""" task 6 """
import unittest
max_integer = __import__('6-max_integer').max_integer


class Tests_for_task6(unittest.TestCase):
    """ unittest for the function max_integer """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([6, 2, 3, 4, 5, 1]), 6)
        self.assertEqual(max_integer([1, 2, 3, 6, 5, 4]), 6)

    def test_max_integer_empty(self):
        """ check list not empty """
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer(), None)

    def test_max_float(self):
        """ test max float """
        self.assertEqual(max_integer([1.3, 4.5, 2.0, 5.6]), 5.6)
