# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from node_monitor_agent.test import BaseTestCase


class TestAgentController(BaseTestCase):
    """AgentController integration test stubs"""

    def test_agent_get(self):
        """Test case for agent_get

        Check version
        """
        response = self.client.open(
            '//agent',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_key_get(self):
        """Test case for key_get

        Check key
        """
        response = self.client.open(
            '//key',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        Check ping
        """
        response = self.client.open(
            '//',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
