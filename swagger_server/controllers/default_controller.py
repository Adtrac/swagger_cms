import uuid

import connexion
import six

from swagger_server.services import service
from swagger_server.models.asset import Asset  # noqa: E501
from swagger_server.models.assets import Assets  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.player_state import PlayerState  # noqa: E501
from swagger_server.models.players import Players  # noqa: E501
from swagger_server.models.playout_plan import PlayoutPlan  # noqa: E501
from swagger_server.models.report import Report  # noqa: E501
from swagger_server import util


def assets_get():  # noqa: E501
    """List all asset metadata

    Retrieve the list of all asset metadata # noqa: E501


    :rtype: Assets
    """
    return service.get_assets()


# For whatever reason _metadata is not populated from the formdata part of the request
def assets_post(_metadata=None, content=None):  # noqa: E501
    """Upload a media file

    Upload a media file # noqa: E501

    :param _metadata:
    :type _metadata: dict | bytes
    :param content: 
    :type content: strstr

    :rtype: Asset
    """
    if connexion.request.is_json:
        metadata = object.from_dict(connexion.request.get_json())  # noqa: E501

    _metadata = {"a": "b"}
    asset_id = service.create_asset(content, _metadata)
    return Asset(asset_id, _metadata)


def players_get():  # noqa: E501
    """List all players

    Returns a list of player records # noqa: E501


    :rtype: Players
    """
    return 'do some magic!'


def players_player_id_get(player_id):  # noqa: E501
    """Retrieve a single player&#x27;s record

    Returns a player record # noqa: E501

    :param player_id: ID of player to return
    :type player_id: str

    :rtype: Player
    """
    return 'do some magic!'


def players_player_id_healthcheck_get(player_id):  # noqa: E501
    """Retrieve a single player&#x27;s heartbeat

    Returns a player state # noqa: E501

    :param player_id: ID of player to health-check
    :type player_id: str

    :rtype: PlayerState
    """
    return 'do some magic!'


def playouts_date_post(date, body=None):  # noqa: E501
    """Submit the playout plan for the entire day

     # noqa: E501

    :param _date: Playout plan will be executed on this day.
    :type _date: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    date = util.deserialize_date(date)
    if connexion.request.is_json:
        body = PlayoutPlan.from_dict(connexion.request.get_json())  # noqa: E501

    service.create_playout(date, body)
    return 'OK'


def reports_date_get(_date):  # noqa: E501
    """Retrieve the given day&#x27;s playout report

    Returns a list of asset records (not the media files themselves!) # noqa: E501

    :param _date: date for which to retrieve the playout reports
    :type _date: str

    :rtype: Report
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'
