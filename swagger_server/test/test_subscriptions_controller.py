# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response_default2 import InlineResponseDefault2  # noqa: E501
from swagger_server.models.inline_response_default3 import InlineResponseDefault3  # noqa: E501
from swagger_server.models.inline_response_default4 import InlineResponseDefault4  # noqa: E501
from swagger_server.models.inline_response_default5 import InlineResponseDefault5  # noqa: E501
from swagger_server.models.inline_response_default6 import InlineResponseDefault6  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server.models.subscription_body_with_secret import SubscriptionBodyWithSecret  # noqa: E501
from swagger_server.models.subscription_id import SubscriptionID  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSubscriptionsController(BaseTestCase):
    """SubscriptionsController integration test stubs"""

    def test_v2_event_subscriptions_get(self):
        """Test case for v2_event_subscriptions_get

        Receive a list of your active subscriptions
        """
        query_string = [('limit', 2),
                        ('cursor', 'cursor_example'),
                        ('sort', 'sort_example')]
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/event-subscriptions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_event_subscriptions_post(self):
        """Test case for v2_event_subscriptions_post

        Create a subscription
        """
        body = SubscriptionBodyWithSecret()
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/event-subscriptions',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_event_subscriptions_subscription_iddelete(self):
        """Test case for v2_event_subscriptions_subscription_iddelete

        Stop a subscription, using the subscription ID
        """
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/event-subscriptions/{subscriptionID}'.format(subscription_id=SubscriptionID()),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_event_subscriptions_subscription_idget(self):
        """Test case for v2_event_subscriptions_subscription_idget

        Find a subscription by subscription ID
        """
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/event-subscriptions/{subscriptionID}'.format(subscription_id=SubscriptionID()),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_event_subscriptions_subscription_idput(self):
        """Test case for v2_event_subscriptions_subscription_idput

        Alter a subscription
        """
        body = Subscription()
        headers = [('api_version', 'api_version_example')]
        response = self.client.open(
            '/v2/event-subscriptions/{subscriptionID}'.format(subscription_id=SubscriptionID()),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
