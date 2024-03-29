# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.change_remark import ChangeRemark  # noqa: F401,E501
from swagger_server.models.delay_reason_code import DelayReasonCode  # noqa: F401,E501
from swagger_server.models.document_references import DocumentReferences  # noqa: F401,E501
from swagger_server.models.operations_transport_event import OperationsTransportEvent  # noqa: F401,E501
from swagger_server.models.reference import Reference  # noqa: F401,E501
from swagger_server.models.references import References  # noqa: F401,E501
from swagger_server.models.transport_call import TransportCall  # noqa: F401,E501
from swagger_server.models.transport_event_type_code import TransportEventTypeCode  # noqa: F401,E501
from swagger_server.models.vessel_schedule_change_remark import VesselScheduleChangeRemark  # noqa: F401,E501
from swagger_server import util


class TransportEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, references: List[Reference]=None, event_classifier_code: str=None, transport_event_type_code: TransportEventTypeCode=None, delay_reason_code: DelayReasonCode=None, change_remark: ChangeRemark=None, transport_call: TransportCall=None, vessel_schedule_change_remark: VesselScheduleChangeRemark=None, transport_call_id: Object=None, event_type_code: str=None, document_references: DocumentReferences=None):  # noqa: E501
        """TransportEvent - a model defined in Swagger

        :param references: The references of this TransportEvent.  # noqa: E501
        :type references: List[Reference]
        :param event_classifier_code: The event_classifier_code of this TransportEvent.  # noqa: E501
        :type event_classifier_code: str
        :param transport_event_type_code: The transport_event_type_code of this TransportEvent.  # noqa: E501
        :type transport_event_type_code: TransportEventTypeCode
        :param delay_reason_code: The delay_reason_code of this TransportEvent.  # noqa: E501
        :type delay_reason_code: DelayReasonCode
        :param change_remark: The change_remark of this TransportEvent.  # noqa: E501
        :type change_remark: ChangeRemark
        :param transport_call: The transport_call of this TransportEvent.  # noqa: E501
        :type transport_call: TransportCall
        :param vessel_schedule_change_remark: The vessel_schedule_change_remark of this TransportEvent.  # noqa: E501
        :type vessel_schedule_change_remark: VesselScheduleChangeRemark
        :param transport_call_id: The transport_call_id of this TransportEvent.  # noqa: E501
        :type transport_call_id: Object
        :param event_type_code: The event_type_code of this TransportEvent.  # noqa: E501
        :type event_type_code: str
        :param document_references: The document_references of this TransportEvent.  # noqa: E501
        :type document_references: DocumentReferences
        """
        self.swagger_types = {
            'references': List[Reference],
            'event_classifier_code': str,
            'transport_event_type_code': TransportEventTypeCode,
            'delay_reason_code': DelayReasonCode,
            'change_remark': ChangeRemark,
            'transport_call': TransportCall,
            'vessel_schedule_change_remark': VesselScheduleChangeRemark,
            'transport_call_id': Object,
            'event_type_code': str,
            'document_references': DocumentReferences
        }

        self.attribute_map = {
            'references': 'references',
            'event_classifier_code': 'eventClassifierCode',
            'transport_event_type_code': 'transportEventTypeCode',
            'delay_reason_code': 'delayReasonCode',
            'change_remark': 'changeRemark',
            'transport_call': 'transportCall',
            'vessel_schedule_change_remark': 'vesselScheduleChangeRemark',
            'transport_call_id': 'transportCallID',
            'event_type_code': 'eventTypeCode',
            'document_references': 'documentReferences'
        }
        self._references = references
        self._event_classifier_code = event_classifier_code
        self._transport_event_type_code = transport_event_type_code
        self._delay_reason_code = delay_reason_code
        self._change_remark = change_remark
        self._transport_call = transport_call
        self._vessel_schedule_change_remark = vessel_schedule_change_remark
        self._transport_call_id = transport_call_id
        self._event_type_code = event_type_code
        self._document_references = document_references

    @classmethod
    def from_dict(cls, dikt) -> 'TransportEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transportEvent of this TransportEvent.  # noqa: E501
        :rtype: TransportEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def references(self) -> List[Reference]:
        """Gets the references of this TransportEvent.


        :return: The references of this TransportEvent.
        :rtype: List[Reference]
        """
        return self._references

    @references.setter
    def references(self, references: List[Reference]):
        """Sets the references of this TransportEvent.


        :param references: The references of this TransportEvent.
        :type references: List[Reference]
        """

        self._references = references

    @property
    def event_classifier_code(self) -> str:
        """Gets the event_classifier_code of this TransportEvent.

        Code for the event classifier can be - ACT (Actual) - PLN (Planned) - EST (Estimated)   # noqa: E501

        :return: The event_classifier_code of this TransportEvent.
        :rtype: str
        """
        return self._event_classifier_code

    @event_classifier_code.setter
    def event_classifier_code(self, event_classifier_code: str):
        """Sets the event_classifier_code of this TransportEvent.

        Code for the event classifier can be - ACT (Actual) - PLN (Planned) - EST (Estimated)   # noqa: E501

        :param event_classifier_code: The event_classifier_code of this TransportEvent.
        :type event_classifier_code: str
        """

        self._event_classifier_code = event_classifier_code

    @property
    def transport_event_type_code(self) -> TransportEventTypeCode:
        """Gets the transport_event_type_code of this TransportEvent.


        :return: The transport_event_type_code of this TransportEvent.
        :rtype: TransportEventTypeCode
        """
        return self._transport_event_type_code

    @transport_event_type_code.setter
    def transport_event_type_code(self, transport_event_type_code: TransportEventTypeCode):
        """Sets the transport_event_type_code of this TransportEvent.


        :param transport_event_type_code: The transport_event_type_code of this TransportEvent.
        :type transport_event_type_code: TransportEventTypeCode
        """
        if transport_event_type_code is None:
            raise ValueError("Invalid value for `transport_event_type_code`, must not be `None`")  # noqa: E501

        self._transport_event_type_code = transport_event_type_code

    @property
    def delay_reason_code(self) -> DelayReasonCode:
        """Gets the delay_reason_code of this TransportEvent.


        :return: The delay_reason_code of this TransportEvent.
        :rtype: DelayReasonCode
        """
        return self._delay_reason_code

    @delay_reason_code.setter
    def delay_reason_code(self, delay_reason_code: DelayReasonCode):
        """Sets the delay_reason_code of this TransportEvent.


        :param delay_reason_code: The delay_reason_code of this TransportEvent.
        :type delay_reason_code: DelayReasonCode
        """

        self._delay_reason_code = delay_reason_code

    @property
    def change_remark(self) -> ChangeRemark:
        """Gets the change_remark of this TransportEvent.


        :return: The change_remark of this TransportEvent.
        :rtype: ChangeRemark
        """
        return self._change_remark

    @change_remark.setter
    def change_remark(self, change_remark: ChangeRemark):
        """Sets the change_remark of this TransportEvent.


        :param change_remark: The change_remark of this TransportEvent.
        :type change_remark: ChangeRemark
        """

        self._change_remark = change_remark

    @property
    def transport_call(self) -> TransportCall:
        """Gets the transport_call of this TransportEvent.


        :return: The transport_call of this TransportEvent.
        :rtype: TransportCall
        """
        return self._transport_call

    @transport_call.setter
    def transport_call(self, transport_call: TransportCall):
        """Sets the transport_call of this TransportEvent.


        :param transport_call: The transport_call of this TransportEvent.
        :type transport_call: TransportCall
        """
        if transport_call is None:
            raise ValueError("Invalid value for `transport_call`, must not be `None`")  # noqa: E501

        self._transport_call = transport_call

    @property
    def vessel_schedule_change_remark(self) -> VesselScheduleChangeRemark:
        """Gets the vessel_schedule_change_remark of this TransportEvent.


        :return: The vessel_schedule_change_remark of this TransportEvent.
        :rtype: VesselScheduleChangeRemark
        """
        return self._vessel_schedule_change_remark

    @vessel_schedule_change_remark.setter
    def vessel_schedule_change_remark(self, vessel_schedule_change_remark: VesselScheduleChangeRemark):
        """Sets the vessel_schedule_change_remark of this TransportEvent.


        :param vessel_schedule_change_remark: The vessel_schedule_change_remark of this TransportEvent.
        :type vessel_schedule_change_remark: VesselScheduleChangeRemark
        """

        self._vessel_schedule_change_remark = vessel_schedule_change_remark

    @property
    def transport_call_id(self) -> Object:
        """Gets the transport_call_id of this TransportEvent.


        :return: The transport_call_id of this TransportEvent.
        :rtype: Object
        """
        return self._transport_call_id

    @transport_call_id.setter
    def transport_call_id(self, transport_call_id: Object):
        """Sets the transport_call_id of this TransportEvent.


        :param transport_call_id: The transport_call_id of this TransportEvent.
        :type transport_call_id: Object
        """

        self._transport_call_id = transport_call_id

    @property
    def event_type_code(self) -> str:
        """Gets the event_type_code of this TransportEvent.

        Unique identifier for Event Type Code, for transport events this is either - ARRI (Arrival) - DEPA (Departure)  Deprecated - use transportEventTypeCode instead   # noqa: E501

        :return: The event_type_code of this TransportEvent.
        :rtype: str
        """
        return self._event_type_code

    @event_type_code.setter
    def event_type_code(self, event_type_code: str):
        """Sets the event_type_code of this TransportEvent.

        Unique identifier for Event Type Code, for transport events this is either - ARRI (Arrival) - DEPA (Departure)  Deprecated - use transportEventTypeCode instead   # noqa: E501

        :param event_type_code: The event_type_code of this TransportEvent.
        :type event_type_code: str
        """

        self._event_type_code = event_type_code

    @property
    def document_references(self) -> DocumentReferences:
        """Gets the document_references of this TransportEvent.


        :return: The document_references of this TransportEvent.
        :rtype: DocumentReferences
        """
        return self._document_references

    @document_references.setter
    def document_references(self, document_references: DocumentReferences):
        """Sets the document_references of this TransportEvent.


        :param document_references: The document_references of this TransportEvent.
        :type document_references: DocumentReferences
        """

        self._document_references = document_references
