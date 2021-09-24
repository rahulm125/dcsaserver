# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DocumentReferencesInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, document_reference_type: str=None, document_reference_value: str=None):  # noqa: E501
        """DocumentReferencesInner - a model defined in Swagger

        :param document_reference_type: The document_reference_type of this DocumentReferencesInner.  # noqa: E501
        :type document_reference_type: str
        :param document_reference_value: The document_reference_value of this DocumentReferencesInner.  # noqa: E501
        :type document_reference_value: str
        """
        self.swagger_types = {
            'document_reference_type': str,
            'document_reference_value': str
        }

        self.attribute_map = {
            'document_reference_type': 'documentReferenceType',
            'document_reference_value': 'documentReferenceValue'
        }
        self._document_reference_type = document_reference_type
        self._document_reference_value = document_reference_value

    @classmethod
    def from_dict(cls, dikt) -> 'DocumentReferencesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The documentReferences_inner of this DocumentReferencesInner.  # noqa: E501
        :rtype: DocumentReferencesInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def document_reference_type(self) -> str:
        """Gets the document_reference_type of this DocumentReferencesInner.

        Describes where the documentReferenceValue is pointing to  # noqa: E501

        :return: The document_reference_type of this DocumentReferencesInner.
        :rtype: str
        """
        return self._document_reference_type

    @document_reference_type.setter
    def document_reference_type(self, document_reference_type: str):
        """Sets the document_reference_type of this DocumentReferencesInner.

        Describes where the documentReferenceValue is pointing to  # noqa: E501

        :param document_reference_type: The document_reference_type of this DocumentReferencesInner.
        :type document_reference_type: str
        """
        allowed_values = ["BKG (Booking)", "TRD (Transport Document)"]  # noqa: E501
        if document_reference_type not in allowed_values:
            raise ValueError(
                "Invalid value for `document_reference_type` ({0}), must be one of {1}"
                .format(document_reference_type, allowed_values)
            )

        self._document_reference_type = document_reference_type

    @property
    def document_reference_value(self) -> str:
        """Gets the document_reference_value of this DocumentReferencesInner.

        The value of the identifier the documentReferenceType is describing  # noqa: E501

        :return: The document_reference_value of this DocumentReferencesInner.
        :rtype: str
        """
        return self._document_reference_value

    @document_reference_value.setter
    def document_reference_value(self, document_reference_value: str):
        """Sets the document_reference_value of this DocumentReferencesInner.

        The value of the identifier the documentReferenceType is describing  # noqa: E501

        :param document_reference_value: The document_reference_value of this DocumentReferencesInner.
        :type document_reference_value: str
        """

        self._document_reference_value = document_reference_value
