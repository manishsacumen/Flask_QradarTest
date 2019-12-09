from mock import MagicMock
import requests_mock
from app.qpylib import qpylib
import pytest
# from app.aes_crypt import AESCipher
from mock_data import (name, access_key, domain, url, level_overall_change, level_factor_change,
                       level_new_issue_change, portfolio_ids, fetch_historical_data, user_config)
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

@requests_mock.Mocker()
def test_poll_write_with_valid_api_key(mock):
    #ae_ob = AESCipher_cp()
    qpylib.get_console_address = MagicMock(return_value=None)
    qpylib.log = MagicMock(return_value=None)
    AESCipher_cp.ae_ob = MagicMock(return_value=None)
    from app.poll_n_write import read_data_store, AESCipher, poll_scorecard_n_write
    read_data_store = MagicMock(return_value=True)
    print("calling poll-----------")

    #enc_obj =
    # enc_obj.encrypt = MagicMock(return_value=None)
    validate_api_credentials = MagicMock(return_value=False)
    status, msg = poll_scorecard_n_write(access_key, domain, url, level_overall_change, level_factor_change,
                                         level_new_issue_change, portfolio_ids, fetch_historical_data,
                                         MONITOR_CONFIG={}, DIFF_OVERRIDE_CONFIG={}, proxy={})


    assert status == False


