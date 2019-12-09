__author__ = 'Sacumen(www.sacumen.com)'

from app import app
from flask import render_template, request
from qpylib import qpylib

from aes_crypt import AESCipher
from data_store import read_data_store

#import poll_n_write


# -------------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    # Render home.html

    current_config = read_data_store()
    import pdb;pdb.set_trace()
    # Decrypt access key if available
    if current_config.get('access_key'):
        cipher = AESCipher()
        current_config['access_key'] = cipher.decrypt(current_config.get('access_key'))

    # Handle joining portfolio id
    if current_config.get('portfolio_ids') and current_config.get('portfolio_ids') != 'all' and \
            type(current_config.get('portfolio_ids')) == list:
        current_config['portfolio_ids'] = ','.join(current_config.get('portfolio_ids'))

    # Set config values if not available in current config
    if not current_config.get('monitor_config'):
        current_config['monitor_config'] = {}
    if not current_config.get('diff_override_config'):
        current_config['diff_override_config'] = {}

    if not current_config.get('proxy_dict'):
        current_config['proxy_dict'] = {}

    # Mask access_key
    if current_config.get('access_key'):
        current_config['access_key'] = current_config['access_key'][:6] + '**********'

    if request.method == 'POST':
        return render_template('home.html', required_or_not='false', **current_config)
    else:
        return render_template('home.html', required_or_not='true', **current_config)


# -------------------------------------------------------------------------------
@app.route('/result', methods=['POST'])
def result():
    import poll_n_write
    # Get the form
    form = request.form

    # Extract the form data
    ACCESS_KEY = form.get('access_key')
    DOMAIN = form.get('domain', '')
    URL = form.get('url')
    LEVEL_OVERALL_CHANGE = form.get('level_overall_change', '1')
    LEVEL_FACTOR_CHANGE = form.get('level_factor_change', '1')
    LEVEL_NEW_ISSUE_CHANGE = form.get('level_new_issue_change', '1')

    # If masked access key is present, unmask it using data store
    if ACCESS_KEY.endswith('**********'):
        current_config = read_data_store()
        ACCESS_KEY = current_config['access_key']

    # Split portfolio ids if present
    if form.get('portfolio_ids', '').strip().strip(',').lower() == 'all':
        PORTFOLIO_IDS = 'all'
    elif not form.get('portfolio_ids'):
        PORTFOLIO_IDS = None
    else:
        PORTFOLIO_IDS = form.get('portfolio_ids', '').strip().strip(',')
        PORTFOLIO_IDS = PORTFOLIO_IDS.split(',') if PORTFOLIO_IDS else None

    FETCH_HISTORICAL_DATA = bool(form.get('fetch_historical_data', False))

    MONITOR_CONFIG = {
        'fetch_company_overall': form.get('fetch_company_overall', 'no').lower() == 'yes',
        'fetch_company_factors': form.get('fetch_company_factors', 'no').lower() == 'yes',
        'fetch_company_issues': form.get('fetch_company_issues', 'no').lower() == 'yes',
        'fetch_portfolio_overall': form.get('fetch_portfolio_overall', 'no').lower() == 'yes',
        'fetch_portfolio_factors': form.get('fetch_portfolio_factors', 'no').lower() == 'yes',
        'fetch_portfolio_issues': form.get('fetch_portfolio_issues', 'no').lower() == 'yes',
        'issue_level_findings': form.get('issue_level_findings', 'no').lower() == 'yes',
        'proxy': form.get('proxy'),
        'level': form.get('level', 'info').upper(),
        'logLevel': form.get('level'),
        'proxy_type': form.get('proxy_type', 'no'),
        'host': form.get('host', 'no'),
        'port': form.get('port', 'no'),
        'username': form.get('username', 'no'),
        'password': form.get('password', 'no'),
    }
    if MONITOR_CONFIG['proxy'] != 'on':
        MONITOR_CONFIG['proxy'] = False

    DIFF_OVERRIDE_CONFIG = {
        'diff_override_own_overall': form.get('diff_override_own_overall', 'no').lower() == 'yes',
        'diff_override_portfolio_overall': form.get('diff_override_portfolio_overall', 'no').lower() == 'yes',
        'diff_override_own_factor': form.get('diff_override_own_factor', 'no').lower() == 'yes',
        'diff_override_portfolio_factor': form.get('diff_override_portfolio_factor', 'no').lower() == 'yes',
    }

    if MONITOR_CONFIG['proxy']:
        proxy_dict = {
            'proxy_type': MONITOR_CONFIG['proxy_type'],
            'host': MONITOR_CONFIG['host'],
            'port': MONITOR_CONFIG['port'],
            'username': MONITOR_CONFIG['username'],
            'password': MONITOR_CONFIG['password'],
        }
    else:
        proxy_dict = {}
        MONITOR_CONFIG['proxy_type'] = ''
        MONITOR_CONFIG['host'] = ''
        MONITOR_CONFIG['port'] = ''
        MONITOR_CONFIG['username'] = ''
        MONITOR_CONFIG['password'] = ''

    try:
        log_level = MONITOR_CONFIG.get('level', 'INFO')
        qpylib.set_log_level(log_level)
    except Exception as err:
        qpylib.log("Error " + str(err))
        raise

    # Connect to the SecurityScorecard; Start polling and write to the LEEF logger
    res, msg = poll_n_write.poll_scorecard_n_write(ACCESS_KEY,
                                                   DOMAIN,
                                                   URL,
                                                   LEVEL_OVERALL_CHANGE,
                                                   LEVEL_FACTOR_CHANGE,
                                                   LEVEL_NEW_ISSUE_CHANGE,
                                                   PORTFOLIO_IDS,
                                                   FETCH_HISTORICAL_DATA,
                                                   MONITOR_CONFIG,
                                                   DIFF_OVERRIDE_CONFIG,
                                                   proxy_dict)

    # If polling starts successfully, render dloading.html; Otherwise render error_with_back.html
    if res == True:
        return render_template('dloading.html', qname="success")
    else:
        qpylib.log(msg, level='error')
        return render_template('error_with_back.html', err=msg)

@app.route('/demo')
def demo():
    return "Hello", 200