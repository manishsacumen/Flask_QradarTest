from mock_data import CONFIG_VALUE_COMPLETE_DATA, CONFIG_VALUE_DATA_PORTFOLIO_LIST
import flask
from flask import Flask
from mock import MagicMock
import mock
from app import views
import pytest
from conftest import client
from app.data_store import read_data_store
import json
from flask import template_rendered
from contextlib import contextmanager
from app.flask_keys import get_flask_keys, random_word
import responses
import requests
from pytest_mock import mocker
from app import app, views
from mock_data import RESULT_DATA, RESULT_DATA1


class AESCipher(object):

    def decrypt(self, value):
        return str(value)


class TestViews(object):
    def test_index(self, client,mocker):

        mocker.patch('app.views.read_data_store', return_value=CONFIG_VALUE_COMPLETE_DATA)
        test_obj = AESCipher()
        mocker.patch('app.views.AESCipher', return_value=test_obj)
        mocker.patch('app.views.render_template', return_value="Get Called")
        url = '/' or '/index'
        response = client.get(url)
        assert response.get_data() == "Get Called"

    def test_index_portfolio_list(self, client, mocker):
        mocker.patch('app.views.read_data_store', return_value=CONFIG_VALUE_DATA_PORTFOLIO_LIST)
        test_obj = AESCipher()
        mocker.patch('app.views.AESCipher', return_value=test_obj)
        mocker.patch('app.views.render_template', return_value="Get Called")
        url = '/' or '/index'
        response = client.get(url)
        assert response.get_data() == "Get Called"

    # def test_post_call(self, client, mocker):
    #     mocker.patch('app.views.read_data_store', return_value=CONFIG_VALUE_COMPLETE_DATA)
    #     test_obj = AESCipher()
    #     mocker.patch('app.views.AESCipher', return_value=test_obj)
    #     mocker.patch('app.views.render_template', return_value="Post Called")
    #     url = '/'
    #     response = client.post(url, data={"Hello": "hi", "csrf_token": False})
    #     print(response.data)
