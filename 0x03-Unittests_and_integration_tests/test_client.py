#!/usr/bin/env python3
"""Define Tests for client.py"""
import unittest
import client
import requests
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Represents a test case for GithubOrgClient.
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, domain, mock):
        """Tests GithubOrgClient.org"""
        url = GithubOrgClient(domain)
        url.org()

        mock.assert_called_once_with(url.ORG_URL.format(org=domain))

    def test_public_repos_url(self):
        """Tests GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_property:
            mock_property.return_value = "public url"
            test_inst = GithubOrgClient("org_name")

            self.assertEqual(test_inst._public_repos_url, "public url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """Tests  GithubOrgClient.public_repos"""

        payload = [{"name": "google"}, {"name": "linkedin"}]
        mock_get.return_value = payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos:
            mock_public_repos.return_value = "mocked public url"
            test_instance = GithubOrgClient("test")
            actual = test_instance.public_repos()
            expected = [item["name"] for item in payload]

            self.assertEqual(actual, expected)
            mock_public_repos.assert_called_once()
