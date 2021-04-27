import enum


class ParamOption(enum.Enum):
    """This class stores potential query parameter options."""
    # Required params for Realtor - Canadian Real Estate API
    LATITUDE_MIN = "LatitudeMin",
    LATITUDE_MAX = "LatitudeMax",
    LONGITUDE_MIN = "LongitudeMin",
    LONGITUDE_MAX = "LongitudeMax",
    RECORDS_PER_PAGE = "RecordsPerPage",
    CURRENT_PAGE = "CurrentPage",

    # Required params for Realtor API
    CITY = "city",
    LIMIT = "limit",
    OFFSET = "offset",
    STATE_CODE = "state_code",

    # Optional params for Realtor API
    RADIUS = "radius",
    BATHS_MIN = "baths_min",
    BEDS_MIN = "beds_min",
    PRICE_MIN = "price_min",
    PRICE_MAX = "price_max",
    POSTAL_CODE = "postal_code",
    SQFT_MIN = "sqft_min",
    SQFT_MAX = "sqft_max",
    AGE_MIN = "age_min",
    AGE_MAX = "age_max",
    LOT_SQFT_MAX = "lot_sqft_max",
    LOT_SQFT_MIN = "lot_sqft_min",
    PROP_TYPE = "prop_type",
    SORT = "sort"


class QueryBuilder(object):
    def __init__(self):
        self.query = {}

    def with_param(self, param_name: str, param_value):
        """Add custom query parameters as needed"""
        self.query[param_name] = str(param_value)
        return self

    def build(self) -> dict:
        return self.query
