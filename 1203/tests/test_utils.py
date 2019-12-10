from flask import Flask
from app import app
from app.utils import validate_api_credentials, get_json_from_url
from mock import MagicMock, patch
import requests
from app import app
import requests_mock
import mock
from mock_data import JSON_DATA
import json

class TestUtilsObject(object):

    def test_validate_api_credentials(self):

        url = "https://api.securityscorecard.io"
        token = "gAAAAABd5PaRpM3BxeTZl4L-tOU6Hszd_yo7zWSpQufwm2SaQITczdA"

        validate_api_credentials = MagicMock(return_value=[200, 429])

        if validate_api_credentials.status_code in [200, 429]:
            assert validate_api_credentials(url, token) == True

    @requests_mock.mock()
    def test_get_json_from_url(self, mock):

        mock.get("http://123-fake-api.com", text=json.dumps(JSON_DATA))

        response = get_json_from_url("http://123-fake-api.com", headers=None, params=None, proxy=None)

        assert response == {"key": "value"}





