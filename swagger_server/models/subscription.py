# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.carrier_booking_reference import CarrierBookingReference  # noqa: F401,E501
from swagger_server.models.equipment_reference import EquipmentReference  # noqa: F401,E501
from swagger_server.models.event_types import EventTypes  # noqa: F401,E501
from swagger_server.models.subscription_body import SubscriptionBody  # noqa: F401,E501
from swagger_server.models.transport_document_reference import TransportDocumentReference  # noqa: F401,E501
from swagger_server.models.transport_document_type_codes import TransportDocumentTypeCodes  # noqa: F401,E501
from swagger_server import util


class Subscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, event_type: EventTypes=None, carrier_booking_reference: CarrierBookingReference=None, booking_reference: str=None, transport_document_id: str=None, transport_document_reference: TransportDocumentReference=None, transport_document_type_code: TransportDocumentTypeCodes=None, schedule_id: Object=None, equipment_reference: EquipmentReference=None):  # noqa: E501
        """Subscription - a model defined in Swagger

        :param event_type: The event_type of this Subscription.  # noqa: E501
        :type event_type: EventTypes
        :param carrier_booking_reference: The carrier_booking_reference of this Subscription.  # noqa: E501
        :type carrier_booking_reference: CarrierBookingReference
        :param booking_reference: The booking_reference of this Subscription.  # noqa: E501
        :type booking_reference: str
        :param transport_document_id: The transport_document_id of this Subscription.  # noqa: E501
        :type transport_document_id: str
        :param transport_document_reference: The transport_document_reference of this Subscription.  # noqa: E501
        :type transport_document_reference: TransportDocumentReference
        :param transport_document_type_code: The transport_document_type_code of this Subscription.  # noqa: E501
        :type transport_document_type_code: TransportDocumentTypeCodes
        :param schedule_id: The schedule_id of this Subscription.  # noqa: E501
        :type schedule_id: Object
        :param equipment_reference: The equipment_reference of this Subscription.  # noqa: E501
        :type equipment_reference: EquipmentReference
        """
        self.swagger_types = {
            'event_type': EventTypes,
            'carrier_booking_reference': CarrierBookingReference,
            'booking_reference': str,
            'transport_document_id': str,
            'transport_document_reference': TransportDocumentReference,
            'transport_document_type_code': TransportDocumentTypeCodes,
            'schedule_id': Object,
            'equipment_reference': EquipmentReference
        }

        self.attribute_map = {
            'event_type': 'eventType',
            'carrier_booking_reference': 'carrierBookingReference',
            'booking_reference': 'bookingReference',
            'transport_document_id': 'transportDocumentID',
            'transport_document_reference': 'transportDocumentReference',
            'transport_document_type_code': 'transportDocumentTypeCode',
            'schedule_id': 'scheduleID',
            'equipment_reference': 'equipmentReference'
        }
        self._event_type = event_type
        self._carrier_booking_reference = carrier_booking_reference
        self._booking_reference = booking_reference
        self._transport_document_id = transport_document_id
        self._transport_document_reference = transport_document_reference
        self._transport_document_type_code = transport_document_type_code
        self._schedule_id = schedule_id
        self._equipment_reference = equipment_reference

    @classmethod
    def from_dict(cls, dikt) -> 'Subscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The subscription of this Subscription.  # noqa: E501
        :rtype: Subscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_type(self) -> EventTypes:
        """Gets the event_type of this Subscription.


        :return: The event_type of this Subscription.
        :rtype: EventTypes
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: EventTypes):
        """Sets the event_type of this Subscription.


        :param event_type: The event_type of this Subscription.
        :type event_type: EventTypes
        """

        self._event_type = event_type

    @property
    def carrier_booking_reference(self) -> CarrierBookingReference:
        """Gets the carrier_booking_reference of this Subscription.


        :return: The carrier_booking_reference of this Subscription.
        :rtype: CarrierBookingReference
        """
        return self._carrier_booking_reference

    @carrier_booking_reference.setter
    def carrier_booking_reference(self, carrier_booking_reference: CarrierBookingReference):
        """Sets the carrier_booking_reference of this Subscription.


        :param carrier_booking_reference: The carrier_booking_reference of this Subscription.
        :type carrier_booking_reference: CarrierBookingReference
        """

        self._carrier_booking_reference = carrier_booking_reference

    @property
    def booking_reference(self) -> str:
        """Gets the booking_reference of this Subscription.

        The identifier for a shipment, which is issued by and unique within each of the carriers.  Deprecated - use carrierBookingReference instead   # noqa: E501

        :return: The booking_reference of this Subscription.
        :rtype: str
        """
        return self._booking_reference

    @booking_reference.setter
    def booking_reference(self, booking_reference: str):
        """Sets the booking_reference of this Subscription.

        The identifier for a shipment, which is issued by and unique within each of the carriers.  Deprecated - use carrierBookingReference instead   # noqa: E501

        :param booking_reference: The booking_reference of this Subscription.
        :type booking_reference: str
        """

        self._booking_reference = booking_reference

    @property
    def transport_document_id(self) -> str:
        """Gets the transport_document_id of this Subscription.

        Uniquely identify a transport document.  Deprecated - use transportDocumentReference instead   # noqa: E501

        :return: The transport_document_id of this Subscription.
        :rtype: str
        """
        return self._transport_document_id

    @transport_document_id.setter
    def transport_document_id(self, transport_document_id: str):
        """Sets the transport_document_id of this Subscription.

        Uniquely identify a transport document.  Deprecated - use transportDocumentReference instead   # noqa: E501

        :param transport_document_id: The transport_document_id of this Subscription.
        :type transport_document_id: str
        """

        self._transport_document_id = transport_document_id

    @property
    def transport_document_reference(self) -> TransportDocumentReference:
        """Gets the transport_document_reference of this Subscription.


        :return: The transport_document_reference of this Subscription.
        :rtype: TransportDocumentReference
        """
        return self._transport_document_reference

    @transport_document_reference.setter
    def transport_document_reference(self, transport_document_reference: TransportDocumentReference):
        """Sets the transport_document_reference of this Subscription.


        :param transport_document_reference: The transport_document_reference of this Subscription.
        :type transport_document_reference: TransportDocumentReference
        """

        self._transport_document_reference = transport_document_reference

    @property
    def transport_document_type_code(self) -> TransportDocumentTypeCodes:
        """Gets the transport_document_type_code of this Subscription.


        :return: The transport_document_type_code of this Subscription.
        :rtype: TransportDocumentTypeCodes
        """
        return self._transport_document_type_code

    @transport_document_type_code.setter
    def transport_document_type_code(self, transport_document_type_code: TransportDocumentTypeCodes):
        """Sets the transport_document_type_code of this Subscription.


        :param transport_document_type_code: The transport_document_type_code of this Subscription.
        :type transport_document_type_code: TransportDocumentTypeCodes
        """

        self._transport_document_type_code = transport_document_type_code

    @property
    def schedule_id(self) -> Object:
        """Gets the schedule_id of this Subscription.


        :return: The schedule_id of this Subscription.
        :rtype: Object
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id: Object):
        """Sets the schedule_id of this Subscription.


        :param schedule_id: The schedule_id of this Subscription.
        :type schedule_id: Object
        """

        self._schedule_id = schedule_id

    @property
    def equipment_reference(self) -> EquipmentReference:
        """Gets the equipment_reference of this Subscription.


        :return: The equipment_reference of this Subscription.
        :rtype: EquipmentReference
        """
        return self._equipment_reference

    @equipment_reference.setter
    def equipment_reference(self, equipment_reference: EquipmentReference):
        """Sets the equipment_reference of this Subscription.


        :param equipment_reference: The equipment_reference of this Subscription.
        :type equipment_reference: EquipmentReference
        """

        self._equipment_reference = equipment_reference
