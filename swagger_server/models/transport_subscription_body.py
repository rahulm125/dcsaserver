# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.carrier_service_code import CarrierServiceCode  # noqa: F401,E501
from swagger_server.models.carrier_voyage_number import CarrierVoyageNumber  # noqa: F401,E501
from swagger_server.models.transport_call_id import TransportCallID  # noqa: F401,E501
from swagger_server.models.un_location_code import UNLocationCode  # noqa: F401,E501
from swagger_server.models.vessel_imo_number import VesselIMONumber  # noqa: F401,E501
from swagger_server import util


class TransportSubscriptionBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, transport_call_id: TransportCallID=None, vessel_imo_number: VesselIMONumber=None, carrier_voyage_number: CarrierVoyageNumber=None, carrier_service_code: CarrierServiceCode=None, un_location_code: UNLocationCode=None):  # noqa: E501
        """TransportSubscriptionBody - a model defined in Swagger

        :param transport_call_id: The transport_call_id of this TransportSubscriptionBody.  # noqa: E501
        :type transport_call_id: TransportCallID
        :param vessel_imo_number: The vessel_imo_number of this TransportSubscriptionBody.  # noqa: E501
        :type vessel_imo_number: VesselIMONumber
        :param carrier_voyage_number: The carrier_voyage_number of this TransportSubscriptionBody.  # noqa: E501
        :type carrier_voyage_number: CarrierVoyageNumber
        :param carrier_service_code: The carrier_service_code of this TransportSubscriptionBody.  # noqa: E501
        :type carrier_service_code: CarrierServiceCode
        :param un_location_code: The un_location_code of this TransportSubscriptionBody.  # noqa: E501
        :type un_location_code: UNLocationCode
        """
        self.swagger_types = {
            'transport_call_id': TransportCallID,
            'vessel_imo_number': VesselIMONumber,
            'carrier_voyage_number': CarrierVoyageNumber,
            'carrier_service_code': CarrierServiceCode,
            'un_location_code': UNLocationCode
        }

        self.attribute_map = {
            'transport_call_id': 'transportCallID',
            'vessel_imo_number': 'vesselIMONumber',
            'carrier_voyage_number': 'carrierVoyageNumber',
            'carrier_service_code': 'carrierServiceCode',
            'un_location_code': 'UNLocationCode'
        }
        self._transport_call_id = transport_call_id
        self._vessel_imo_number = vessel_imo_number
        self._carrier_voyage_number = carrier_voyage_number
        self._carrier_service_code = carrier_service_code
        self._un_location_code = un_location_code

    @classmethod
    def from_dict(cls, dikt) -> 'TransportSubscriptionBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transportSubscriptionBody of this TransportSubscriptionBody.  # noqa: E501
        :rtype: TransportSubscriptionBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transport_call_id(self) -> TransportCallID:
        """Gets the transport_call_id of this TransportSubscriptionBody.


        :return: The transport_call_id of this TransportSubscriptionBody.
        :rtype: TransportCallID
        """
        return self._transport_call_id

    @transport_call_id.setter
    def transport_call_id(self, transport_call_id: TransportCallID):
        """Sets the transport_call_id of this TransportSubscriptionBody.


        :param transport_call_id: The transport_call_id of this TransportSubscriptionBody.
        :type transport_call_id: TransportCallID
        """

        self._transport_call_id = transport_call_id

    @property
    def vessel_imo_number(self) -> VesselIMONumber:
        """Gets the vessel_imo_number of this TransportSubscriptionBody.


        :return: The vessel_imo_number of this TransportSubscriptionBody.
        :rtype: VesselIMONumber
        """
        return self._vessel_imo_number

    @vessel_imo_number.setter
    def vessel_imo_number(self, vessel_imo_number: VesselIMONumber):
        """Sets the vessel_imo_number of this TransportSubscriptionBody.


        :param vessel_imo_number: The vessel_imo_number of this TransportSubscriptionBody.
        :type vessel_imo_number: VesselIMONumber
        """

        self._vessel_imo_number = vessel_imo_number

    @property
    def carrier_voyage_number(self) -> CarrierVoyageNumber:
        """Gets the carrier_voyage_number of this TransportSubscriptionBody.


        :return: The carrier_voyage_number of this TransportSubscriptionBody.
        :rtype: CarrierVoyageNumber
        """
        return self._carrier_voyage_number

    @carrier_voyage_number.setter
    def carrier_voyage_number(self, carrier_voyage_number: CarrierVoyageNumber):
        """Sets the carrier_voyage_number of this TransportSubscriptionBody.


        :param carrier_voyage_number: The carrier_voyage_number of this TransportSubscriptionBody.
        :type carrier_voyage_number: CarrierVoyageNumber
        """

        self._carrier_voyage_number = carrier_voyage_number

    @property
    def carrier_service_code(self) -> CarrierServiceCode:
        """Gets the carrier_service_code of this TransportSubscriptionBody.


        :return: The carrier_service_code of this TransportSubscriptionBody.
        :rtype: CarrierServiceCode
        """
        return self._carrier_service_code

    @carrier_service_code.setter
    def carrier_service_code(self, carrier_service_code: CarrierServiceCode):
        """Sets the carrier_service_code of this TransportSubscriptionBody.


        :param carrier_service_code: The carrier_service_code of this TransportSubscriptionBody.
        :type carrier_service_code: CarrierServiceCode
        """

        self._carrier_service_code = carrier_service_code

    @property
    def un_location_code(self) -> UNLocationCode:
        """Gets the un_location_code of this TransportSubscriptionBody.


        :return: The un_location_code of this TransportSubscriptionBody.
        :rtype: UNLocationCode
        """
        return self._un_location_code

    @un_location_code.setter
    def un_location_code(self, un_location_code: UNLocationCode):
        """Sets the un_location_code of this TransportSubscriptionBody.


        :param un_location_code: The un_location_code of this TransportSubscriptionBody.
        :type un_location_code: UNLocationCode
        """

        self._un_location_code = un_location_code