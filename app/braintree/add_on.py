from app.braintree.configuration import Configuration
from app.braintree.modification import Modification

class AddOn(Modification):
    @staticmethod
    def all():
        return Configuration.gateway().add_on.all()
