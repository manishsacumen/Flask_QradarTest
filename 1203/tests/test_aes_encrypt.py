import __builtin__
import requests_mock, os
from mock import MagicMock

@requests_mock.Mocker
class TestListWindowsPasswords():
    def setUp(self, mock):
        self._orig_pathexists = os.path.exists
        os.path.exists = MagicMock(True)

    def test_dump(self):
        with patch('__builtin__.open', unittest.mock.mock_open()) as m:
            data_writer = WriteData(
                dir='/my/path/not/exists',
                name='Foo'
            )
            data_writer.dump()

        self.assertEqual(os.path.exists.received_args[0], '/my/path/not/exists')  # fixed
        m.assert_called_once_with('/my/path/not/exists/output.text', 'w+')
        handle = m()
        handle.write.assert_called_once_with('Hello, Foo!')