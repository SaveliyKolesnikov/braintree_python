from app.library.braintree_python.braintree.error_result import ErrorResult
from app.library.braintree_python.braintree.resource import Resource
from app.library.braintree_python.braintree.resource_collection import ResourceCollection
from app.library.braintree_python.braintree.successful_result import SuccessfulResult
from app.library.braintree_python.braintree.exceptions.not_found_error import NotFoundError
from app.library.braintree_python.braintree.merchant import Merchant
from app.library.braintree_python.braintree.oauth_credentials import OAuthCredentials


class MerchantGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def create(self, params):
        return self.__create_merchant(params)

    def __create_merchant(self, params=None):
        if params is None:
            params = {}
        response = self.config.http().post("/merchants/create_via_api", {
            "merchant": params
        })

        if "response" in response and "merchant" in response["response"]:
            return SuccessfulResult({
                "merchant": Merchant(self.gateway, response["response"]["merchant"]),
                "credentials": OAuthCredentials(self.gateway, response["response"]["credentials"])
            })
        else:
            return ErrorResult(self.gateway, response["api_error_response"])

