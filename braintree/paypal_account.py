from .resource import Resource
from .configuration import Configuration
from .subscription import Subscription


class PayPalAccount(Resource):
    @staticmethod
    def find(paypal_account_token):
        return Configuration.gateway().paypal_account.find(paypal_account_token)

    @staticmethod
    def delete(paypal_account_token):
        return Configuration.gateway().paypal_account.delete(paypal_account_token)

    @staticmethod
    def update(paypal_account_token, params=None):
        if params is None:
            params = {}
        return Configuration.gateway().paypal_account.update(paypal_account_token, params)

    @staticmethod
    def signature():
        signature = [
            "token",
            {"options": ["make_default"]}
        ]
        return signature

    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
        if "subscriptions" in attributes:
            self.subscriptions = [Subscription(gateway, subscription) for subscription in self.subscriptions]
