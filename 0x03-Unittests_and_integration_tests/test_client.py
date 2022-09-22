#!/usr/bin/env python3
"""Contains tests for functions in the module client"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests that GithubOrgClient.org returns the correct value"""

        url = f"https://api.github.com/orgs/{org_name}"
        spec = GithubOrgClient(org_name)
        spec.org()
        mock_get_json.assert_called_once_with(url)
    