# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.carrier_booking_reference import CarrierBookingReference  # noqa: F401,E501
from swagger_server.models.transport_document_reference import TransportDocumentReference  # noqa: F401,E501
from swagger_server.models.transport_document_type_codes import TransportDocumentTypeCodes  # noqa: F401,E501
from swagger_server import util


class ShipmentSubscriptionBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, carrier_booking_reference: CarrierBookingReference=None, booking_reference: str=None, transport_document_id: str=None, transport_document_reference: TransportDocumentReference=None, transport_document_type_code: TransportDocumentTypeCodes=None):  # noqa: E501
        """ShipmentSubscriptionBody - a model defined in Swagger

        :param carrier_booking_reference: The carrier_booking_reference of this ShipmentSubscriptionBody.  # noqa: E501
        :type carrier_booking_reference: CarrierBookingReference
        :param booking_reference: The booking_reference of this ShipmentSubscriptionBody.  # noqa: E501
        :type booking_reference: str
        :param transport_document_id: The transport_document_id of this ShipmentSubscriptionBody.  # noqa: E501
        :type transport_document_id: str
        :param transport_document_reference: The transport_document_reference of this ShipmentSubscriptionBody.  # noqa: E501
        :type transport_document_reference: TransportDocumentReference
        :param transport_document_type_code: The transport_document_type_code of this ShipmentSubscriptionBody.  # noqa: E501
        :type transport_document_type_code: TransportDocumentTypeCodes
        """
        self.swagger_types = {
            'carrier_booking_reference': CarrierBookingReference,
            'booking_reference': str,
            'transport_document_id': str,
            'transport_document_reference': TransportDocumentReference,
            'transport_document_type_code': TransportDocumentTypeCodes
        }

        self.attribute_map = {
            'carrier_booking_reference': 'carrierBookingReference',
            'booking_reference': 'bookingReference',
            'transport_document_id': 'transportDocumentID',
            'transport_document_reference': 'transportDocumentReference',
            'transport_document_type_code': 'transportDocumentTypeCode'
        }
        self._carrier_booking_reference = carrier_booking_reference
        self._booking_reference = booking_reference
        self._transport_document_id = transport_document_id
        self._transport_document_reference = transport_document_reference
        self._transport_document_type_code = transport_document_type_code

    @classmethod
    def from_dict(cls, dikt) -> 'ShipmentSubscriptionBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The shipmentSubscriptionBody of this ShipmentSubscriptionBody.  # noqa: E501
        :rtype: ShipmentSubscriptionBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def carrier_booking_reference(self) -> CarrierBookingReference:
        """Gets the carrier_booking_reference of this ShipmentSubscriptionBody.


        :return: The carrier_booking_reference of this ShipmentSubscriptionBody.
        :rtype: CarrierBookingReference
        """
        return self._carrier_booking_reference

    @carrier_booking_reference.setter
    def carrier_booking_reference(self, carrier_booking_reference: CarrierBookingReference):
        """Sets the carrier_booking_reference of this ShipmentSubscriptionBody.


        :param carrier_booking_reference: The carrier_booking_reference of this ShipmentSubscriptionBody.
        :type carrier_booking_reference: CarrierBookingReference
        """

        self._carrier_booking_reference = carrier_booking_reference

    @property
    def booking_reference(self) -> str:
        """Gets the booking_reference of this ShipmentSubscriptionBody.

        The identifier for a shipment, which is issued by and unique within each of the carriers.  Deprecated - use carrierBookingReference instead   # noqa: E501

        :return: The booking_reference of this ShipmentSubscriptionBody.
        :rtype: str
        """
        return self._booking_reference

    @booking_reference.setter
    def booking_reference(self, booking_reference: str):
        """Sets the booking_reference of this ShipmentSubscriptionBody.

        The identifier for a shipment, which is issued by and unique within each of the carriers.  Deprecated - use carrierBookingReference instead   # noqa: E501

        :param booking_reference: The booking_reference of this ShipmentSubscriptionBody.
        :type booking_reference: str
        """

        self._booking_reference = booking_reference

    @property
    def transport_document_id(self) -> str:
        """Gets the transport_document_id of this ShipmentSubscriptionBody.

        Uniquely identify a transport document.  Deprecated - use transportDocumentReference instead   # noqa: E501

        :return: The transport_document_id of this ShipmentSubscriptionBody.
        :rtype: str
        """
        return self._transport_document_id

    @transport_document_id.setter
    def transport_document_id(self, transport_document_id: str):
        """Sets the transport_document_id of this ShipmentSubscriptionBody.

        Uniquely identify a transport document.  Deprecated - use transportDocumentReference instead   # noqa: E501

        :param transport_document_id: The transport_document_id of this ShipmentSubscriptionBody.
        :type transport_document_id: str
        """

        self._transport_document_id = transport_document_id

    @property
    def transport_document_reference(self) -> TransportDocumentReference:
        """Gets the transport_document_reference of this ShipmentSubscriptionBody.


        :return: The transport_document_reference of this ShipmentSubscriptionBody.
        :rtype: TransportDocumentReference
        """
        return self._transport_document_reference

    @transport_document_reference.setter
    def transport_document_reference(self, transport_document_reference: TransportDocumentReference):
        """Sets the transport_document_reference of this ShipmentSubscriptionBody.


        :param transport_document_reference: The transport_document_reference of this ShipmentSubscriptionBody.
        :type transport_document_reference: TransportDocumentReference
        """

        self._transport_document_reference = transport_document_reference

    @property
    def transport_document_type_code(self) -> TransportDocumentTypeCodes:
        """Gets the transport_document_type_code of this ShipmentSubscriptionBody.


        :return: The transport_document_type_code of this ShipmentSubscriptionBody.
        :rtype: TransportDocumentTypeCodes
        """
        return self._transport_document_type_code

    @transport_document_type_code.setter
    def transport_document_type_code(self, transport_document_type_code: TransportDocumentTypeCodes):
        """Sets the transport_document_type_code of this ShipmentSubscriptionBody.


        :param transport_document_type_code: The transport_document_type_code of this ShipmentSubscriptionBody.
        :type transport_document_type_code: TransportDocumentTypeCodes
        """

        self._transport_document_type_code = transport_document_type_code