# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vessel_call_sign_number import VesselCallSignNumber  # noqa: F401,E501
from swagger_server.models.vessel_flag import VesselFlag  # noqa: F401,E501
from swagger_server.models.vessel_name import VesselName  # noqa: F401,E501
from swagger_server.models.vessel_operator_carrier_code import VesselOperatorCarrierCode  # noqa: F401,E501
from swagger_server.models.vessel_operator_carrier_code_list_provider import VesselOperatorCarrierCodeListProvider  # noqa: F401,E501
from swagger_server import util


class Vessel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, vessel_name: VesselName=None, vessel_flag: VesselFlag=None, vessel_call_sign_number: VesselCallSignNumber=None, vessel_operator_carrier_code: VesselOperatorCarrierCode=None, vessel_operator_carrier_code_list_provider: VesselOperatorCarrierCodeListProvider=None):  # noqa: E501
        """Vessel - a model defined in Swagger

        :param vessel_name: The vessel_name of this Vessel.  # noqa: E501
        :type vessel_name: VesselName
        :param vessel_flag: The vessel_flag of this Vessel.  # noqa: E501
        :type vessel_flag: VesselFlag
        :param vessel_call_sign_number: The vessel_call_sign_number of this Vessel.  # noqa: E501
        :type vessel_call_sign_number: VesselCallSignNumber
        :param vessel_operator_carrier_code: The vessel_operator_carrier_code of this Vessel.  # noqa: E501
        :type vessel_operator_carrier_code: VesselOperatorCarrierCode
        :param vessel_operator_carrier_code_list_provider: The vessel_operator_carrier_code_list_provider of this Vessel.  # noqa: E501
        :type vessel_operator_carrier_code_list_provider: VesselOperatorCarrierCodeListProvider
        """
        self.swagger_types = {
            'vessel_name': VesselName,
            'vessel_flag': VesselFlag,
            'vessel_call_sign_number': VesselCallSignNumber,
            'vessel_operator_carrier_code': VesselOperatorCarrierCode,
            'vessel_operator_carrier_code_list_provider': VesselOperatorCarrierCodeListProvider
        }

        self.attribute_map = {
            'vessel_name': 'vesselName',
            'vessel_flag': 'vesselFlag',
            'vessel_call_sign_number': 'vesselCallSignNumber',
            'vessel_operator_carrier_code': 'vesselOperatorCarrierCode',
            'vessel_operator_carrier_code_list_provider': 'vesselOperatorCarrierCodeListProvider'
        }
        self._vessel_name = vessel_name
        self._vessel_flag = vessel_flag
        self._vessel_call_sign_number = vessel_call_sign_number
        self._vessel_operator_carrier_code = vessel_operator_carrier_code
        self._vessel_operator_carrier_code_list_provider = vessel_operator_carrier_code_list_provider

    @classmethod
    def from_dict(cls, dikt) -> 'Vessel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vessel of this Vessel.  # noqa: E501
        :rtype: Vessel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vessel_name(self) -> VesselName:
        """Gets the vessel_name of this Vessel.


        :return: The vessel_name of this Vessel.
        :rtype: VesselName
        """
        return self._vessel_name

    @vessel_name.setter
    def vessel_name(self, vessel_name: VesselName):
        """Sets the vessel_name of this Vessel.


        :param vessel_name: The vessel_name of this Vessel.
        :type vessel_name: VesselName
        """

        self._vessel_name = vessel_name

    @property
    def vessel_flag(self) -> VesselFlag:
        """Gets the vessel_flag of this Vessel.


        :return: The vessel_flag of this Vessel.
        :rtype: VesselFlag
        """
        return self._vessel_flag

    @vessel_flag.setter
    def vessel_flag(self, vessel_flag: VesselFlag):
        """Sets the vessel_flag of this Vessel.


        :param vessel_flag: The vessel_flag of this Vessel.
        :type vessel_flag: VesselFlag
        """

        self._vessel_flag = vessel_flag

    @property
    def vessel_call_sign_number(self) -> VesselCallSignNumber:
        """Gets the vessel_call_sign_number of this Vessel.


        :return: The vessel_call_sign_number of this Vessel.
        :rtype: VesselCallSignNumber
        """
        return self._vessel_call_sign_number

    @vessel_call_sign_number.setter
    def vessel_call_sign_number(self, vessel_call_sign_number: VesselCallSignNumber):
        """Sets the vessel_call_sign_number of this Vessel.


        :param vessel_call_sign_number: The vessel_call_sign_number of this Vessel.
        :type vessel_call_sign_number: VesselCallSignNumber
        """

        self._vessel_call_sign_number = vessel_call_sign_number

    @property
    def vessel_operator_carrier_code(self) -> VesselOperatorCarrierCode:
        """Gets the vessel_operator_carrier_code of this Vessel.


        :return: The vessel_operator_carrier_code of this Vessel.
        :rtype: VesselOperatorCarrierCode
        """
        return self._vessel_operator_carrier_code

    @vessel_operator_carrier_code.setter
    def vessel_operator_carrier_code(self, vessel_operator_carrier_code: VesselOperatorCarrierCode):
        """Sets the vessel_operator_carrier_code of this Vessel.


        :param vessel_operator_carrier_code: The vessel_operator_carrier_code of this Vessel.
        :type vessel_operator_carrier_code: VesselOperatorCarrierCode
        """

        self._vessel_operator_carrier_code = vessel_operator_carrier_code

    @property
    def vessel_operator_carrier_code_list_provider(self) -> VesselOperatorCarrierCodeListProvider:
        """Gets the vessel_operator_carrier_code_list_provider of this Vessel.


        :return: The vessel_operator_carrier_code_list_provider of this Vessel.
        :rtype: VesselOperatorCarrierCodeListProvider
        """
        return self._vessel_operator_carrier_code_list_provider

    @vessel_operator_carrier_code_list_provider.setter
    def vessel_operator_carrier_code_list_provider(self, vessel_operator_carrier_code_list_provider: VesselOperatorCarrierCodeListProvider):
        """Sets the vessel_operator_carrier_code_list_provider of this Vessel.


        :param vessel_operator_carrier_code_list_provider: The vessel_operator_carrier_code_list_provider of this Vessel.
        :type vessel_operator_carrier_code_list_provider: VesselOperatorCarrierCodeListProvider
        """

        self._vessel_operator_carrier_code_list_provider = vessel_operator_carrier_code_list_provider
