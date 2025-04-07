from app.library.braintree_python.braintree.resource import Resource
from app.library.braintree_python.braintree.transaction import Transaction

class LocalPaymentFunded(Resource):
    """
    A class representing Braintree LocalPaymentFunded webhook.
    """
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)

        self.transaction = Transaction(gateway, attributes.pop("transaction"))
