from splunk_utils import extract_input_fields
from tests.mockers import Helper


class TestExtractInputFields(object):
    data = {
        'key1': 'val1',
        'key2': 'val2',
    }

    def test_extract_input_fields(self):
        helper = Helper(**self.data)
        fields = ['key1', 'key2', 'key3']

        options = extract_input_fields(helper, fields)

        assert len(options) == len(fields) + 2  # +2 to include portfolio ids and proxy
        assert options.get('key1') == self.data['key1']
        assert options.get('key2') == self.data['key2']
        assert options.get('key3') is None
        assert options.get('portfolio_ids') is None
        assert options.get('proxy') == {}

    def test_with_all_portfolios(self):
        data = self.data.copy()
        data['portfolio_ids'] = 'all'
        fields = ['portfolio_ids']

        helper = Helper(**data)
        options = extract_input_fields(helper, fields)

        assert options.get('portfolio_ids') == 'all'

    def test_with_specific_portfolio_ids(self):
        data = self.data.copy()
        p1 = '123abc'
        p2 = '789xyz'
        data['portfolio_ids'] = ' {},{}, '.format(p1, p2)
        fields = ['portfolio_ids']

        helper = Helper(**data)
        options = extract_input_fields(helper, fields)
        assert options.get('portfolio_ids') == [p1, p2]

    def test_with_proxy_settings_with_username_and_password(self):
        proxy = {
            'proxy_type': 'https',
            'proxy_username': 'user',
            'proxy_password': 'pass',
            'proxy_url': 'example.com',
            'proxy_port': '8080'
        }
        data = self.data.copy()
        data['proxy'] = proxy
        fields = ['key1', 'key2']
        helper = Helper(**data)
        options = extract_input_fields(helper, fields)

        assert options['proxy']['http'] == 'https://user:pass@example.com:8080'
        assert options['proxy']['https'] == 'https://user:pass@example.com:8080'

    def test_with_proxy_settings_without_username_and_password(self):
        proxy = {
            'proxy_type': 'https',
            'proxy_url': 'example.com',
            'proxy_port': '8080'
        }
        data = self.data.copy()
        data['proxy'] = proxy
        fields = ['key1', 'key2']
        helper = Helper(**data)
        options = extract_input_fields(helper, fields)

        assert options['proxy']['http'] == 'https://example.com:8080'
        assert options['proxy']['https'] == 'https://example.com:8080'
