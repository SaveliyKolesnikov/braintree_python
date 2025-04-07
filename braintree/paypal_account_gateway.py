import braintree
from .paypal_account import PayPalAccount
from .error_result import ErrorResult
from .exceptions.not_found_error import NotFoundError
from .resource import Resource
from .successful_result import SuccessfulResult


class PayPalAccountGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def find(self, paypal_account_token):
        try:
            if paypal_account_token is None or paypal_account_token.strip() == "":
                raise NotFoundError()

            response = self.config.http().get(self.config.base_merchant_path() + "/payment_methods/paypal_account/" + paypal_account_token)
            if "paypal_account" in response:
                return PayPalAccount(self.gateway, response["paypal_account"])
        except NotFoundError:
            raise NotFoundError("paypal account with token " + repr(paypal_account_token) + " not found")

    def delete(self, paypal_account_token):
        self.config.http().delete(self.config.base_merchant_path() + "/payment_methods/paypal_account/" + paypal_account_token)
        return SuccessfulResult()

    def update(self, paypal_account_token, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, PayPalAccount.signature())
        response = self.config.http().put(self.config.base_merchant_path() + "/payment_methods/paypal_account/" + paypal_account_token, {"paypal_account": params})
        if "paypal_account" in response:
            return SuccessfulResult({"paypal_account": PayPalAccount(self.gateway, response["paypal_account"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])
