from app.braintree.blik_alias import BlikAlias
from app.braintree.resource import Resource
from app.braintree.transaction import Transaction

class LocalPaymentCompleted(Resource):
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)

        if "transaction" in attributes:
            self.transaction = Transaction(gateway, attributes.pop("transaction"))
        if "blik_aliases" in attributes:
            self.blik_aliases = [BlikAlias(gateway, blik_alias) for blik_alias in self.blik_aliases]
