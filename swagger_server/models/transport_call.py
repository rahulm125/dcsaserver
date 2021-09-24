# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.carrier_service_code import CarrierServiceCode  # noqa: F401,E501
from swagger_server.models.facility_code import FacilityCode  # noqa: F401,E501
from swagger_server.models.facility_code_list_provider import FacilityCodeListProvider  # noqa: F401,E501
from swagger_server.models.facility_type_code_trn import FacilityTypeCodeTRN  # noqa: F401,E501
from swagger_server.models.mode_of_transport import ModeOfTransport  # noqa: F401,E501
from swagger_server.models.other_facility import OtherFacility  # noqa: F401,E501
from swagger_server.models.transport_call_sequence_number import TransportCallSequenceNumber  # noqa: F401,E501
from swagger_server.models.un_location_code1 import UNLocationCode1  # noqa: F401,E501
from swagger_server.models.vessel import Vessel  # noqa: F401,E501
from swagger_server import util


class TransportCall(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, carrier_service_code: CarrierServiceCode=None, carrier_voyage_number: Object=None, transport_call_sequence_number: TransportCallSequenceNumber=None, un_location_code: UNLocationCode1=None, facility_code: FacilityCode=None, facility_code_list_provider: FacilityCodeListProvider=None, facility_type_code: FacilityTypeCodeTRN=None, other_facility: OtherFacility=None, mode_of_transport: ModeOfTransport=None, location: Object=None, vessel: Vessel=None):  # noqa: E501
        """TransportCall - a model defined in Swagger

        :param carrier_service_code: The carrier_service_code of this TransportCall.  # noqa: E501
        :type carrier_service_code: CarrierServiceCode
        :param carrier_voyage_number: The carrier_voyage_number of this TransportCall.  # noqa: E501
        :type carrier_voyage_number: Object
        :param transport_call_sequence_number: The transport_call_sequence_number of this TransportCall.  # noqa: E501
        :type transport_call_sequence_number: TransportCallSequenceNumber
        :param un_location_code: The un_location_code of this TransportCall.  # noqa: E501
        :type un_location_code: UNLocationCode1
        :param facility_code: The facility_code of this TransportCall.  # noqa: E501
        :type facility_code: FacilityCode
        :param facility_code_list_provider: The facility_code_list_provider of this TransportCall.  # noqa: E501
        :type facility_code_list_provider: FacilityCodeListProvider
        :param facility_type_code: The facility_type_code of this TransportCall.  # noqa: E501
        :type facility_type_code: FacilityTypeCodeTRN
        :param other_facility: The other_facility of this TransportCall.  # noqa: E501
        :type other_facility: OtherFacility
        :param mode_of_transport: The mode_of_transport of this TransportCall.  # noqa: E501
        :type mode_of_transport: ModeOfTransport
        :param location: The location of this TransportCall.  # noqa: E501
        :type location: Object
        :param vessel: The vessel of this TransportCall.  # noqa: E501
        :type vessel: Vessel
        """
        self.swagger_types = {
            'carrier_service_code': CarrierServiceCode,
            'carrier_voyage_number': Object,
            'transport_call_sequence_number': TransportCallSequenceNumber,
            'un_location_code': UNLocationCode1,
            'facility_code': FacilityCode,
            'facility_code_list_provider': FacilityCodeListProvider,
            'facility_type_code': FacilityTypeCodeTRN,
            'other_facility': OtherFacility,
            'mode_of_transport': ModeOfTransport,
            'location': Object,
            'vessel': Vessel
        }

        self.attribute_map = {
            'carrier_service_code': 'carrierServiceCode',
            'carrier_voyage_number': 'carrierVoyageNumber',
            'transport_call_sequence_number': 'transportCallSequenceNumber',
            'un_location_code': 'UNLocationCode',
            'facility_code': 'facilityCode',
            'facility_code_list_provider': 'facilityCodeListProvider',
            'facility_type_code': 'facilityTypeCode',
            'other_facility': 'otherFacility',
            'mode_of_transport': 'modeOfTransport',
            'location': 'location',
            'vessel': 'vessel'
        }
        self._carrier_service_code = carrier_service_code
        self._carrier_voyage_number = carrier_voyage_number
        self._transport_call_sequence_number = transport_call_sequence_number
        self._un_location_code = un_location_code
        self._facility_code = facility_code
        self._facility_code_list_provider = facility_code_list_provider
        self._facility_type_code = facility_type_code
        self._other_facility = other_facility
        self._mode_of_transport = mode_of_transport
        self._location = location
        self._vessel = vessel

    @classmethod
    def from_dict(cls, dikt) -> 'TransportCall':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transportCall of this TransportCall.  # noqa: E501
        :rtype: TransportCall
        """
        return util.deserialize_model(dikt, cls)

    @property
    def carrier_service_code(self) -> CarrierServiceCode:
        """Gets the carrier_service_code of this TransportCall.


        :return: The carrier_service_code of this TransportCall.
        :rtype: CarrierServiceCode
        """
        return self._carrier_service_code

    @carrier_service_code.setter
    def carrier_service_code(self, carrier_service_code: CarrierServiceCode):
        """Sets the carrier_service_code of this TransportCall.


        :param carrier_service_code: The carrier_service_code of this TransportCall.
        :type carrier_service_code: CarrierServiceCode
        """

        self._carrier_service_code = carrier_service_code

    @property
    def carrier_voyage_number(self) -> Object:
        """Gets the carrier_voyage_number of this TransportCall.

        The vessel operator-specific identifier of the Voyage.  In case there are multiple voyages the export voyage is chosen.   # noqa: E501

        :return: The carrier_voyage_number of this TransportCall.
        :rtype: Object
        """
        return self._carrier_voyage_number

    @carrier_voyage_number.setter
    def carrier_voyage_number(self, carrier_voyage_number: Object):
        """Sets the carrier_voyage_number of this TransportCall.

        The vessel operator-specific identifier of the Voyage.  In case there are multiple voyages the export voyage is chosen.   # noqa: E501

        :param carrier_voyage_number: The carrier_voyage_number of this TransportCall.
        :type carrier_voyage_number: Object
        """

        self._carrier_voyage_number = carrier_voyage_number

    @property
    def transport_call_sequence_number(self) -> TransportCallSequenceNumber:
        """Gets the transport_call_sequence_number of this TransportCall.


        :return: The transport_call_sequence_number of this TransportCall.
        :rtype: TransportCallSequenceNumber
        """
        return self._transport_call_sequence_number

    @transport_call_sequence_number.setter
    def transport_call_sequence_number(self, transport_call_sequence_number: TransportCallSequenceNumber):
        """Sets the transport_call_sequence_number of this TransportCall.


        :param transport_call_sequence_number: The transport_call_sequence_number of this TransportCall.
        :type transport_call_sequence_number: TransportCallSequenceNumber
        """

        self._transport_call_sequence_number = transport_call_sequence_number

    @property
    def un_location_code(self) -> UNLocationCode1:
        """Gets the un_location_code of this TransportCall.


        :return: The un_location_code of this TransportCall.
        :rtype: UNLocationCode1
        """
        return self._un_location_code

    @un_location_code.setter
    def un_location_code(self, un_location_code: UNLocationCode1):
        """Sets the un_location_code of this TransportCall.


        :param un_location_code: The un_location_code of this TransportCall.
        :type un_location_code: UNLocationCode1
        """

        self._un_location_code = un_location_code

    @property
    def facility_code(self) -> FacilityCode:
        """Gets the facility_code of this TransportCall.


        :return: The facility_code of this TransportCall.
        :rtype: FacilityCode
        """
        return self._facility_code

    @facility_code.setter
    def facility_code(self, facility_code: FacilityCode):
        """Sets the facility_code of this TransportCall.


        :param facility_code: The facility_code of this TransportCall.
        :type facility_code: FacilityCode
        """

        self._facility_code = facility_code

    @property
    def facility_code_list_provider(self) -> FacilityCodeListProvider:
        """Gets the facility_code_list_provider of this TransportCall.


        :return: The facility_code_list_provider of this TransportCall.
        :rtype: FacilityCodeListProvider
        """
        return self._facility_code_list_provider

    @facility_code_list_provider.setter
    def facility_code_list_provider(self, facility_code_list_provider: FacilityCodeListProvider):
        """Sets the facility_code_list_provider of this TransportCall.


        :param facility_code_list_provider: The facility_code_list_provider of this TransportCall.
        :type facility_code_list_provider: FacilityCodeListProvider
        """

        self._facility_code_list_provider = facility_code_list_provider

    @property
    def facility_type_code(self) -> FacilityTypeCodeTRN:
        """Gets the facility_type_code of this TransportCall.


        :return: The facility_type_code of this TransportCall.
        :rtype: FacilityTypeCodeTRN
        """
        return self._facility_type_code

    @facility_type_code.setter
    def facility_type_code(self, facility_type_code: FacilityTypeCodeTRN):
        """Sets the facility_type_code of this TransportCall.


        :param facility_type_code: The facility_type_code of this TransportCall.
        :type facility_type_code: FacilityTypeCodeTRN
        """

        self._facility_type_code = facility_type_code

    @property
    def other_facility(self) -> OtherFacility:
        """Gets the other_facility of this TransportCall.


        :return: The other_facility of this TransportCall.
        :rtype: OtherFacility
        """
        return self._other_facility

    @other_facility.setter
    def other_facility(self, other_facility: OtherFacility):
        """Sets the other_facility of this TransportCall.


        :param other_facility: The other_facility of this TransportCall.
        :type other_facility: OtherFacility
        """

        self._other_facility = other_facility

    @property
    def mode_of_transport(self) -> ModeOfTransport:
        """Gets the mode_of_transport of this TransportCall.


        :return: The mode_of_transport of this TransportCall.
        :rtype: ModeOfTransport
        """
        return self._mode_of_transport

    @mode_of_transport.setter
    def mode_of_transport(self, mode_of_transport: ModeOfTransport):
        """Sets the mode_of_transport of this TransportCall.


        :param mode_of_transport: The mode_of_transport of this TransportCall.
        :type mode_of_transport: ModeOfTransport
        """
        if mode_of_transport is None:
            raise ValueError("Invalid value for `mode_of_transport`, must not be `None`")  # noqa: E501

        self._mode_of_transport = mode_of_transport

    @property
    def location(self) -> Object:
        """Gets the location of this TransportCall.


        :return: The location of this TransportCall.
        :rtype: Object
        """
        return self._location

    @location.setter
    def location(self, location: Object):
        """Sets the location of this TransportCall.


        :param location: The location of this TransportCall.
        :type location: Object
        """

        self._location = location

    @property
    def vessel(self) -> Vessel:
        """Gets the vessel of this TransportCall.


        :return: The vessel of this TransportCall.
        :rtype: Vessel
        """
        return self._vessel

    @vessel.setter
    def vessel(self, vessel: Vessel):
        """Sets the vessel of this TransportCall.


        :param vessel: The vessel of this TransportCall.
        :type vessel: Vessel
        """

        self._vessel = vessel