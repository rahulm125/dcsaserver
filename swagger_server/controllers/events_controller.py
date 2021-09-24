import connexion
import six

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
from swagger_server import util


def v2_events_event_idget(event_id):  # noqa: E501
    """Find events by eventID.

    Returns event with the specified eventID. # noqa: E501

    :param event_id: The ID of the event to receive
    :type event_id: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        event_id = EventID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_events_get(event_type=None, shipment_event_type_code=None, carrier_booking_reference=None, booking_reference=None, transport_document_id=None, transport_document_reference=None, transport_document_type_code=None, transport_event_type_code=None, schedule_id=None, transport_call_id=None, vessel_imo_number=None, carrier_voyage_number=None, carrier_service_code=None, un_location_code=None, equipment_event_type_code=None, equipment_reference=None, event_created_date_time=None, limit=None, cursor=None, sort=None, api_version=None):  # noqa: E501
    """Find events.

    Returns all events filtered by the queryParameters.  &lt;b&gt;NB&lt;/b&gt;&amp;#58; It is possible to combine queryParameters. When combining queryParameters be aware that it is also possible to make combinations that are mutual contradicting.  Example&amp;#58; &lt;i&gt;shipmentEventTypeCode&#x3D;DRFT and equipmentEventTypeCode&#x3D;GTIN&lt;/i&gt;  Since there is no event that can be a ShipmentEvent &lt;u&gt;and&lt;/u&gt; an EquipmentEvent at the same time &lt;b&gt;this will return an empty list&lt;b&gt;!  # noqa: E501

    :param event_type: The type of event(s) to filter by. Possible values are  - SHIPMENT (Shipment events) - TRANSPORT (Transport events) - EQUIPMENT (Equipment events)  It is possible to select multiple values by comma (,) separating them. For multiple values the OR-operator is used. For example eventType&#x3D;SHIPMENT,EQUIPMENT matches both Shipment- and Equipment-events.  Default value is all event types. 
    :type event_type: List[str]
    :param shipment_event_type_code: The status of the document in the process to filter by. Possible values are - RECE (Received) - DRFT (Drafted) - PENA (Pending Approval) - PENU (Pending Update) - REJE (Rejected) - APPR (Approved) - ISSU (Issued) - SURR (Surrendered) - SUBM (Submitted) - VOID (Void) - CONF (Confirmed)  It is possible to select multiple values by comma (,) separating them. For multiple values the OR-operator is used. For example &lt;i&gt;shipmentEventTypeCode&#x3D;RECE,DRFT&lt;/i&gt;  Matches &lt;b&gt;both&lt;/b&gt; Received (RECE) and Drafted (DRFT) shipment events.  Default is all shipmentEventTypeCodes.  This filter is only relevant when filtering on ShipmentEvents 
    :type shipment_event_type_code: list | bytes
    :param carrier_booking_reference: A set of unique characters provided by carrier to identify a booking.  Specifying this filter will only return events related to this particular carrierBookingReference. 
    :type carrier_booking_reference: dict | bytes
    :param booking_reference: Deprecated - use carrierBookingReference instead.
    :type booking_reference: str
    :param transport_document_id: A unique id to identify a transport document.  Deprecated - use transportDocumentReference instead transportDocumentReference 
    :type transport_document_id: 
    :param transport_document_reference: A unique number reference allocated by the shipping line to the transport document and the main number used for the tracking of the status of the shipment.  Specifying this filter will only return events related to this particular transportDocumentReference 
    :type transport_document_reference: dict | bytes
    :param transport_document_type_code: Specifies the type of the transport document (a Bill of Lading (BOL) or a Sea Waybill (SWB)) to filter by.  Default is both. 
    :type transport_document_type_code: list | bytes
    :param transport_event_type_code: Identifier for type of Transport event to filter by - ARRI (Arrived) - DEPA (Departed)  It is possible to select multiple values by comma (,) separating them. For multiple values the OR-operator is used. For example &lt;i&gt;transportEventTypeCode&#x3D;ARRI,DEPA&lt;/i&gt; matches &lt;b&gt;both&lt;/b&gt; Arrived (ARRI) and Departed (DEPA) transport events.  Default is all transportEventTypeCodes.  This filter is only relevant when filtering on TransportEvents 
    :type transport_event_type_code: list | bytes
    :param schedule_id: ID uniquely identifying a schedule, to filter events by.  This filter was added by mistake and is thus deprecated. 
    :type schedule_id: dict | bytes
    :param transport_call_id: ID uniquely identifying a transport call, to filter events by.  Specifying this filter will only return events related to this particular transportCallID 
    :type transport_call_id: dict | bytes
    :param vessel_imo_number: The identifier of vessel for which schedule details are published. Depending on schedule type, this may not be available yet.  Specifying this filter will only return events related to this particular vesselIMONumber. 
    :type vessel_imo_number: dict | bytes
    :param carrier_voyage_number: Filter on the vessel operator-specific identifier of the Voyage.  Specifying this filter will only return events related to this particular carrierVoyageNumber. 
    :type carrier_voyage_number: dict | bytes
    :param carrier_service_code: Filter on the carrier specific identifier of the service.  Specifying this filter will only return events related to this particular carrierServiceCode. 
    :type carrier_service_code: dict | bytes
    :param un_location_code: The UN Location code specifying where the place is located.  Specifying this filter will only return events related to this particular UN Location code. 
    :type un_location_code: dict | bytes
    :param equipment_event_type_code: Unique identifier for equipmentEventTypeCode. - LOAD (Loaded) - DISC (Discharged) - GTIN (Gated in) - GTOT (Gated out) - STUF (Stuffed) - STRP (Stripped)  It is possible to select multiple values by comma (,) separating them. For multiple values the OR-operator is used. For example &lt;i&gt;equipmentEventTypeCode&#x3D;GTIN,GTOT&lt;/i&gt; matches &lt;b&gt;both&lt;/b&gt; Gated in (GTIN) and Gated out (GTOT) equipment events.  Default is all equipmentEventTypeCodes.  This filter is only relevant when filtering on EquipmentEvents 
    :type equipment_event_type_code: list | bytes
    :param equipment_reference: Will filter by the unique identifier for the equipment, which should follow the BIC ISO Container Identification Number where possible.  Specifying this filter will only return events related to this particular equipmentReference 
    :type equipment_reference: dict | bytes
    :param event_created_date_time: Limit the result based on the creating date of the event. It is possible to use operators on this query parameter. This is done by adding a colon followed by an operator at the end of the queryParameterName (before the &#x3D;)  &lt;i&gt;eventCreatedDateTime&lt;b&gt;&amp;#58;gte&lt;/b&gt;&#x3D;2021-04-01T14&amp;#58;12&amp;#58;56+01&amp;#58;00&lt;/i&gt;  would result in all events created &amp;#8805; 2021-04-01T14&amp;#58;12&amp;#58;56+01&amp;#58;00  The following operators are supported - &amp;#58;gte (&amp;#8805; Greater than or equal) - &amp;#58;gt (&amp;#62; Greater than) - &amp;#58;lte (&amp;#8804; Less than or equal) - &amp;#58;lt (&amp;#60; Less than) - &amp;#58;eq (&amp;#61; Equal to)  If no operator is provided, a &lt;b&gt;strictly equal&lt;/b&gt; is used (this is equivalent to &lt;b&gt;&amp;#58;eq&lt;/b&gt; operator). 
    :type event_created_date_time: dict | bytes
    :param limit: Maximum number of items to return.
    :type limit: int
    :param cursor: A server generated value to specify a specific point in a collection result, used for pagination.
    :type cursor: str
    :param sort: A comma-separated list of field names to define the sort order. Field names should be suffixed by a (:) followed by either the keyword ASC (for ascending order) or DESC (for descening order) to specify direction. &lt;b&gt;:ASC&lt;/b&gt; may be omitted, in which case ascending order will be used. 
    :type sort: str
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: List[Object]
    """
    if connexion.request.is_json:
        shipment_event_type_code = [ShipmentEventTypeCode.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        carrier_booking_reference = CarrierBookingReference.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transport_document_reference = TransportDocumentReference.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transport_document_type_code = [TransportDocumentType.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        transport_event_type_code = [TransportEventTypeCode.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        schedule_id = ScheduleID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transport_call_id = TransportCallID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        vessel_imo_number = VesselIMONumber.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        carrier_voyage_number = CarrierVoyageNumber.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        carrier_service_code = CarrierServiceCode.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        un_location_code = UNLocationCode.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        equipment_event_type_code = [EquipmentEventTypeCode.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        equipment_reference = EquipmentReference.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        event_created_date_time = EventCreatedDateTime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
