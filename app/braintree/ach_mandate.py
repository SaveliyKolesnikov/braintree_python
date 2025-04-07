import app.braintree as braintree
from app.braintree.util.datetime_parser import parse_datetime
from app.braintree.resource import Resource

class AchMandate(Resource):

    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
