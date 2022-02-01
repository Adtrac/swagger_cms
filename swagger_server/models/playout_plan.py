# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.playout_plan_playouts import PlayoutPlanPlayouts  # noqa: F401,E501
from swagger_server import util


class PlayoutPlan(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, playouts: List[PlayoutPlanPlayouts]=None):  # noqa: E501
        """PlayoutPlan - a model defined in Swagger

        :param playouts: The playouts of this PlayoutPlan.  # noqa: E501
        :type playouts: List[PlayoutPlanPlayouts]
        """
        self.swagger_types = {
            'playouts': List[PlayoutPlanPlayouts]
        }

        self.attribute_map = {
            'playouts': 'playouts'
        }
        self._playouts = playouts

    @classmethod
    def from_dict(cls, dikt) -> 'PlayoutPlan':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PlayoutPlan of this PlayoutPlan.  # noqa: E501
        :rtype: PlayoutPlan
        """
        return util.deserialize_model(dikt, cls)

    @property
    def playouts(self) -> List[PlayoutPlanPlayouts]:
        """Gets the playouts of this PlayoutPlan.


        :return: The playouts of this PlayoutPlan.
        :rtype: List[PlayoutPlanPlayouts]
        """
        return self._playouts

    @playouts.setter
    def playouts(self, playouts: List[PlayoutPlanPlayouts]):
        """Sets the playouts of this PlayoutPlan.


        :param playouts: The playouts of this PlayoutPlan.
        :type playouts: List[PlayoutPlanPlayouts]
        """

        self._playouts = playouts
