#!/usr/bin/env python3
"""Defines a test case using parameterized"""
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize
import unittest
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Represents a test case for utils.access_nested_map.
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


class TestGetJson(unittest.TestCase):
    """Represents a test case for utils.get_json.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests get_json"""
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Represents a test case for utils.memoize.
    """

    def test_memoize(self):
        """Tests memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            instance = TestClass()
            instance.a_property()
            instance.a_property()

            mock_method.assert_called_once()
