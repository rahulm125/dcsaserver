# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.error import Error  # noqa: F401,E501
from swagger_server.models.sub_errors import SubErrors  # noqa: F401,E501
from swagger_server import util


class InlineResponseDefault(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, http_method: Object=None, request_uri: Object=None, errors: SubErrors=None, status_code: int=None, status_code_text: str=None, error_date_time: str=None):  # noqa: E501
        """InlineResponseDefault - a model defined in Swagger

        :param http_method: The http_method of this InlineResponseDefault.  # noqa: E501
        :type http_method: Object
        :param request_uri: The request_uri of this InlineResponseDefault.  # noqa: E501
        :type request_uri: Object
        :param errors: The errors of this InlineResponseDefault.  # noqa: E501
        :type errors: SubErrors
        :param status_code: The status_code of this InlineResponseDefault.  # noqa: E501
        :type status_code: int
        :param status_code_text: The status_code_text of this InlineResponseDefault.  # noqa: E501
        :type status_code_text: str
        :param error_date_time: The error_date_time of this InlineResponseDefault.  # noqa: E501
        :type error_date_time: str
        """
        self.swagger_types = {
            'http_method': Object,
            'request_uri': Object,
            'errors': SubErrors,
            'status_code': int,
            'status_code_text': str,
            'error_date_time': str
        }

        self.attribute_map = {
            'http_method': 'httpMethod',
            'request_uri': 'requestUri',
            'errors': 'errors',
            'status_code': 'statusCode',
            'status_code_text': 'statusCodeText',
            'error_date_time': 'errorDateTime'
        }
        self._http_method = http_method
        self._request_uri = request_uri
        self._errors = errors
        self._status_code = status_code
        self._status_code_text = status_code_text
        self._error_date_time = error_date_time

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponseDefault':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_default of this InlineResponseDefault.  # noqa: E501
        :rtype: InlineResponseDefault
        """
        return util.deserialize_model(dikt, cls)

    @property
    def http_method(self) -> Object:
        """Gets the http_method of this InlineResponseDefault.


        :return: The http_method of this InlineResponseDefault.
        :rtype: Object
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method: Object):
        """Sets the http_method of this InlineResponseDefault.


        :param http_method: The http_method of this InlineResponseDefault.
        :type http_method: Object
        """
        if http_method is None:
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501

        self._http_method = http_method

    @property
    def request_uri(self) -> Object:
        """Gets the request_uri of this InlineResponseDefault.


        :return: The request_uri of this InlineResponseDefault.
        :rtype: Object
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri: Object):
        """Sets the request_uri of this InlineResponseDefault.


        :param request_uri: The request_uri of this InlineResponseDefault.
        :type request_uri: Object
        """
        if request_uri is None:
            raise ValueError("Invalid value for `request_uri`, must not be `None`")  # noqa: E501

        self._request_uri = request_uri

    @property
    def errors(self) -> SubErrors:
        """Gets the errors of this InlineResponseDefault.


        :return: The errors of this InlineResponseDefault.
        :rtype: SubErrors
        """
        return self._errors

    @errors.setter
    def errors(self, errors: SubErrors):
        """Sets the errors of this InlineResponseDefault.


        :param errors: The errors of this InlineResponseDefault.
        :type errors: SubErrors
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def status_code(self) -> int:
        """Gets the status_code of this InlineResponseDefault.

        The HTTP status code  # noqa: E501

        :return: The status_code of this InlineResponseDefault.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int):
        """Sets the status_code of this InlineResponseDefault.

        The HTTP status code  # noqa: E501

        :param status_code: The status_code of this InlineResponseDefault.
        :type status_code: int
        """
        if status_code is None:
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501

        self._status_code = status_code

    @property
    def status_code_text(self) -> str:
        """Gets the status_code_text of this InlineResponseDefault.

        The textual representation of the response status.  # noqa: E501

        :return: The status_code_text of this InlineResponseDefault.
        :rtype: str
        """
        return self._status_code_text

    @status_code_text.setter
    def status_code_text(self, status_code_text: str):
        """Sets the status_code_text of this InlineResponseDefault.

        The textual representation of the response status.  # noqa: E501

        :param status_code_text: The status_code_text of this InlineResponseDefault.
        :type status_code_text: str
        """
        if status_code_text is None:
            raise ValueError("Invalid value for `status_code_text`, must not be `None`")  # noqa: E501

        self._status_code_text = status_code_text

    @property
    def error_date_time(self) -> str:
        """Gets the error_date_time of this InlineResponseDefault.

        The date and time (in ISO 8601 format) the error occurred.  # noqa: E501

        :return: The error_date_time of this InlineResponseDefault.
        :rtype: str
        """
        return self._error_date_time

    @error_date_time.setter
    def error_date_time(self, error_date_time: str):
        """Sets the error_date_time of this InlineResponseDefault.

        The date and time (in ISO 8601 format) the error occurred.  # noqa: E501

        :param error_date_time: The error_date_time of this InlineResponseDefault.
        :type error_date_time: str
        """
        if error_date_time is None:
            raise ValueError("Invalid value for `error_date_time`, must not be `None`")  # noqa: E501

        self._error_date_time = error_date_time
