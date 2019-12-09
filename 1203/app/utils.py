__author__ = 'Sacumen(www.sacumen.com)'

"""utils module

Contains helper functions used by application
"""

from functools import reduce
from config import LEEF_HEADER, PRODUCT_VERSION
import requests

from scorecard_exceptions import InvalidAPIKeyError, ResourceNotFoundError, InvalidJSONError, ServerError


def get_json_from_url(url, headers=None, params=None, proxy=None):
    """Creates json response from url

    :param url: str, url to call
    :param headers: dict, Optional custom headers
    :param params: dict, url parameters
    :param proxy: dict
    :return: object, json data from api mapped to equivalent python objects
    """
    headers = headers or {}
    params = params or {}

    try:
        if proxy:
            req = requests.get(url, headers=headers, params=params, proxies=proxy)
        else:
            req = requests.get(url, headers=headers, params=params)
    except Exception as e:
        raise Exception("Error in connecting to {}\nProxy: {}.\n{}".format(url, proxy, str(e)))

    try:
        rv = req.json()
    except ValueError as e:
        raise InvalidJSONError("URL: {}\nheaders: {}\nparams: {}\nstatus code: {}\nContent: {}".format(
            url,
            headers,
            params,
            req.status_code,
            req.content
        ))

    if req.status_code == 401:
        raise InvalidAPIKeyError("URL: {}\nheaders: {}\nparams: {}\nstatus code: {}\nContent: {}".format(
            url,
            headers,
            params,
            req.status_code,
            req.content
        ))

    if req.status_code == 404:
        raise ResourceNotFoundError("URL: {}\nheaders: {}\nparams: {}\nstatus code: {}\nContent: {}".format(
            url,
            headers,
            params,
            req.status_code,
            req.content
        ))

    if req.status_code == 502:
        raise ServerError("URL: {}\nheaders: {}\nparams: {}\nstatus code: {}\nContent: {}".format(
            url,
            headers,
            params,
            req.status_code,
            req.content
        ))

    if req.status_code != 200:
        raise requests.RequestException("URL: {} Received status {} with content {}.\n Headers {}, Params {}".format(
            url, req.status_code, req.content, headers, params))
    return rv


def connect_to_ss(url, token, params=None, proxy=None):
    """Connect to ss api and returns json data

    :param url: str
    :param token: str
    :param params: dict, url parameters
    :param proxy: dict
    :return: json
    """
    headers = {
        'authorization': 'Token {}'.format(token),
        'X-SSC-Application-Name': 'QRadar',
        'X-SSC-Application-Version': '1.0',
    }
    rv = get_json_from_url(url, headers, params, proxy)
    return rv


def get_value_from_dict_list(iterable, key, value):
    """Checks the key exists and matches with the value in a iterable of dicts,
    and returns it if present

    :param iterable:
    :param key: str, Key to check
    :param value: str, value to check
    :return: dict if present else None
    """
    for item in iterable:
        if key in item.keys() and item[key] == value:
            return item

    return None


def build_leef(items, event_id, product, force_creation=False):
    """Builds leef string from dict

    There should be an integer value in items with key diff. Leef is built only if the value of
    diff is negative or the flag force_creation is set. All the data passed in items except diff
    will become a key value pair in leef string

    :param items: dict, key-value pairs to include in leef
    :param event_id: event id to be included in leef header
    :param product: product id to be included in leef header
    :param force_creation: boolean, forces creation of leef even if the diff is non negative
    :return: str
    """
    if not items:
        return ''

    # Prevent leef creation if score is not changed
    if not force_creation and items['diff'] == 0:
        #print("Diff is 0 and override is not set. Skipping leef building")
        return ''

    # Remove diff from items
    del items['diff']

    leef = '{}|{}|{}|{}|'.format(LEEF_HEADER, product, PRODUCT_VERSION, event_id)
    leef = reduce(lambda acc, key: "{}{}={}\t".format(acc, key, items[key]), items.keys(), leef)
    return leef.strip()


def validate_api_credentials(token, url):
    """ Validate api credentials by calling a test url

    :param token: str
    :param url: str
    :return: boolean
    """

    headers = {'authorization': 'Token {}'.format(token)}
    test_url = '{}/metadata/factors'.format(url)

    r = requests.get(test_url, headers=headers)

    return r.status_code in [200, 429]

