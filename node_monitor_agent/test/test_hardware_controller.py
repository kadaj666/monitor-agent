# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from node_monitor_agent.test import BaseTestCase


class TestHardwareController(BaseTestCase):
    """HardwareController integration test stubs"""

    def test_cpu_detail_get(self):
        """Test case for cpu_detail_get

        check cpu information
        """
        response = self.client.open(
            '//cpu/{detail}'.format(detail='detail_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disk_detail_get(self):
        """Test case for disk_detail_get

        check cpu information
        """
        response = self.client.open(
            '//disk/{detail}'.format(detail='detail_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mem_detail_get(self):
        """Test case for mem_detail_get

        check cpu information
        """
        response = self.client.open(
            '//mem/{detail}'.format(detail='detail_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_net_detail_get(self):
        """Test case for net_detail_get

        check cpu information
        """
        response = self.client.open(
            '//net/{detail}'.format(detail='detail_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
