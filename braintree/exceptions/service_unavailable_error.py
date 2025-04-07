from app.library.braintree_python.braintree.exceptions.braintree_error import BraintreeError

class ServiceUnavailableError(BraintreeError):
    """
    Raised when the gateway is unavailable.
    """
    pass
