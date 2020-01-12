#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """ Class for unittest of max_integer function"""

    def test_max_intlist(self):
        """ Test when a list of integers is passed """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_intlist_neg(self):
        """ Test when a list of neg integers is passed """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_intlist_mix(self):
        """ Test when a list of neg and pos integers is passed """
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_max_floatlist(self):
        """ Test when a list of floats is passed """
        self.assertEqual(max_integer([1.1, 2.5, 3.1, 4.9]), 4.9)

    def test_max_floatlist_neg(self):
        """ Test when a list of neg floats is passed """
        self.assertEqual(max_integer([-1.05, -2.2, -3.5, -4.0]), -1.05)

    def test_max_floatlist_mix(self):
        """ Test when a list of neg and pos floats is passed """
        self.assertEqual(max_integer([-1.8, 2.1, 3.6, -4.1]), 3.6)

    def test_max_intfloatlist_mix(self):
        """ Test when a list of neg and pos integers and floats is passed """
        self.assertEqual(max_integer([-1, 2.1, 3, -4.1]), 3)

    def test_max_empty(self):
        """ Test when an empty list function is passed """
        self.assertEqual(max_integer([]), None)

    def test_max_singleint(self):
        """ Test when a single int is passed as list """
        self.assertEqual(max_integer([5]), 5)

    def test_max_singlefloat(self):
        """ Test when a single int is passed as list """
        self.assertEqual(max_integer([5.5]), 5.5)

    def test_max_repeatedint(self):
        """ Test when a single int is passed as list """
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_repeatedfloat(self):
        """ Test when a single int is passed as list """
        self.assertEqual(max_integer([5.5, 5.5, 5.5]), 5.5)

    def test_max_comprenhension(self):
        """ Test when a list is created through comprenhension"""
        self.assertEqual(max_integer([i for i in range(10)]), 9)

    def test_max_intfloattuple_mix(self):
        """ Test when a tuple of neg and pos integers and floats is passed """
        self.assertEqual(max_integer((-1, 2.1, 3, -4.1)), 3)

    def test_max_emptytuple(self):
        """ Test when an empty tuple is passed """
        self.assertEqual(max_integer(()), None)

    def test_max_nolistint(self):
        """ Test when an integer is passed to function """
        with self.assertRaises(TypeError):
            max_integer(2)

    def test_max_nolistfloat(self):
        """ Test when a float is passed to function """
        with self.assertRaises(TypeError):
            max_integer(2.0)

    def test_max_nolistset(self):
        """ Test when a float is passed to function """
        with self.assertRaises(TypeError):
            max_integer({1, 2})

    def test_max_dict(self):
        """ Test when an dictionary with keys in order is passed """
        self.assertEqual(max_integer({0: -3, 1: 1.5, 2: 5}), 5)

    def test_max_nodict(self):
        """ Test when a dict is passed to function with keys not in order """
        with self.assertRaises(KeyError):
            max_integer({1: 2})

    def test_max_emptydict(self):
        """ Test when an empty dictionary is passed """
        self.assertEqual(max_integer(()), None)

    def test_max_matrix(self):
        """ Test when a matrix  dictionary is passed """
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])

    def test_max_char(self):
        """ Test when a list of chars is passed """
        self.assertEqual(max_integer(["1", "2", "a", "4"]), 'a')

    def test_max_str(self):
        """ Test when a string is passed """
        self.assertEqual(max_integer("Holberton"), 't')

    def test_max_liststromt(self):
        """ Test when a list with number and string is passed """
        with self.assertRaises(TypeError):
            max_integer([1, "2"])
