import pytest
import requests_mock

from house_screener.api.api_error import ApiRequestException
from ..api.api_wrapper import ApiWrapper
from ..api.query_builder import QueryBuilder

query = QueryBuilder().with_city("Kelowna").build()


def test_wrapper_get_successful_request():
    """Tests an API call to get houses for sale"""
    wrapper_instance = ApiWrapper(api_key="random-key", url="http://random-url")
    with requests_mock.Mocker() as m:
        adapter = m.get(wrapper_instance.for_sale_url,
                        complete_qs=False,
                        json={'name': 'awesome-mock'})
        response = wrapper_instance.get(query)
    assert response.json() == {'name': 'awesome-mock'}
    assert adapter.call_count == 1


def test_wrapper_get_bad_request():
    wrapper_instance = ApiWrapper(api_key="random-key", url="http://random-url")
    with requests_mock.Mocker() as m:
        m.get(wrapper_instance.for_sale_url,
              complete_qs=False,
              status_code=404)
        with pytest.raises(ApiRequestException):
            wrapper_instance.get(query)
