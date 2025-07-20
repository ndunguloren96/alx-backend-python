#!/usr/bin/env python3
"""
Unit tests for the client module.
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
# Assuming fixtures.py content is available or copied here for context
# In a real scenario, you would import these from fixtures.py
# from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


# Manually define fixtures based on typical problem context if import fails
# In a real setup, these would come from fixtures.py
org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
repos_payload = [
    {"name": "episodes.dart", "license": {"key": "apache-2.0"}},
    {"name": "firmata.py", "license": {"key": "apache-2.0"}},
    {"name": "open-location-code", "license": {"key": "apache-2.0"}},
    {"name": "dot-chacha", "license": {"key": "mit"}},
]
expected_repos = [
    "episodes.dart",
    "firmata.py",
    "open-location-code",
    "dot-chacha",
]
apache2_repos = [
    "episodes.dart",
    "firmata.py",
    "open-location-code",
]


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Tests that GithubOrgClient.org returns the correct value
        and get_json is called once with the expected argument.
        """
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, {"login": org_name})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """
        Tests that _public_repos_url returns the expected URL
        based on the mocked org payload.
        """
        expected_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_url}

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Tests that public_repos returns the expected list of repositories
        and that mocked methods are called once.
        """
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = repos_payload

        public_repos_url = "http://example.com/repos"

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = public_repos_url
            client = GithubOrgClient("test_org")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: dict, license_key: str,
                         expected: bool) -> None:
        """
        Tests that GithubOrgClient.has_license returns the expected boolean.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient.public_repos method.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        Sets up class-level mocks for requests.get to simulate API calls.
        """
        config = {
            'return_value.json.side_effect': [
                cls.org_payload,
                cls.repos_payload,
                cls.repos_payload, # For apache2 repos call if it happens
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Stops the patcher after all tests in the class have run.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Tests public_repos method with integration setup.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(
            self.mock_get.call_args_list[0][0][0],
            "https://api.github.com/orgs/google"
        )
        self.assertEqual(
            self.mock_get.call_args_list[1][0][0],
            "https://api.github.com/orgs/google/repos"
        )
        self.assertEqual(self.mock_get.call_count, 2) # Org call + repos call

    def test_public_repos_with_license(self) -> None:
        """
        Tests public_repos method with a license filter.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.assertEqual(
            self.mock_get.call_args_list[0][0][0],
            "https://api.github.com/orgs/google"
        )
        self.assertEqual(
            self.mock_get.call_args_list[1][0][0],
            "https://api.github.com/orgs/google/repos"
        )
        # Note: Depending on caching within client.org and client.repos_payload,
        # the call count might vary. If memoize works as expected, these
        # calls for 'org' and 'repos_payload' should only happen once per instance.
        # For integration, we expect them to be called on first access.
        # The specific call count here depends on whether the `public_repos`
        # method (which calls `repos_payload` which in turn calls `org`)
        # is part of the memoized setup. Given they are memoized, the counts
        # reflect the initial fetch.
        # If test_public_repos runs first, it might consume the first 2 side effects.
        # This test then re-accesses memoized properties.
        # For a clean integration test, it's often better to reset call_count
        # or ensure each test case starts fresh for accurate call count assertion.
        # For this specific setup, we're assuming setUpClass prepares side_effect
        # for multiple possible calls within the parameterized class scope.
        # Resetting mock_get.call_count for each test method:
        self.mock_get.reset_mock() # Reset after previous test if tests are not isolated enough by parameterized_class
        client = GithubOrgClient("google") # Re-instantiate for clean state
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.assertEqual(self.mock_get.call_count, 2) # Should be 2 calls for fresh instance
