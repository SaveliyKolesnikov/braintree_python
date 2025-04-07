from app.library.braintree_python.braintree.attribute_getter import AttributeGetter
from app.library.braintree_python.braintree.liability_shift import LiabilityShift

class RiskData(AttributeGetter):
    def __init__(self, attributes):
        AttributeGetter.__init__(self, attributes)
        if "liability_shift" in attributes:
            self.liability_shift = LiabilityShift(attributes["liability_shift"])
