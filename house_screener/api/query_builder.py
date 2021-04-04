import enum


class ParamOption(enum.Enum):
    CITY = "city",  # required
    LIMIT = "limit",  # required
    OFFSET = "offset",  # required
    STATE_CODE = "state_code",  # required
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

    def with_city(self, city: str):
        """The value of city field responded in locations/auto-complete API (do not use this parameter with
        postal_code)"""
        self.query[ParamOption.CITY] = city
        return self

    def with_limit(self, limit: int):
        """The number of items to be responded in every request"""
        self.query[ParamOption.LIMIT] = limit
        return self

    def with_offset(self, offset: int):
        """The offset of items to be ignored in response for paging"""
        self.query[ParamOption.OFFSET] = offset
        return self

    def with_state_code(self, state_code: str):
        """The value of state_code field responded in locations/auto-complete API (do not use this parameter with
        postal_code)"""
        self.query[ParamOption.STATE_CODE] = state_code
        return self

    def with_radius(self, radius):
        """Radius in miles to look for properties (1 to 20)"""
        self.query[ParamOption.RADIUS] = radius
        return self

    def with_baths_min(self, baths_min: int):
        """Min baths of properties"""
        self.query[ParamOption.BATHS_MIN] = baths_min
        return self

    def with_beds_min(self, beds_min: int):
        """Min beds of properties"""
        self.query[ParamOption.BEDS_MIN] = beds_min
        return self

    def with_price_min(self, price_min: int):
        """Option filter by setting min price"""
        self.query[ParamOption.PRICE_MIN] = price_min
        return self

    def with_price_max(self, price_max: int):
        """Option filter by setting max price"""
        self.query[ParamOption.PRICE_MAX] = price_max
        return self

    def with_postal_code(self, postal_code: str):
        """Zip code or postal code (do not use this parameter with city and state_code)"""
        self.query[ParamOption.POSTAL_CODE] = postal_code
        return self

    def with_sqft_min(self, sqft_min: int):
        """Min size of the properties"""
        self.query[ParamOption.SQFT_MIN] = sqft_min
        return self

    def with_sqft_max(self, sqft_max: int):
        """Max size of the properties"""
        self.query[ParamOption.SQFT_MAX] = sqft_max
        return self

    def with_age_min(self, age_min: int):
        """Max age of properties"""
        self.query[ParamOption.AGE_MIN] = age_min
        return self

    def with_age_max(self, age_max: int):
        """Min age of properties"""
        self.query[ParamOption.AGE_MAX] = age_max
        return self

    def with_lot_sqft_max(self, lot_sqft_max: int):
        """Max Lot/Acreage size"""
        self.query[ParamOption.LOT_SQFT_MAX] = lot_sqft_max
        return self

    def with_lot_sqft_min(self, lot_sqft_min: int):
        """Min Lot/Acreage size"""
        self.query[ParamOption.LOT_SQFT_MIN] = lot_sqft_min
        return self

    def with_prop_type(self, prop_type: str):
        """One of the followings (separated by comma for multiple values):
        single_family,multi_family,condo,mobile,land,farm,other"""
        self.query[ParamOption.PROP_TYPE] = prop_type
        return self

    def with_sort(self, sort: str):
        """One of the followings :
        relevance|newest|price_low|price_high|photos|open_house_date|sqft_high|price_reduced_date"""
        self.query[ParamOption.SORT] = sort
        return self

    def with_(self, param_name, param_value):
        """Add custom query parameters as needed"""
        self.query[param_name] = param_value
        return self

    def build(self) -> dict:
        return self.query
