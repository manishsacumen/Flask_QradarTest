# from test_app import MyTest
# from data_store import read_data_store
#
# current_config_access_key = {'access_key': 'xyz'}
# current_config_port_list = ['abc123', 'asd23d']
#
# app = MyTest.create_app()
#
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index')
# def test_index_with_access_key():
#     access_key = 'xyz'
#     assert access_key == current_config_access_key['access_key']
#
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index')
# def test_index_with_portfolio_list():
#     portfolio_list = ['abc123', 'asd23d']
#     assert portfolio_list == current_config_port_list
#
from flask import Flask
from mock import MagicMock
import mock
from app import views
import pytest
from conftest import client
from app.data_store import read_data_store


def test_index(client, mocker):
    read_data_store = MagicMock(return_value = {"Hello":"Hi"})
    url = '/' or '/index'
    response = client.get(url)
    assert response.status_code == 200

