import pandas as pd
from requests import Response

from house_screener.api.api_error import ApiRequestException

keys = ['Building', 'Id', 'Land', 'MlsNumber', 'Property', 'PostalCode']


def parse_response(response_to_parse: Response) -> pd.DataFrame:
    if response_to_parse.status_code >= 300: raise ApiRequestException()
    results = response_to_parse.json()
    if results['Results']:
        results = results['Results']
        print(results)
        new_results = [{k: element[k] for k in keys} for element in results]

    df = pd.DataFrame(new_results, columns=keys)
    print(df)
    return df
