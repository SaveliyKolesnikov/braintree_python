from app.library.braintree_python.braintree.configuration import Configuration
from app.library.braintree_python.braintree.modification import Modification

class AddOn(Modification):
    @staticmethod
    def all():
        return Configuration.gateway().add_on.all()
