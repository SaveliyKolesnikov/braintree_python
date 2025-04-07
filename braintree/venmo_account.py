import app.library.braintree_python.braintree as braintree
from app.library.braintree_python.braintree.resource import Resource

class VenmoAccount(Resource):
    """
    A class representing Braintree Venmo accounts.
    """
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)

        if "subscriptions" in attributes:
            self.subscriptions = [braintree.subscription.Subscription(gateway, subscription) for subscription in self.subscriptions]
