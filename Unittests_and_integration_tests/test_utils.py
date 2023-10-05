#!/usr/bin/env python3
""" test module for utils file """


import unittest
import unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ checks for return value """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_path, path, expected):
        """ test nested map access """
        self.assertEqual(access_nested_map(nested_path, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_path, path):
        """ test exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_path, path)


class TestGetJson(unittest.TestCase):
    """ testing getting json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ test json method """
        mock = Mock()
        mock.json.return_value = test_payload
        mock.json.return_value = payload
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()

class TestMemoize(unittest.TestCase):
    """ testing memoizing function """

    def test_memoize(self):
        """ tests callback memoization """
        class TestClass:
            """ test class """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        tester = TestClass()
        with patch.object(tester, "a_method") as mock:
            mock.return_value = 42
            tester.a_property
            tester.a_property
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
