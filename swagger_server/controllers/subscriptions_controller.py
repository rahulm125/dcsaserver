import connexion
import six

from swagger_server.models.inline_response_default2 import InlineResponseDefault2  # noqa: E501
from swagger_server.models.inline_response_default3 import InlineResponseDefault3  # noqa: E501
from swagger_server.models.inline_response_default4 import InlineResponseDefault4  # noqa: E501
from swagger_server.models.inline_response_default5 import InlineResponseDefault5  # noqa: E501
from swagger_server.models.inline_response_default6 import InlineResponseDefault6  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server.models.subscription_body_with_secret import SubscriptionBodyWithSecret  # noqa: E501
from swagger_server.models.subscription_id import SubscriptionID  # noqa: E501
from swagger_server import util


def v2_event_subscriptions_get(limit=None, cursor=None, sort=None, api_version=None):  # noqa: E501
    """Receive a list of your active subscriptions

     # noqa: E501

    :param limit: Maximum number of items to return.
    :type limit: int
    :param cursor: A server generated value to specify a specific point in a collection result, used for pagination.
    :type cursor: str
    :param sort: A comma-separated list of field names to define the sort order. Field names should be suffixed by a (:) followed by either the keyword ASC (for ascending order) or DESC (for descening order) to specify direction. &lt;b&gt;:ASC&lt;/b&gt; may be omitted, in which case ascending order will be used. 
    :type sort: str
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: List[Subscription]
    """
    return 'do some magic!'


def v2_event_subscriptions_post(body, api_version=None):  # noqa: E501
    """Create a subscription

     # noqa: E501

    :param body: Parameters used to configure the subscription. It is possible to only receive cirtain types of events by adding filter values to the subscription.

All values in the subscription body except&amp;#58; &lt;i&gt;callback, secret and subscriptionID&lt;/i&gt; will be used as filters. All filters specified must be filfilled in order to match an Event. A logical &lt;b&gt;AND&lt;/b&gt; is used between filters. So

&lt;i&gt;shipmentEventTypeCode&#x3D;DRFT&lt;b&gt;&amp;&lt;/b&gt;carrierBookingReference&#x3D;ABC123123&lt;/i&gt;

means that the events matched must both be Draft (shipmentEventTypeCode&#x3D;DRFT) &lt;b&gt;and&lt;/b&gt; be connected to carrierBookingReference ABC123123 (carrierBookingReference&#x3D;ABC123123)

Filters that are specified as (comma separated) lists use logical &lt;b&gt;OR&lt;/b&gt; between list values. So

&lt;i&gt;eventType&#x3D;SHIPMENT,TRANSPORT&lt;/i&gt;

means that &lt;b&gt;both&lt;/b&gt; Shipment- &lt;b&gt;and&lt;/b&gt; Transport-events will be matched by this subscription.

    :type body: dict | bytes
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = SubscriptionBodyWithSecret.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_event_subscriptions_subscription_iddelete(subscription_id, api_version=None):  # noqa: E501
    """Stop a subscription, using the subscription ID

     # noqa: E501

    :param subscription_id: The universal unique ID of the subscription.
    :type subscription_id: dict | bytes
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: None
    """
    if connexion.request.is_json:
        subscription_id = SubscriptionID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_event_subscriptions_subscription_idget(subscription_id, api_version=None):  # noqa: E501
    """Find a subscription by subscription ID

     # noqa: E501

    :param subscription_id: The universal unique ID of the subscription.
    :type subscription_id: dict | bytes
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: Subscription
    """
    if connexion.request.is_json:
        subscription_id = SubscriptionID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_event_subscriptions_subscription_idput(body, subscription_id, api_version=None):  # noqa: E501
    """Alter a subscription

     # noqa: E501

    :param body: Parameters used to configure the subscription
    :type body: dict | bytes
    :param subscription_id: The universal unique ID of the subscription.
    :type subscription_id: dict | bytes
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        subscription_id = SubscriptionID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
