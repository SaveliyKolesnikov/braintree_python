from .util.http import Http
import braintree
import warnings
from .exceptions.not_found_error import NotFoundError
from .resource_collection import ResourceCollection
from .successful_result import SuccessfulResult
from .error_result import ErrorResult
from .resource import Resource
from .configuration import Configuration

class SettlementBatchSummary(Resource):
    @staticmethod
    def generate(settlement_date, group_by_custom_field=None):
        return Configuration.gateway().settlement_batch_summary.generate(settlement_date, group_by_custom_field)
