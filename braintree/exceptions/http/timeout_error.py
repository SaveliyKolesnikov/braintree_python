from app.library.braintree_python.braintree.exceptions.unexpected_error import UnexpectedError

class TimeoutError(UnexpectedError):
    pass


class ConnectTimeoutError(TimeoutError):
    pass


class ReadTimeoutError(TimeoutError):
    pass
