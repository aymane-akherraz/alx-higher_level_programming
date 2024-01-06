#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defines a TestMaxInteger class """
    def test_one_el_list(self):
        """ Test with a list with one integer """
        self.assertEqual(max_integer([20]), 20)

    def test_same_el_list(self):
        """ Test with a list with the same integer """
        self.assertEqual(max_integer([10, 10, 10, 10, 10]), 10)

    def test_int_list(self):
        """ Test with a list of integers """
        self.assertEqual(max_integer([3, -6, 0, 7, 23, -8]), 23)

    def test_negative_int_list(self):
        """ Test with a list of negative integers """
        self.assertEqual(max_integer([-4, -2, -3, -10, -1, -100]), -1)

    def test_positive_int_list(self):
        """ Test with a list of positive integers """
        self.assertEqual(max_integer([3, 20, 3, 1, 1, 50]), 50)

    def test_float_list(self):
        """ Test with a list of floats """
        self.assertEqual(max_integer([2.33, -4.3, 2.9, -30.9]), 2.9)

    def test_negative_float_list(self):
        """ Test with a list of negative floats """
        self.assertEqual(max_integer([-4.7, -2.3, -1.0, -6.1, -1.55]), -1.0)

    def test_positive_float_list(self):
        """ Test with a list of positive floats """
        self.assertEqual(max_integer([3.4, 2.0, 4.3, 1.1, 11.5, 0.30]), 11.5)

    def test_str_list(self):
        """ Test with a list of strings """
        self.assertEqual(max_integer(["aa", "dd", "aa", "cc"]), "dd")

    def test_with_None(self):
        """ Test with None as arg """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        """ Test with an empty list (which is passed by default)"""
        self.assertEqual(max_integer(), None)

    def test_mixed_list(self):
        """ Test with a list of mixed types """
        with self.assertRaises(TypeError):
            max_integer([1, "hello", None, 20, 3.4, [], {"key", "value"}])

    def test_nested_lists(self):
        """ Test with a list of lists of numbers """
        self.assertEqual(max_integer([[10], [], [8.2, 9], [3], [7], [0.5]]),
                         [10])

    def test_nested_mixed_list(self):
        """ Test with a list of lists of mixed types """
        with self.assertRaises(TypeError):
            max_integer([[10], ["Hi"], [8.2, 9], [3, [None]], [7], [{"k": 3}]])

    def test_int_arg(self):
        """ Test with a int as argument """
        with self.assertRaises(TypeError):
            max_integer(13)

    def test_float_arg(self):
        """ Test with a float as argument """
        with self.assertRaises(TypeError):
            max_integer(1.3)

    def test_nan_list(self):
        """ Test with nan values """
        self.assertEqual(max_integer([9, 8.9, float('nan'), 10, float('nan')]),
                         10)
