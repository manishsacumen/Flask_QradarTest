from mock import MagicMock, patch
import requests_mock
from app.qpylib import qpylib
import pytest
from app.aes_crypt import AESCipher
from mock_data import (name, access_key, domain, url, level_overall_change, level_factor_change,
                       level_new_issue_change, portfolio_ids, fetch_historical_data, user_config)
import app
#
# @requests_mock.Mocker()
# class TestQradar:
#
#     def setup_mock(self, mock):
#         pass

import json
#ae_ob = AESCipher()

class AESCipher_cp(object):

    @staticmethod
    def __generate_key():
        """Generates and returns fernet key

        :return: str - key
        """
        # key = Fernet.generate_key()
        return 'key'

    def __get_key(self):

        data = {
            'secret_key': self.__generate_key()
        }
        return data.get('secret_key')

    def encrypt(self, raw):
        # enc = self.fernet.encrypt(bytes(raw))
        return 'a123bc'

    def decrypt(self, enc):
        return 'key'

@requests_mock.Mocker()
def test_qr(mock):
    qpylib.get_console_address = MagicMock(return_value=None)
    qpylib.log = MagicMock(return_value=None)
    from app.poll_n_write import process_events, QRadarThread
    process_events = MagicMock(return_value=True)
    qr_obj = QRadarThread(name, access_key, domain, url, level_overall_change, level_factor_change,
                          level_new_issue_change, portfolio_ids, fetch_historical_data, user_config)
    assert user_config['access_key'] == 'xyz'


@requests_mock.Mocker()
def test_qr_with_less_args(mock):
    qpylib.get_console_address = MagicMock(return_value=None)
    qpylib.log = MagicMock(return_value=None)
    from app.poll_n_write import process_events, QRadarThread
    process_events = MagicMock(return_value=True)
    with pytest.raises(TypeError):
        qr_obj = QRadarThread(name, access_key, domain, url, level_overall_change, level_factor_change,
                              level_new_issue_change, portfolio_ids, fetch_historical_data)




@patch('app.aes_crypt.AESCipher')
@patch('app.utils.validate_api_credentials')
@patch('app.data_store.update_data_store')
def test_poll_write_with_valid_api_key(mocker, mock_aescipher,mock_validate_api_credentials, mock_update_data_store ):
    qpylib.get_console_address = MagicMock(return_value=None)
    qpylib.log = MagicMock(return_value=None)
    app.aes_crypt.AESCipher =  MagicMock(return_value=None)
    app.aes_crypt.AESCipher.side_effect = side_effect
    from app.poll_n_write import read_data_store, poll_scorecard_n_write
    read_data_store = MagicMock(return_value=True)
    app.utils.validate_api_credentials = MagicMock(return_value= None)
    app.utils.validate_api_credentials.side_effect = side_effect_validate
    app.data_store.update_data_store  = MagicMock(return_value = None)
    app.data_store.update_data_store  =  side_effect_validate
    status, msg = poll_scorecard_n_write(access_key, domain, url, level_overall_change, level_factor_change,
                                         level_new_issue_change, portfolio_ids, fetch_historical_data,
                                         MONITOR_CONFIG={}, DIFF_OVERRIDE_CONFIG={}, proxy={})


    assert status == True

def side_effect():
    return AESCipher_cp()

def side_effect_validate():
    return None



