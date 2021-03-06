# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.opening_hour import OpeningHour  # noqa: F401,E501
from swagger_server import util


class Player(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, player_id: str=None, site_id: str=None, name: str=None, location: str=None, longitude: float=None, latitude: float=None, width: int=None, height: int=None, orientation: str=None, opening_hours: List[OpeningHour]=None):  # noqa: E501
        """Player - a model defined in Swagger

        :param player_id: The player_id of this Player.  # noqa: E501
        :type player_id: str
        :param site_id: The site_id of this Player.  # noqa: E501
        :type site_id: str
        :param name: The name of this Player.  # noqa: E501
        :type name: str
        :param location: The location of this Player.  # noqa: E501
        :type location: str
        :param longitude: The longitude of this Player.  # noqa: E501
        :type longitude: float
        :param latitude: The latitude of this Player.  # noqa: E501
        :type latitude: float
        :param width: The width of this Player.  # noqa: E501
        :type width: int
        :param height: The height of this Player.  # noqa: E501
        :type height: int
        :param orientation: The orientation of this Player.  # noqa: E501
        :type orientation: str
        :param opening_hours: The opening_hours of this Player.  # noqa: E501
        :type opening_hours: List[OpeningHour]
        """
        self.swagger_types = {
            'player_id': str,
            'site_id': str,
            'name': str,
            'location': str,
            'longitude': float,
            'latitude': float,
            'width': int,
            'height': int,
            'orientation': str,
            'opening_hours': List[OpeningHour]
        }

        self.attribute_map = {
            'player_id': 'playerId',
            'site_id': 'siteId',
            'name': 'name',
            'location': 'location',
            'longitude': 'longitude',
            'latitude': 'latitude',
            'width': 'width',
            'height': 'height',
            'orientation': 'orientation',
            'opening_hours': 'openingHours'
        }
        self._player_id = player_id
        self._site_id = site_id
        self._name = name
        self._location = location
        self._longitude = longitude
        self._latitude = latitude
        self._width = width
        self._height = height
        self._orientation = orientation
        self._opening_hours = opening_hours

    @classmethod
    def from_dict(cls, dikt) -> 'Player':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Player of this Player.  # noqa: E501
        :rtype: Player
        """
        return util.deserialize_model(dikt, cls)

    @property
    def player_id(self) -> str:
        """Gets the player_id of this Player.


        :return: The player_id of this Player.
        :rtype: str
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id: str):
        """Sets the player_id of this Player.


        :param player_id: The player_id of this Player.
        :type player_id: str
        """
        if player_id is None:
            raise ValueError("Invalid value for `player_id`, must not be `None`")  # noqa: E501

        self._player_id = player_id

    @property
    def site_id(self) -> str:
        """Gets the site_id of this Player.


        :return: The site_id of this Player.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: str):
        """Sets the site_id of this Player.


        :param site_id: The site_id of this Player.
        :type site_id: str
        """

        self._site_id = site_id

    @property
    def name(self) -> str:
        """Gets the name of this Player.


        :return: The name of this Player.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Player.


        :param name: The name of this Player.
        :type name: str
        """

        self._name = name

    @property
    def location(self) -> str:
        """Gets the location of this Player.


        :return: The location of this Player.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Player.


        :param location: The location of this Player.
        :type location: str
        """

        self._location = location

    @property
    def longitude(self) -> float:
        """Gets the longitude of this Player.


        :return: The longitude of this Player.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this Player.


        :param longitude: The longitude of this Player.
        :type longitude: float
        """

        self._longitude = longitude

    @property
    def latitude(self) -> float:
        """Gets the latitude of this Player.


        :return: The latitude of this Player.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this Player.


        :param latitude: The latitude of this Player.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def width(self) -> int:
        """Gets the width of this Player.


        :return: The width of this Player.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width: int):
        """Sets the width of this Player.


        :param width: The width of this Player.
        :type width: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self) -> int:
        """Gets the height of this Player.


        :return: The height of this Player.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height: int):
        """Sets the height of this Player.


        :param height: The height of this Player.
        :type height: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def orientation(self) -> str:
        """Gets the orientation of this Player.

        Screen orientation  # noqa: E501

        :return: The orientation of this Player.
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation: str):
        """Sets the orientation of this Player.

        Screen orientation  # noqa: E501

        :param orientation: The orientation of this Player.
        :type orientation: str
        """
        allowed_values = ["landscape", "portrait"]  # noqa: E501
        if orientation not in allowed_values:
            raise ValueError(
                "Invalid value for `orientation` ({0}), must be one of {1}"
                .format(orientation, allowed_values)
            )

        self._orientation = orientation

    @property
    def opening_hours(self) -> List[OpeningHour]:
        """Gets the opening_hours of this Player.

        A list of open periods, possibly more than one per weekday  # noqa: E501

        :return: The opening_hours of this Player.
        :rtype: List[OpeningHour]
        """
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, opening_hours: List[OpeningHour]):
        """Sets the opening_hours of this Player.

        A list of open periods, possibly more than one per weekday  # noqa: E501

        :param opening_hours: The opening_hours of this Player.
        :type opening_hours: List[OpeningHour]
        """

        self._opening_hours = opening_hours
