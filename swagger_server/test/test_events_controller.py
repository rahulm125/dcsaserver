# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.carrier_booking_reference import CarrierBookingReference  # noqa: E501
from swagger_server.models.carrier_service_code import CarrierServiceCode  # noqa: E501
from swagger_server.models.carrier_voyage_number import CarrierVoyageNumber  # noqa: E501
from swagger_server.models.equipment_event_type_code import EquipmentEventTypeCode  # noqa: E501
from swagger_server.models.equipment_reference import EquipmentReference  # noqa: E501
from swagger_server.models.event_created_date_time import EventCreatedDateTime  # noqa: E501
from swagger_server.models.event_id import EventID  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response_default import InlineResponseDefault  # noqa: E501
from swagger_server.models.inline_response_default1 import InlineResponseDefault1  # noqa: E501
from swagger_server.models.schedule_id import ScheduleID  # noqa: E501
from swagger_server.models.shipment_event_type_code import ShipmentEventTypeCode  # noqa: E501
from swagger_server.models.transport_call_id import TransportCallID  # noqa: E501
from swagger_server.models.transport_document_reference import TransportDocumentReference  # noqa: E501
from swagger_server.models.transport_document_type import TransportDocumentType  # noqa: E501
from swagger_server.models.transport_event_type_code import TransportEventTypeCode  # noqa: E501
from swagger_server.models.un_location_code import UNLocationCode  # noqa: E501
from swagger_server.models.vessel_imo_number import VesselIMONumber  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventsController(BaseTestCase):
    """EventsController integration test stubs"""

    def test_v2_events_event_idget(self):
        """Test case for v2_events_event_idget

        Find events by eventID.
        """
        response = self.client.open(
            '/v2/events/{eventID}'.format(event_id=EventID()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_events_get(self):
        """Test case for v2_events_get

        Find events.
        """
        query_string = [('event_type', 'event_type_example'),
                        ('shipment_event_type_code', ShipmentEventTypeCode()),
                        ('carrier_booking_reference', CarrierBookingReference()),
                        ('booking_reference', 'booking_reference_example'),
                        ('transport_document_id', '38400000-8cf0-11bd-b23e-10b96e4ef00d'),
                        ('transport_document_reference', TransportDocumentReference()),
                        ('transport_document_type_code', TransportDocumentType()),
                        ('transport_event_type_code', TransportEventTypeCode()),
                        ('schedule_id', ScheduleID()),
                        ('transport_call_id', TransportCallID()),
                        ('vessel_imo_number', VesselIMONumber()),
                        ('carrier_voyage_number', CarrierVoyageNumber()),
                        ('carrier_service_code', CarrierServiceCode()),
                        ('un_location_code', UNLocationCode()),
                        ('equipment_event_type_code', EquipmentEventTypeCode()),
                        ('equipment_reference', EquipmentReference()),
                        ('event_created_date_time', EventCreatedDateTime()),
                        ('limit', 2),
                        ('cursor', 'cursor_example'),
                        ('sort', 'sort_example')]
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/events',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
