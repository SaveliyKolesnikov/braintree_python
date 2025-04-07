from decimal import Decimal
from .resource import Resource

class Modification(Resource):
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
        self.amount = Decimal(self.amount)
