#!/usr/bin/env python3
""" tests the GithubOrgClient class """


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient Class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """ Test org method """
        mock_get_json.return_value = {"payload": True}
        test_class = GithubOrgClient(test_org_name)
        self.assertEqual(test_class.org, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_url(self, mock):
        """ test _public_repos_url method """
        test_class = GithubOrgClient("google")
        mock.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        self.assertEqual(
            test_class._public_repos_url,
            mock.return_value.get("repos_url")
        )


if __name__ == "__main__":
    unittest.main()
