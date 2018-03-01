# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from zencow_agent.test import BaseTestCase


class TestVersionController(BaseTestCase):
    """VersionController integration test stubs"""

    def test_agent_hwid_version_service_user_get(self):
        """Test case for agent_hwid_version_service_user_get

        return all available groups
        """
        response = self.client.open(
            '/api/agent/{hwid}/version/{service}/{user}'.format(hwid='hwid_example', service='service_example', user='user_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
