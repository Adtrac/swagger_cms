# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReportInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, player_id: str=None, hours: List[int]=None):  # noqa: E501
        """ReportInner - a model defined in Swagger

        :param id: The id of this ReportInner.  # noqa: E501
        :type id: str
        :param player_id: The player_id of this ReportInner.  # noqa: E501
        :type player_id: str
        :param hours: The hours of this ReportInner.  # noqa: E501
        :type hours: List[int]
        """
        self.swagger_types = {
            'id': str,
            'player_id': str,
            'hours': List[int]
        }

        self.attribute_map = {
            'id': 'id',
            'player_id': 'playerId',
            'hours': 'hours'
        }
        self._id = id
        self._player_id = player_id
        self._hours = hours

    @classmethod
    def from_dict(cls, dikt) -> 'ReportInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Report_inner of this ReportInner.  # noqa: E501
        :rtype: ReportInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ReportInner.


        :return: The id of this ReportInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ReportInner.


        :param id: The id of this ReportInner.
        :type id: str
        """

        self._id = id

    @property
    def player_id(self) -> str:
        """Gets the player_id of this ReportInner.


        :return: The player_id of this ReportInner.
        :rtype: str
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id: str):
        """Sets the player_id of this ReportInner.


        :param player_id: The player_id of this ReportInner.
        :type player_id: str
        """

        self._player_id = player_id

    @property
    def hours(self) -> List[int]:
        """Gets the hours of this ReportInner.


        :return: The hours of this ReportInner.
        :rtype: List[int]
        """
        return self._hours

    @hours.setter
    def hours(self, hours: List[int]):
        """Sets the hours of this ReportInner.


        :param hours: The hours of this ReportInner.
        :type hours: List[int]
        """

        self._hours = hours