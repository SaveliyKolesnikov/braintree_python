from app.library.braintree_python.braintree.add_on_gateway import AddOnGateway
from app.library.braintree_python.braintree.address_gateway import AddressGateway
from app.library.braintree_python.braintree.apple_pay_gateway import ApplePayGateway
from app.library.braintree_python.braintree.client_token_gateway import ClientTokenGateway
from app.library.braintree_python.braintree.configuration import Configuration
from app.library.braintree_python.braintree.credit_card_gateway import CreditCardGateway
from app.library.braintree_python.braintree.credit_card_verification_gateway import CreditCardVerificationGateway
from app.library.braintree_python.braintree.customer_gateway import CustomerGateway
from app.library.braintree_python.braintree.customer_session_gateway import CustomerSessionGateway
from app.library.braintree_python.braintree.discount_gateway import DiscountGateway
from app.library.braintree_python.braintree.dispute_gateway import DisputeGateway
from app.library.braintree_python.braintree.document_upload_gateway import DocumentUploadGateway
from app.library.braintree_python.braintree.exchange_rate_quote_gateway import ExchangeRateQuoteGateway
from app.library.braintree_python.braintree.merchant_account_gateway import MerchantAccountGateway
from app.library.braintree_python.braintree.merchant_gateway import MerchantGateway
from app.library.braintree_python.braintree.oauth_gateway import OAuthGateway
from app.library.braintree_python.braintree.payment_method_gateway import PaymentMethodGateway
from app.library.braintree_python.braintree.payment_method_nonce_gateway import PaymentMethodNonceGateway
from app.library.braintree_python.braintree.paypal_account_gateway import PayPalAccountGateway
from app.library.braintree_python.braintree.paypal_payment_resource_gateway import PayPalPaymentResourceGateway
from app.library.braintree_python.braintree.sepa_direct_debit_account_gateway import SepaDirectDebitAccountGateway
from app.library.braintree_python.braintree.plan_gateway import PlanGateway
from app.library.braintree_python.braintree.settlement_batch_summary_gateway import SettlementBatchSummaryGateway
from app.library.braintree_python.braintree.subscription_gateway import SubscriptionGateway
from app.library.braintree_python.braintree.testing_gateway import TestingGateway
from app.library.braintree_python.braintree.transaction_gateway import TransactionGateway
from app.library.braintree_python.braintree.transaction_line_item_gateway import TransactionLineItemGateway
from app.library.braintree_python.braintree.us_bank_account_gateway import UsBankAccountGateway
from app.library.braintree_python.braintree.us_bank_account_verification_gateway import UsBankAccountVerificationGateway
from app.library.braintree_python.braintree.webhook_notification_gateway import WebhookNotificationGateway
from app.library.braintree_python.braintree.webhook_testing_gateway import WebhookTestingGateway
import braintree.configuration

class BraintreeGateway(object):
    def __init__(self, config=None, **kwargs):
        if isinstance(config, braintree.configuration.Configuration):
            self.config = config
        else:
            self.config = Configuration(
                client_id=kwargs.get("client_id"),
                client_secret=kwargs.get("client_secret"),
                access_token=kwargs.get("access_token"),
                http_strategy=kwargs.get("http_strategy")
            )
        self.graphql_client = self.config.graphql_client()

        self.add_on = AddOnGateway(self)
        self.address = AddressGateway(self)
        self.apple_pay = ApplePayGateway(self)
        self.client_token = ClientTokenGateway(self)
        self.credit_card = CreditCardGateway(self)
        self.customer = CustomerGateway(self)
        self.customer_session = CustomerSessionGateway(self)
        self.discount = DiscountGateway(self)
        self.dispute = DisputeGateway(self)
        self.document_upload = DocumentUploadGateway(self)
        self.exchange_rate_quote = ExchangeRateQuoteGateway(self)
        self.merchant = MerchantGateway(self)
        self.merchant_account = MerchantAccountGateway(self)
        self.oauth = OAuthGateway(self)
        self.payment_method = PaymentMethodGateway(self)
        self.payment_method_nonce = PaymentMethodNonceGateway(self)
        self.paypal_account = PayPalAccountGateway(self)
        self.paypal_payment_resource = PayPalPaymentResourceGateway(self)
        self.plan = PlanGateway(self)
        self.sepa_direct_debit_account = SepaDirectDebitAccountGateway(self)
        self.settlement_batch_summary = SettlementBatchSummaryGateway(self)
        self.subscription = SubscriptionGateway(self)
        self.testing = TestingGateway(self)
        self.transaction = TransactionGateway(self)
        self.transaction_line_item = TransactionLineItemGateway(self)
        self.us_bank_account = UsBankAccountGateway(self)
        self.us_bank_account_verification = UsBankAccountVerificationGateway(self)
        self.verification = CreditCardVerificationGateway(self)
        self.webhook_notification = WebhookNotificationGateway(self)
        self.webhook_testing = WebhookTestingGateway(self)
