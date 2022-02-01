# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.asset import Asset  # noqa: E501
from swagger_server.models.assets import Assets  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.player_state import PlayerState  # noqa: E501
from swagger_server.models.players import Players  # noqa: E501
from swagger_server.models.playout_plan import PlayoutPlan  # noqa: E501
from swagger_server.models.report import Report  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_assets_get(self):
        """Test case for assets_get

        List all asset metadata
        """
        response = self.client.open(
            'localhost:8080/api/v10/assets',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assets_post(self):
        """Test case for assets_post

        Upload a media file
        """
        data = dict(metadata=None,
                    content='content_example')
        response = self.client.open(
            'localhost:8080/api/v10/assets',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_players_get(self):
        """Test case for players_get

        List all players
        """
        response = self.client.open(
            'localhost:8080/api/v10/players',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_players_player_id_get(self):
        """Test case for players_player_id_get

        Retrieve a single player's record
        """
        response = self.client.open(
            'localhost:8080/api/v10/players/{playerId}'.format(player_id='player_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_players_player_id_healthcheck_get(self):
        """Test case for players_player_id_healthcheck_get

        Retrieve a single player's heartbeat
        """
        response = self.client.open(
            'localhost:8080/api/v10/players/{playerId}/healthcheck'.format(player_id='player_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playouts_date_post(self):
        """Test case for playouts_date_post

        Submit the playout plan for the entire day
        """
        body = PlayoutPlan()
        response = self.client.open(
            'localhost:8080/api/v10/playouts/{date}'.format(_date='2013-10-20'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reports_date_get(self):
        """Test case for reports_date_get

        Retrieve the given day's playout report
        """
        response = self.client.open(
            'localhost:8080/api/v10/reports/{date}'.format(_date='2013-10-20'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
