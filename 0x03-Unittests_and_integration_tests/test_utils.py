#!/usr/bin/env python3
"""
Unit tests for the utils module.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple,
                                         exception: type) -> None:
        """
        Tests that access_nested_map raises the expected KeyError
        for invalid inputs.
        """
        with self.assertRaises(exception) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json function from utils.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: dict,
                      mock_get: Mock) -> None:
        """
        Tests that get_json returns the expected result and
        requests.get is called once with the correct URL.
        """
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Tests the memoize decorator from utils.
    """
    def test_memoize(self) -> None:
        """
        Tests that a method decorated with memoize returns the correct result
        and the underlying method is called only once.
        """
        class TestClass:
            """
            A test class to demonstrate memoization.
            """
            def a_method(self) -> int:
                """
                A simple method that returns 42.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                A property decorated with memoize.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_method:
            test_object = TestClass()
            self.assertEqual(test_object.a_property, 42)
            self.assertEqual(test_object.a_property, 42)
            mock_a_method.assert_called_once()
