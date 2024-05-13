#!/usr/bin/env python3
"""Define Tests for client.py"""
import unittest
import client
import requests
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


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

