from app.braintree.util.http import Http
import app.braintree as braintree
import warnings
from app.braintree.exceptions.not_found_error import NotFoundError
from app.braintree.resource_collection import ResourceCollection
from app.braintree.successful_result import SuccessfulResult
from app.braintree.error_result import ErrorResult
from app.braintree.resource import Resource
from app.braintree.configuration import Configuration

class SettlementBatchSummary(Resource):
    @staticmethod
    def generate(settlement_date, group_by_custom_field=None):
        return Configuration.gateway().settlement_batch_summary.generate(settlement_date, group_by_custom_field)
