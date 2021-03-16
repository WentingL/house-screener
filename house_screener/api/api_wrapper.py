import configparser

import requests


class APIConfigPropertyMissingException(Exception):
    pass


class ApiWrapper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('api-config.properties')
        # Rapid API host and secret
        self.__SECRET = config.get("API", "REALTOR_RAPID_API_KEY")
        if self.__SECRET is "":
            raise APIConfigPropertyMissingException()
        self.__host = config.get("API", "REALTOR_RAPID_API_HOST")
        self.__headers = {
            'x-rapidapi-key': self.__SECRET,
            'x-rapidapi-host': self.__host
        }
        # Rapid API URLs
        self.for_sale_url = config.get("URL", "FOR_SALE_URL")
        self.sold_url = config.get("URL", "SOLD_URL")
        self.by_mls_url = config.get("URL", "BY_MLS_URL")
        self.for_rent_url = config.get("URL", "FOR_RENT_URL")

    def get_for_sale(self, query_string):
        response = requests.request("GET", self.for_sale_url, headers=self.__headers, params=query_string)
        return response

    def get_sold(self, query_string):
        response = requests.request("GET", self.sold_url, headers=self.__headers, params=query_string)
        return response

    def get_by_mls(self, query_string):
        response = requests.request("GET", self.by_mls_url, headers=self.__headers, params=query_string)
        return response

    def get_for_rent(self, query_string):
        response = requests.request("GET", self.for_rent_url, headers=self.__headers, params=query_string)
        return response


if __name__ == "__main__":
    input_param = {"city": "New York City", "offset": "0", "limit": "200", "state_code": "NY", "sort": "relevance"}
    api_wrapper_instance = ApiWrapper()
    result = api_wrapper_instance.get_for_sale(input_param)
    print(result.text)
