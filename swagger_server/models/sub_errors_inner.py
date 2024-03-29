# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SubErrorsInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, reason: str=None, message: str=None):  # noqa: E501
        """SubErrorsInner - a model defined in Swagger

        :param reason: The reason of this SubErrorsInner.  # noqa: E501
        :type reason: str
        :param message: The message of this SubErrorsInner.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'reason': str,
            'message': str
        }

        self.attribute_map = {
            'reason': 'reason',
            'message': 'message'
        }
        self._reason = reason
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'SubErrorsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The subErrors_inner of this SubErrorsInner.  # noqa: E501
        :rtype: SubErrorsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reason(self) -> str:
        """Gets the reason of this SubErrorsInner.

        High level error message.  # noqa: E501

        :return: The reason of this SubErrorsInner.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this SubErrorsInner.

        High level error message.  # noqa: E501

        :param reason: The reason of this SubErrorsInner.
        :type reason: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def message(self) -> str:
        """Gets the message of this SubErrorsInner.

        Detailed error message.  # noqa: E501

        :return: The message of this SubErrorsInner.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SubErrorsInner.

        Detailed error message.  # noqa: E501

        :param message: The message of this SubErrorsInner.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
