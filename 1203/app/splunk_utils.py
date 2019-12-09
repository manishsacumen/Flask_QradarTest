import datetime

from scorecard import Portfolio
from scorecard_exceptions import InvalidJSONError, ServerError


def build_proxy_dict(proxy_settings):
    if proxy_settings:
        proxy_type = proxy_settings['proxy_type']
        if proxy_settings.get('username') and proxy_settings.get('password'):
            proxy = {
                'http': '{proxy_type}://{user}:{password}@{host}:{port}'.format(
                    proxy_type=proxy_type,
                    user=proxy_settings['proxy_username'],
                    password=proxy_settings['proxy_password'],
                    host=proxy_settings['proxy_url'],
                    port=proxy_settings['proxy_port'],
                ),
                'https': '{proxy_type}://{user}:{password}@{host}:{port}'.format(
                    proxy_type=proxy_type,
                    user=proxy_settings['proxy_username'],
                    password=proxy_settings['proxy_password'],
                    host=proxy_settings['proxy_url'],
                    port=proxy_settings['proxy_port'],
                ),
            }
        else:
            proxy = {
                'http': '{proxy_type}://{host}:{port}'.format(
                    proxy_type=proxy_type,
                    host=proxy_settings['proxy_url'],
                    port=proxy_settings['proxy_port'],
                ),
                'https': '{proxy_type}://{host}:{port}'.format(
                    proxy_type=proxy_type,
                    host=proxy_settings['proxy_url'],
                    port=proxy_settings['proxy_port'],
                ),
        }
    else:
        proxy = {}

    return proxy


def format_portfolio_ids(portfolio_ids):
    try:
        # Python 2.7
        is_string = isinstance(portfolio_ids, unicode)
    except NameError:
        # Python 3
        is_string = isinstance(portfolio_ids, str)

    if is_string and portfolio_ids.strip().strip(',').lower() == 'all':
        portfolio_ids = 'all'
    elif is_string:
        portfolio_ids = portfolio_ids.strip().strip(',')
        portfolio_ids = portfolio_ids.split(',') if portfolio_ids else None

    return portfolio_ids


def extract_input_fields(helper, fields):
    inputs = {}
    for field in fields:
        inputs[field] = helper.get_arg(field)

    proxy_settings = helper.get_proxy()
    inputs['proxy'] = build_proxy_dict(proxy_settings)
    message = 'Proxy settings found' if inputs['proxy'] else 'No proxy settings found'
    helper.log_info(message)

    inputs['portfolio_ids'] = format_portfolio_ids(inputs.get('portfolio_ids'))

    if not inputs['portfolio_ids']:
        helper.log_warning('No portfolio ids received. Fetching data from portfolio companies will be skipped')
    elif inputs['portfolio_ids'] == 'all':
        helper.log_info('Data from all portfolio companies will be fetched')
    else:
        helper.log_info('Data from following portfolios will be fetched.\n{}'.format(inputs['portfolio_ids']))

    return inputs


def build_portfolio(helper, access_key, ids, **config):
    try:
        portfolio = Portfolio(access_key, ids, **config)
    except InvalidJSONError as e:
        helper.log_error("Data received from API is not in JSON format.")
        helper.log_error("No portfolios to proceed. Stopping...")
        raise
    except ServerError as e:
        helper.log_error("Sever error occurred while calling the API")
        helper.log_error("No portfolios to proceed. Stopping...")
        raise
    except Exception as e:
        helper.log_error("Error in finding portfolios")
        raise

    for invalid_id in portfolio.invalid_ids:
        helper.log_error("The Portfolio ID {} invalid. "
                         "Please validate that your portfolio ID is entered correctly".format(invalid_id))

    return portfolio
