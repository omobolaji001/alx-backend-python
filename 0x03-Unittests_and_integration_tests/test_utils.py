#!/usr/bin/env python3
"""Defines a test case using parameterized"""
from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Represents a test case for access_nested_map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map"""
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests access_nested_map for exception cases"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
