from .address import Address
from .resource import Resource
from warnings import warn
from .subscription import Subscription

class MasterpassCard(Resource):
    """
    A class representing Masterpass card. Deprecated
    """
    def __init__(self, gateway, attributes):
        warn("MasterpassCard is deprecated")
        Resource.__init__(self, gateway, attributes)

        if "billing_address" in attributes:
            self.billing_address = Address(gateway, self.billing_address)
        else:
            self.billing_address = None

        if "subscriptions" in attributes:
            self.subscriptions = [Subscription(gateway, subscription) for subscription in self.subscriptions]

    @property
    def expiration_date(self):
        return self.expiration_month + "/" + self.expiration_year

    @property
    def masked_number(self):
        return self.bin + "******" + self.last_4

