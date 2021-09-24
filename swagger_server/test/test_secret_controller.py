# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response_default7 import InlineResponseDefault7  # noqa: E501
from swagger_server.models.subscription_id import SubscriptionID  # noqa: E501
from swagger_server.models.subscription_id_secret_body import SubscriptionIDSecretBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSecretController(BaseTestCase):
    """SecretController integration test stubs"""

    def test_v2_event_subscriptions_subscription_id_secret_put(self):
        """Test case for v2_event_subscriptions_subscription_id_secret_put

        Resets the Secret on an existing subscription.
        """
        body = SubscriptionIDSecretBody()
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/event-subscriptions/{subscriptionID}/secret'.format(subscription_id=SubscriptionID()),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
