from qpylib import qpylib
from data_store import read_data_store, update_data_store


class Helper:

    @staticmethod
    def log_debug(message=None):
        qpylib.log(message, level='debug')

    @staticmethod
    def log_critical(message=None):
        qpylib.log(message, level='critical')

    @staticmethod
    def log_info(message=None):
        qpylib.log(message, level='info')

    @staticmethod
    def log_warning(message=None):
        qpylib.log(message, level='warning')

    @staticmethod
    def log_error(message=None):
        qpylib.log(message, level='error')

    @staticmethod
    def get_check_point(key):
        current_config = read_data_store()
        if not current_config.get(key):
            check_point = ''
        else:
            check_point = current_config.get(key)
        return check_point

    @staticmethod
    def save_check_point(key, value):
        data = {key: value}
        update_data_store(data)
