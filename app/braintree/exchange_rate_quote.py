from app.braintree.attribute_getter import AttributeGetter
from app.braintree.montary_amount import MontaryAmount

class ExchangeRateQuote(AttributeGetter):
    def __init__(self,attributes):
        AttributeGetter.__init__(self,attributes)