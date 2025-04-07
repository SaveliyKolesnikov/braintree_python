import app.library.braintree_python.braintree as braintree
from app.library.braintree_python.braintree.resource import Resource

class UnknownPaymentMethod(Resource):
    def image_url(self):
        return "https://assets.braintreegateway.com/payment_method_logo/unknown.png"
