import app.library.braintree_python.braintree as braintree
from app.library.braintree_python.braintree.resource import Resource

class PayPalHere(Resource):
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)

