from .add_on_gateway import AddOnGateway
from .address_gateway import AddressGateway
from .apple_pay_gateway import ApplePayGateway
from .client_token_gateway import ClientTokenGateway
from .configuration import Configuration
from .credit_card_gateway import CreditCardGateway
from .credit_card_verification_gateway import CreditCardVerificationGateway
from .customer_gateway import CustomerGateway
from .customer_session_gateway import CustomerSessionGateway
from .discount_gateway import DiscountGateway
from .dispute_gateway import DisputeGateway
from .document_upload_gateway import DocumentUploadGateway
from .exchange_rate_quote_gateway import ExchangeRateQuoteGateway
from .merchant_account_gateway import MerchantAccountGateway
from .merchant_gateway import MerchantGateway
from .oauth_gateway import OAuthGateway
from .payment_method_gateway import PaymentMethodGateway
from .payment_method_nonce_gateway import PaymentMethodNonceGateway
from .paypal_account_gateway import PayPalAccountGateway
from .paypal_payment_resource_gateway import PayPalPaymentResourceGateway
from .sepa_direct_debit_account_gateway import SepaDirectDebitAccountGateway
from .plan_gateway import PlanGateway
from .settlement_batch_summary_gateway import SettlementBatchSummaryGateway
from .subscription_gateway import SubscriptionGateway
from .testing_gateway import TestingGateway
from .transaction_gateway import TransactionGateway
from .transaction_line_item_gateway import TransactionLineItemGateway
from .us_bank_account_gateway import UsBankAccountGateway
from .us_bank_account_verification_gateway import UsBankAccountVerificationGateway
from .webhook_notification_gateway import WebhookNotificationGateway
from .webhook_testing_gateway import WebhookTestingGateway
from .configuration import Configuration
class BraintreeGateway(object):
    def __init__(self, config=None, **kwargs):
        if isinstance(config, Configuration):
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
