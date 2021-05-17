import random

import pandas
import pytest
from requests.models import Response

from house_screener.api.api_error import ApiRequestException
from house_screener.api.response_processor import parse_response

keys = ['Building', 'Id', 'Land', 'MlsNumber', 'Property', 'PostalCode']


def test_error_status_code_throw_apiresponseexception():
    test_response = Response()
    test_response.code = "expired"
    test_response.error_type = "expired"
    test_response.status_code = 400

    with pytest.raises(ApiRequestException):
        parse_response(test_response)


def test_returns_pandas_dataframe():
    test_response = MockResponse()
    test_response.status_code = 200
    result = parse_response(test_response)
    assert isinstance(result, pandas.DataFrame)
    assert set(keys).issubset(set(result.columns))


class MockResponse(Response):
    def json(self):
        return {"Results": [{k: random.random() for k in keys}]}
