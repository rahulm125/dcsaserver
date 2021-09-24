import connexion
import six

from swagger_server.models.inline_response_default7 import InlineResponseDefault7  # noqa: E501
from swagger_server.models.subscription_id import SubscriptionID  # noqa: E501
from swagger_server.models.subscription_id_secret_body import SubscriptionIDSecretBody  # noqa: E501
from swagger_server import util


def v2_event_subscriptions_subscription_id_secret_put(body, subscription_id, api_version=None):  # noqa: E501
    """Resets the Secret on an existing subscription.

     # noqa: E501

    :param body: Parameters used to configure the subscription
    :type body: dict | bytes
    :param subscription_id: The universal unique ID of the subscription.
    :type subscription_id: dict | bytes
    :param api_version: An API-Version header MAY be added to the request (optional); if added it MUST only contain MAJOR version. API-Version header MUST be aligned with the URI version.
    :type api_version: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = SubscriptionIDSecretBody.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        subscription_id = SubscriptionID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
