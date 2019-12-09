from collections import OrderedDict

from formatters import dict_to_kv_string


def test_dict_to_kv_string():
    ip = OrderedDict([
        ('key1', 'val1'),
        ('key2', 'val2'),
    ])
    op = "key1=val1 key2=val2"
    assert dict_to_kv_string(ip) == op

    # Test with single valued dict
    ip = OrderedDict([
        ('key1', 'val1'),
    ])
    op = "key1=val1"
    assert dict_to_kv_string(ip) == op

    # Test with empty dict
    assert dict_to_kv_string({}) == ""
