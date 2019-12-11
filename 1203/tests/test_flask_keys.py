from app import flask_keys
import mock
import json
import pytest

class TestFlaskKeys(object):
    def test_flask_keys(self):
        read_data = json.dumps({'a': 1, 'b': 2, 'c': 3})
        mock_open = mock.mock_open(read_data=read_data)
        with mock.patch('app.flask_keys.open', mock_open):
            data = flask_keys.get_flask_keys()
            assert "a" in data

    def test_flask_keys1(self):
        with pytest.raises(IOError):
            flask_keys.get_flask_keys()

