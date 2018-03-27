# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from node_monitor_agent.test import BaseTestCase


class TestOsController(BaseTestCase):
    """OsController integration test stubs"""

    def test_boot_time_get(self):
        """Test case for boot_time_get

        check node boot time
        """
        response = self.client.open(
            '//boot_time',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_distr_get(self):
        """Test case for distr_get

        Check distribution type
        """
        response = self.client.open(
            '//distr',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hostname_get(self):
        """Test case for hostname_get

        Check hostname
        """
        response = self.client.open(
            '//hostname',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_la_get(self):
        """Test case for la_get

        check LA value
        """
        response = self.client.open(
            '//la',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_python_get(self):
        """Test case for python_get

        Check python version
        """
        response = self.client.open(
            '//python',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_top5cpu_get(self):
        """Test case for top5cpu_get

        Check top 5 process by cpu 
        """
        response = self.client.open(
            '//top5cpu',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_top5io_get(self):
        """Test case for top5io_get

        Check top 5 process by I/O 
        """
        response = self.client.open(
            '//top5io',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_top5mem_get(self):
        """Test case for top5mem_get

        Check top 5 process by mem 
        """
        response = self.client.open(
            '//top5mem',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
