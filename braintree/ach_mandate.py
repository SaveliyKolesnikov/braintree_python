import braintree
from .util.datetime_parser import parse_datetime
from .resource import Resource

class AchMandate(Resource):

    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
