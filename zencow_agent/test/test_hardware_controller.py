# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from zencow_agent.test import BaseTestCase


class TestHardwareController(BaseTestCase):
    """HardwareController integration test stubs"""

    def test_agent_hwid_iron_device_get(self):
        """Test case for agent_hwid_iron_device_get

        return all available groups
        """
        response = self.client.open(
            '/api/agent/{hwid}/iron/{device}'.format(hwid='hwid_example', device='device_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
