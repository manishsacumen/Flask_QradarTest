from app import app
from app.utils import validate_api_credentials, get_json_from_url
from mock import MagicMock, patch
import requests
from app import app
import requests_mock
import mock
from mock_data import JSON_DATA
import json
from app.utils import build_leef

from app.utils import get_value_from_dict_list

def test_get_value_from_dict_list():
    assert get_value_from_dict_list([{'a':'app'}], 'a', 'app')



def test_get_value_from_dict_list1():
    assert None == get_value_from_dict_list([{}], 'a', 'app')

@requests_mock.mock()
def test_connect_to_ss(mock):
    headers = {
        'authorization': 'abc',
        'X-SSC-Application-Name': 'qwe',
        'X-SSC-Application-Version': '1.2',
    }


    mock.get("http://123-fake-api.com", text=json.dumps(JSON_DATA))

    response = get_json_from_url("http://123-fake-api.com", headers=headers, params=None, proxy=None)

    assert response == {"key": "value"}

items = {'diff':0, 'xyz':2}

def test_build_leaf():
    res = build_leef({}, 1, 'sacumn')
    assert res == ''

def test_build_leaf1():
    res = build_leef(items, 1, 'sacumen',)
    assert res == ''


def test_build_leaf2():
    res = build_leef(items, 1, 'sacumen', force_creation=True)
    assert res == 'LEEF:1.0|SECURITYSCORECARD IO|sacumen|1.0.0|1|xyz=2'



