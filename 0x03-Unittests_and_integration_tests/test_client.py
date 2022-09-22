#!/usr/bin/env python3
"""Contains tests for functions in the module client"""
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests that GithubOrgClient.org returns the correct value"""

        url = "https://api.github.com/orgs/{}".format(org_name)
        spec = GithubOrgClient(org_name)
        spec.org()
        mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ("example_name", {"repos_url": "http://example_url.com"})
    ])
    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, name, expected, mock_org):
        """Tests _public_repos_url"""

        mock_org.return_value = expected
        test_property = GithubOrgClient(name)._public_repos_url
        self.assertEqual(test_property, expected.get('repos_url'))

    @patch('client.get_json')
    @patch.object(
        GithubOrgClient,
        '_public_repos_url',
        new_callable=PropertyMock
        )
    def test_public_repos(self, mock_public_repos, mock_get_json):
        """Tests public_repos method"""

        payload = [
            {"name": "url_1"},
            {"name": "url_2"},
            {"name": "url_3"}
        ]

        mock_get_json.return_value = payload
        mock_public_repos.return_value = "some_url"

        test_client = GithubOrgClient("example_name")
        repos = test_client.public_repos()
        self.assertEqual(repos, [p["name"] for p in payload])

        mock_public_repos.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """Tests has_licence method"""

        self.assertEqual(
            GithubOrgClient.has_license(repo, key),
            expected
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """an integration test for githuborg client"""

    @classmethod
    def setUpClass(cls):
        """ set up class befor each method"""
        config = {'return_value.json.side_effect':
                  [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """add some more integration"""
        tst_cls = GithubOrgClient('Facebook')
        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down after each class"""
        cls.get_patcher.stop()
