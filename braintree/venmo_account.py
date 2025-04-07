from .resource import Resource
from .subscription import Subscription

class VenmoAccount(Resource):
    """
    A class representing Braintree Venmo accounts.
    """
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)

        if "subscriptions" in attributes:
            self.subscriptions = [Subscription(gateway, subscription) for subscription in self.subscriptions]
