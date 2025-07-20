#!/usr/bin/env python3
"""
Unit tests for the utils module.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function from utils.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               expected: any) -> None:
        """
        Tests that access_nested_map returns the expected result
        for valid inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
