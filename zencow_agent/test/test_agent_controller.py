# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from zencow_agent.test import BaseTestCase


class TestAgentController(BaseTestCase):
    """AgentController integration test stubs"""

    def test_agent_get(self):
        """Test case for agent_get

        Check ping
        """
        response = self.client.open(
            '/api/agent',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_agent_hwid_get(self):
        """Test case for agent_hwid_get

        Check access
        """
        response = self.client.open(
            '/api/agent/{hwid}'.format(hwid='hwid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
