import app.library.braintree_python.braintree as braintree
from app.library.braintree_python.braintree.util.datetime_parser import parse_datetime
from app.library.braintree_python.braintree.resource import Resource

class AchMandate(Resource):

    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
