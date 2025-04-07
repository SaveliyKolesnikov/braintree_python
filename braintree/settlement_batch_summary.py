from app.library.braintree_python.braintree.util.http import Http
import app.library.braintree_python.braintree as braintree
import warnings
from app.library.braintree_python.braintree.exceptions.not_found_error import NotFoundError
from app.library.braintree_python.braintree.resource_collection import ResourceCollection
from app.library.braintree_python.braintree.successful_result import SuccessfulResult
from app.library.braintree_python.braintree.error_result import ErrorResult
from app.library.braintree_python.braintree.resource import Resource
from app.library.braintree_python.braintree.configuration import Configuration

class SettlementBatchSummary(Resource):
    @staticmethod
    def generate(settlement_date, group_by_custom_field=None):
        return Configuration.gateway().settlement_batch_summary.generate(settlement_date, group_by_custom_field)
