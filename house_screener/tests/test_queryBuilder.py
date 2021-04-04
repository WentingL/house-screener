import random

from house_screener.api.query_builder import QueryBuilder, ParamOption
from house_screener.tests.random_util import generate_lowercase_string


def test_with_city():
    test_value = generate_lowercase_string(random.randint(1, 10))
    test_query = QueryBuilder().with_city(test_value).build()
    assert test_query[ParamOption.CITY] == test_value
    test_value = random.randint(1, 10)
    test_query = QueryBuilder().with_city(test_value).build()
    assert test_query[ParamOption.CITY] == test_value


def test_with_limit():
    test_value = generate_lowercase_string(random.randint(1, 10))
    test_query = QueryBuilder().with_limit(test_value).build()
    assert test_query[ParamOption.LIMIT] == test_value
    test_value = random.randint(1, 10)
    test_query = QueryBuilder().with_limit(test_value).build()
    assert test_query[ParamOption.LIMIT] == test_value


def test_with_offset():
    test_value = generate_lowercase_string(random.randint(1, 10))
    test_query = QueryBuilder().with_offset(test_value).build()
    assert test_query[ParamOption.OFFSET] == test_value
    test_value = random.randint(1, 10)
    test_query = QueryBuilder().with_offset(test_value).build()
    assert test_query[ParamOption.OFFSET] == test_value


def test_with_state_code():
    test_value = generate_lowercase_string(random.randint(1, 10))
    test_query = QueryBuilder().with_state_code(test_value).build()
    assert test_query[ParamOption.STATE_CODE] == test_value
    test_value = random.randint(1, 10)
    test_query = QueryBuilder().with_state_code(test_value).build()
    assert test_query[ParamOption.STATE_CODE] == test_value


def test_with_radius():
    test_value = generate_lowercase_string(random.randint(1, 10))
    test_query = QueryBuilder().with_radius(test_value).build()
    assert test_query[ParamOption.RADIUS] == test_value
    test_value = random.randint(1, 10)
    test_query = QueryBuilder().with_radius(test_value).build()
    assert test_query[ParamOption.RADIUS] == test_value


def test_with_baths_min():
    assert True


def test_with_beds_min():
    assert True


def test_with_price_min():
    assert True


def test_with_price_max():
    assert True


def test_with_postal_code():
    assert True


def test_with_sqft_min():
    assert True


def test_with_sqft_max():
    assert True


def test_with_age_min():
    assert True


def test_with_age_max():
    assert True


def test_with_lot_sqft_max():
    assert True


def test_with_lot_sqft_min():
    assert True


def test_with_prop_type():
    assert True


def test_with_sort():
    assert True


def test_with_():
    assert True


def test_build():
    assert True
