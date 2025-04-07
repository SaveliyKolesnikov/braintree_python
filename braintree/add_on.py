from .configuration import Configuration
from .modification import Modification

class AddOn(Modification):
    @staticmethod
    def all():
        return Configuration.gateway().add_on.all()
