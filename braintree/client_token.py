import datetime
import json
import urllib
from .configuration import Configuration
from .signature_service import SignatureService
from .util.crypto import Crypto
from . import exceptions


class ClientToken(object):

    @staticmethod
    def generate(params=None, gateway=None):
        if params is None:
            params = {}
        if gateway is None:
            gateway = Configuration.gateway().client_token

        return gateway.generate(params)

    @staticmethod
    def generate_signature():
        return [
            "customer_id",
            "merchant_account_id",
            "proxy_merchant_id",
            "version",
            {"domains": ["__any_key__"]},
            {"options": ["fail_on_duplicate_payment_method", "fail_on_duplicate_payment_method_for_customer", "make_default", "verify_card"]}
        ]
