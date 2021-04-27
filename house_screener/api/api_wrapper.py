import configparser
import pprint

import requests

from house_screener.api.api_error import ApiConfigPropertyMissingException, ApiRequestException


class ApiWrapper:
    def __init__(self, api_key=None, url=None):
        config = configparser.ConfigParser()
        config.read("api-config.properties")
        # Rapid API host and secret
        try:
            self.__SECRET = config.get("API", "REALTOR_RAPID_API_KEY") if config.has_section("API") else api_key
            if not self.__SECRET: raise ApiConfigPropertyMissingException()
        except (configparser.NoSectionError, configparser.NoOptionError):
            raise ApiConfigPropertyMissingException()
        self.__host = config.get("API", "REALTOR_RAPID_API_HOST") \
            if config.has_option("API", "REALTOR_RAPID_API_HOST") \
            else "None "
        self.__headers = {
            'x-rapidapi-key': self.__SECRET,
            'x-rapidapi-host': self.__host
        }
        # Rapid API URLs
        self.for_sale_url = config.get("URL", "FOR_SALE_URL") if config.has_option("URL", "FOR_SALE_URL") else url
        self.sold_url = config.get("URL", "SOLD_URL") if config.has_option("URL", "SOLD_URL") else url
        self.by_mls_url = config.get("URL", "BY_MLS_URL") if config.has_option("URL", "BY_MLS_URL") else url
        self.for_rent_url = config.get("URL", "FOR_RENT_URL") if config.has_option("URL", "FOR_RENT_URL") else url
        if not self.for_sale_url: raise ApiConfigPropertyMissingException()

    def get(self, query_dict: dict, url=None):
        url = url or self.for_sale_url
        response = requests.get(url, headers=self.__headers, params=query_dict)
        if response.status_code >= 300:
            raise ApiRequestException()
        return response


if __name__ == "__main__":
    import json
    input_param = {"CurrentPage": "1", "LatitudeMin": "49.773437", "LongitudeMax": "-119.3199561",
                   "RecordsPerPage": "10", "LongitudeMin": "-119.589603", "LatitudeMax": "50.025948", "BedRange": "0-0",
                   "BathRange": "0-0", "NumberOfDays": "0", "CultureId": "1", "PriceMin": "0", "SortBy": "1",
                   "SortOrder": "A", "RentMin": "0"}  # for Kelowna city
    api_wrapper_instance = ApiWrapper()
    result = api_wrapper_instance.get(input_param)
    pprint.pprint(result.json())
    with open('data.txt', 'w') as f:
        json.dump(result.json(), f)
