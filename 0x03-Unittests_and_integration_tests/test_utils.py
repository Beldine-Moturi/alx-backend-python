#!/usr/bin/env python3
"""Contains tests for functions in the module utils"""
from unittest.mock import patch, Mock
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Tests access_nested_map function in utils.py"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """tests that access_nested_map works as intended"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """Tests exception raised in access nested map function"""
        self.assertRaises(expected, access_nested_map, map, path)


class TestGetJson(unittest.TestCase):
    """Tests the get json function in utils.py"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, url, return_json, mock_requests):
        """Tests that get_json returns the expected result"""

        mock_response = Mock()
        mock_response.json.return_value = return_json

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(url), return_json)
        mock_requests.get.assert_called_once_with(url)
