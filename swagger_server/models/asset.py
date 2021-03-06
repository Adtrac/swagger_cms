# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Asset(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, metadata: object=None):  # noqa: E501
        """Asset - a model defined in Swagger

        :param id: The id of this Asset.  # noqa: E501
        :type id: str
        :param metadata: The metadata of this Asset.  # noqa: E501
        :type metadata: object
        """
        self.swagger_types = {
            'id': str,
            'metadata': object
        }

        self.attribute_map = {
            'id': 'id',
            'metadata': 'metadata'
        }
        self._id = id
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'Asset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Asset of this Asset.  # noqa: E501
        :rtype: Asset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Asset.


        :return: The id of this Asset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Asset.


        :param id: The id of this Asset.
        :type id: str
        """

        self._id = id

    @property
    def metadata(self) -> object:
        """Gets the metadata of this Asset.


        :return: The metadata of this Asset.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this Asset.


        :param metadata: The metadata of this Asset.
        :type metadata: object
        """

        self._metadata = metadata
