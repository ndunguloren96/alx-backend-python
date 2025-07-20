#!/usr/bin/env python3
"""
Unit tests for the client module.
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Tests that public_repos returns the expected list of repositories
        and that mocked methods are called once.
        """
        repos_payload_mock = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = repos_payload_mock

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
        # Create a dictionary to map URLs to their corresponding payloads
        cls.get_payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            cls.org_payload["repos_url"]: cls.repos_payload,
        }

        def mock_get_json_side_effect(url: str) -> Mock:
            """
            Custom side effect for requests.get() to return
            different mock responses based on the URL.
            """
            mock_response = Mock()
            # Ensure .json() is called on the response and returns the payload
            mock_response.json.return_value = cls.get_payloads[url]
            return mock_response

        cls.get_patcher = patch('requests.get',
                                side_effect=mock_get_json_side_effect)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Stops the patcher after all tests in the class have run.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Tests public_repos method without a license filter,
        ensuring it returns the expected repositories and
        makes the correct API calls.
        """
        # Reset mock calls for each test method to ensure accurate counting
        self.mock_get.reset_mock()

        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

        # Verify calls
        expected_calls = [
            unittest.mock.call("https://api.github.com/orgs/google"),
            unittest.mock.call(self.org_payload["repos_url"])
        ]
        self.mock_get.assert_has_calls(expected_calls)
        self.assertEqual(self.mock_get.call_count, 2)

    def test_public_repos_with_license(self) -> None:
        """
        Tests public_repos method with a license filter,
        ensuring it returns the expected repositories and
        makes the correct API calls.
        """
        # Reset mock calls for each test method to ensure accurate counting
        self.mock_get.reset_mock()

        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

        # Verify calls (should be the same as without license, as has_license
        # is static and does not trigger new API calls)
        expected_calls = [
            unittest.mock.call("https://api.github.com/orgs/google"),
            unittest.mock.call(self.org_payload["repos_url"])
        ]
        self.mock_get.assert_has_calls(expected_calls)
        self.assertEqual(self.mock_get.call_count, 2)
