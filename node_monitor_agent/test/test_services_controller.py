# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from node_monitor_agent.test import BaseTestCase


class TestServicesController(BaseTestCase):
    """ServicesController integration test stubs"""

    def test_service_service_call_get(self):
        """Test case for service_service_call_get

        check service status
        """
        response = self.client.open(
            '//service/{service}/{call}'.format(service='service_example', call='call_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_service_service_get(self):
        """Test case for service_service_get

        check service status
        """
        response = self.client.open(
            '//service/{service}'.format(service='service_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
