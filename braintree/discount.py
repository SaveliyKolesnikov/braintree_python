from app.library.braintree_python.braintree.modification import Modification
from app.library.braintree_python.braintree.configuration import Configuration


class Discount(Modification):

    @staticmethod
    def all():
        return Configuration.gateway().discount.all()
