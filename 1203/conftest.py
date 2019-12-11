import os, sys

import pytest
from mock import MagicMock
#from app import create_app
from tests.qplib import QpLib
from mock import patch, MagicMock
# from app.flask_keys import get_flask_keys
qpylib = QpLib()
create_log = qpylib.create_log()
from app import app


@pytest.fixture
def app_name(mocker):
    """Create and configure a new app instance for each test."""
    #from app import create_app
    #qpylib = MagicMock(return_value=create_log)
    get_flask_keys = MagicMock(return_value='data')
    #mocker.patch('app.poll_n_write.poll_scorecard_n_write', return_value=(True, "Success"))
    #mocker.patch('app.get_flask_keys.get_flask_keys.create_log', return_value=create_log)

    #app = create_app()
    flask_app = app
    yield flask_app


@pytest.fixture
def client(app_name):
    """A test client for the app."""
    client = app_name.test_client()
    return client


@pytest.fixture
def runner(app_name):
    """A test runner for the app's Click commands."""
    return app_name.test_cli_runner()

# @pytest.fixture
# def qplib_obj():
#     qp_ob = QpLib()
#     #mocker.patch('app.poll_n_write.qpylib.get_console_address', return_value=qp_ob.get_console_address())
#     app.poll_n_write.qpylib.get_console_address = MagicMock(return_value=qp_ob.get_console_address())


@pytest.fixture
def mock_aescipher(app_name):
    return None

@pytest.fixture
def mock_validate_api_credentials(app_name):
    return None

@pytest.fixture
def mock_update_data_store(app_name):
    return None
#
