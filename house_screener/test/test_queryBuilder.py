import random

import pytest

from house_screener.api.query_builder import QueryBuilder, ParamOption
from house_screener.test.random_util import generate_lowercase_string


@pytest.fixture
def setup_before_each():
    test_str_value = generate_lowercase_string(random.randint(1, 10))
    test_int_value = random.randint(1, 10)
    rand_enum = random.choice([param.name for param in ParamOption])
    yield test_str_value, test_int_value, rand_enum


def test_with_str_value(setup_before_each):
    test_str,test_int,rand_enum = setup_before_each
    test_query = QueryBuilder().with_param(rand_enum, test_str).build()
    assert test_query[rand_enum] == test_str
    assert isinstance(test_query[rand_enum], str)


def test_with_int_value(setup_before_each):
    test_str,test_int,rand_enum = setup_before_each
    test_query = QueryBuilder().with_param(rand_enum, test_int).build()
    assert test_query[rand_enum] == str(test_int)
    assert isinstance(test_query[rand_enum], str)


def test_build():
    assert True
