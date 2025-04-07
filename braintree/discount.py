from .modification import Modification
from .configuration import Configuration


class Discount(Modification):

    @staticmethod
    def all():
        return Configuration.gateway().discount.all()
