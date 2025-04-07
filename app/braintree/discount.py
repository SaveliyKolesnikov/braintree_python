from app.braintree.modification import Modification
from app.braintree.configuration import Configuration


class Discount(Modification):

    @staticmethod
    def all():
        return Configuration.gateway().discount.all()
