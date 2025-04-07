from .resource import Resource
from .payment_method_parser import parse_payment_method
from .enriched_customer_data import EnrichedCustomerData

class PaymentMethodCustomerDataUpdatedMetadata(Resource):
    """
    A class representing Braintree PaymentMethodCustomerDataUpdatedMetadata webhook.
    """
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
        self.payment_method = parse_payment_method(gateway, attributes["payment_method"])
        if attributes["enriched_customer_data"]:
            self.enriched_customer_data = EnrichedCustomerData(gateway, attributes["enriched_customer_data"])

