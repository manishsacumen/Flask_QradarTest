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
# def test_index(client):
#     # read_data_store = MagicMock(return_value = {"Hello":"Hi"})
#     url = '/' or '/index'
#     response = client.get(url)
#     assert response.status_code == 200


# def test_result2(client, mocker):
#     from app.qpylib import qpylib
#     qpylib.get_console_address = MagicMock(return_value=None)
#     qpylib.log = MagicMock(return_value=None)
#
#     data = {'secret_key': random_word(), 'token': random_word()}
#
#     mocker.patch('app.flask_keys.get_flask_keys', return_value=data)
#     mocker.patch('app.views.render_template', return_value="Get Called")
#     mocker.patch('app.poll_n_write.poll_scorecard_n_write', return_value=True)
#     mocker.patch('app.poll_n_write.poll_scorecard_n_write', return_value=None)
#     RESULT_DATA1.update(({"csrf_token": False}))
#
#     request_mock = mocker.patch.object(flask, "request")
#     request_mock.form.get.return_value = RESULT_DATA1
#     url = '/result'
#
#     response, msg = client.post(url, data=json.dumps(RESULT_DATA1))

    # assert response.status_code == 403

