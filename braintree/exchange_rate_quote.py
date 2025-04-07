from app.library.braintree_python.braintree.attribute_getter import AttributeGetter
from app.library.braintree_python.braintree.montary_amount import MontaryAmount

class ExchangeRateQuote(AttributeGetter):
    def __init__(self,attributes):
        AttributeGetter.__init__(self,attributes)