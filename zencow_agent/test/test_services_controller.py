# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from zencow_agent.test import BaseTestCase


class TestServicesController(BaseTestCase):
    """ServicesController integration test stubs"""

    def test_agent_hwid_services_service_get(self):
        """Test case for agent_hwid_services_service_get

        return all available groups
        """
        response = self.client.open(
            '/api/agent/{hwid}/services/{service}'.format(hwid='hwid_example', service='service_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
