__author__ = 'Sacumen(www.sacumen.com)'

from data_store import read_data_store, update_data_store
from utils import validate_api_credentials
from aes_crypt import AESCipher

from qpylib import qpylib
import logging

import threading
import datetime
import config as CONFIG
from thread_utils import terminate_thread
from scorecard import Company
from writers import CompanyWriter
from splunk_utils import build_portfolio
from helper import Helper

stop_polling_requested = False

# import pdb
# pdb.set_trace()
# logger for LEEF data
console_address = qpylib.get_console_address()

leef_logger = logging.getLogger('LEEF')
leef_formatter = logging.Formatter("%(asctime)s SECURITYSCORECARD %(message)s", "%b %d %H:%M:%S")
leef_logger.setLevel(logging.DEBUG)

syslog_handler = logging.handlers.SysLogHandler(
    address=(console_address, 514),
    facility=logging.handlers.SysLogHandler.LOG_LOCAL1,
)
syslog_handler.setFormatter(leef_formatter)
leef_logger.addHandler(syslog_handler)


class QRadarThread(threading.Thread):
    def __init__(self, name, access_key, domain, url, level_overall_change, level_factor_change,
                 level_new_issue_change, portfolio_ids, fetch_historical_data, user_config):
        threading.Thread.__init__(self, name=name)
        self.event = threading.Event()
        self.access_key = access_key
        self.domain = domain
        self.url = url
        self.level_overall_change = level_overall_change
        self.level_factor_change = level_factor_change
        self.level_new_issue_change = level_new_issue_change
        self.portfolio_ids = portfolio_ids
        self.fetch_historical_data = fetch_historical_data
        self.config = user_config

    def run(self):

        firstTime = True
        counter = 0
        while not self.event.is_set():
            counter = counter + 1

            if firstTime:
                self.threadTask()

            self.event.wait(3)
        syslog_handler.close()

    def threadTask(self):
        qpylib.log('Calling process_events first time for actual work', level='info')

        process_events(self.config, self.access_key, self.domain)

        qpylib.log('Finished write_leefs first time for actual work', level='info')
        next_run = datetime.datetime.now() + datetime.timedelta(seconds=CONFIG.LEEF_FETCH_INTERVAL)

        while True:

            if next_run < datetime.datetime.now():
                qpylib.log('Next run of write_leefs ', level='info')
                process_events(self.config, self.access_key, self.domain)
                qpylib.log('Finished write_leefs subsequent time for actual work', level='info')
                next_run = datetime.datetime.now() + datetime.timedelta(seconds=CONFIG.LEEF_FETCH_INTERVAL)
            # qpylib.log("Putting thread to sleep", level='info')
            # time.sleep(CONFIG.LEEF_FETCH_INTERVAL)



# put logic after this to kill thread with the same name
# get reference to thread and kill using thread.event.set()
def stopThread():
    # qpylib.log('Stop Thread Call made', level='info')

    for threadObj in threading.enumerate():
        threadName = threadObj.name
        qpylib.log('Thread Name %s' %threadName, level='info')
        if threadName == "securityscorecardthread":
            threadObj.event.set()
            terminate_thread(threadObj)

    is_alive = True
    while is_alive:
        qradar_found = False
        for threadObj in threading.enumerate():
            threadName = threadObj.name

            qpylib.log('Thread Name %s' %threadName, level='info')
            if threadName == "securityscorecardthread":
                qradar_found = True

        if not qradar_found:
            is_alive = False


def process_events(config, access_key, domain):
    helper = Helper()

    qpylib.log("Creating Company object.", level='info')
    company = Company(access_key=access_key, domain=domain)
    company_writer = CompanyWriter(company, helper, leef_logger)
    to_date = datetime.datetime.now().date()
    check_point_date = helper.get_check_point(CONFIG.CHECKPOINT_NAME)
    from_date = check_point_date if check_point_date else str(to_date - datetime.timedelta(days=CONFIG.DAYS))
    config.update({'to_date': to_date, 'from_date': from_date})
    helper.log_info('Started logging records, from {} to {}'.format(from_date, to_date))

    # Fetch overall for company
    if config['fetch_company_overall']:
        company_writer.write_overall(**config)
        helper.log_info('Company overall logged.')
        # helper.log_debug('Company overall logged.')

    # Fetch factors for company
    if config['fetch_company_factors']:
        company_writer.write_factors(**config)
        helper.log_info('Company factors logged.')

    # Fetch issues and issue level details for company
    if config['fetch_company_issues']:
        company_writer.write_issues(**config)
        helper.log_info('Company issues logged.')

    helper.log_info("Start processing portfolio companies.")
    try:
        helper.log_info("Portfolio ids are:------{}".format(config['portfolio_ids']))

        if config['portfolio_ids']:
            ids = None if config['portfolio_ids'] == 'all' else config['portfolio_ids']
            portfolio = build_portfolio(helper, access_key, ids, **config)
            helper.log_info("Total portfolio companies = {}.".format(len(portfolio.companies)))

            for company in portfolio.companies:
                company_writer = CompanyWriter(company, helper, leef_logger)
                helper.log_info("Processing portfolio company {} ".format(company.domain))
                config.update({
                    'portfolioId': company.portfolio_id,
                    'portfolioName': "'" + company.portfolio_name + "'",
                })

                # Fetch overall score for company
                if config['fetch_portfolio_overall']:
                    company_writer.write_overall(**config)
                    helper.log_info('Logged portfolio company {} overall'.format(company.domain))

                # Fetch factors for company
                if config['fetch_portfolio_factors']:
                    company_writer.write_factors(**config)
                    helper.log_info('Logged portfolio company {} factor'.format(company.domain))

                # Fetch issues and issue level details for company
                if config['fetch_portfolio_issues']:
                    company_writer.write_issues(**config)
                    helper.log_info('Logged portfolio company {} issue'.format(company.domain))
        else:
            helper.log_info("No portfolios found.")
    except Exception as err:
        helper.log_error("Getting error as {}".format(err))

    helper.log_info("Writing completed to leefs.")


# -------------------------------------------------------------------------------
#
# Start polling the SecurityScorecard
# Write the received messages to LEEF logger
def poll_scorecard_n_write(
        ACCESS_KEY=None,
        DOMAIN=None,
        URL=None,
        LEVEL_OVERALL_CHANGE=None,
        LEVEL_FACTOR_CHANGE=None,
        LEVEL_NEW_ISSUE_CHANGE=None,
        PORTFOLIO_IDS=None,
        FETCH_HISTORICAL_DATA=False,
        MONITOR_CONFIG=None,
        DIFF_OVERRIDE_CONFIG=None,
        proxy=None,
):

    config = read_data_store()
    cipher = AESCipher()

    # Validate access token and URL
    if not validate_api_credentials(ACCESS_KEY, URL):
        qpylib.log('Invalid credentials', level='info')
        return False, "Invalid API token. Please check."

    ACCESS_KEY = cipher.encrypt(ACCESS_KEY)
    update_data_store({
        'access_key': ACCESS_KEY,
        'domain': DOMAIN,
        'url': URL,
        'level_overall_change': LEVEL_OVERALL_CHANGE,
        'level_factor_change': LEVEL_FACTOR_CHANGE,
        'level_new_issue_change': LEVEL_NEW_ISSUE_CHANGE,
        'portfolio_ids': PORTFOLIO_IDS,
        'fetch_historical_data': FETCH_HISTORICAL_DATA,
        'monitor_config': MONITOR_CONFIG,
        'diff_override_config': DIFF_OVERRIDE_CONFIG,
        'proxy': proxy,
    })

    qpylib.log('Done with read and write from conf file', level='info')

    stopThread()

    qpylib.log('Done with stopThread', level='info')

    user_config = {
        'level_overall_change': LEVEL_OVERALL_CHANGE or config.get('level_overall_change', ''),
        'level_factor_change': LEVEL_FACTOR_CHANGE or config.get('level_factor_change', ''),
        'level_new_issue_change': LEVEL_NEW_ISSUE_CHANGE or config.get('level_new_issue_change', ''),
        'portfolio_ids': PORTFOLIO_IDS or config.get('portfolio_ids'),
    }
    if MONITOR_CONFIG:
        user_config.update(MONITOR_CONFIG)
    else:
        user_config.update(config.get('monitor_config', {}))
    if DIFF_OVERRIDE_CONFIG:
        user_config.update(DIFF_OVERRIDE_CONFIG)
    else:
        user_config.update(DIFF_OVERRIDE_CONFIG or config.get('diff_override_config', {}))

    user_config['proxy'] = proxy

    access_key = ACCESS_KEY or config.get('access_key', '')
    thread = QRadarThread(
        "securityscorecardthread",
        access_key=cipher.decrypt(access_key) if access_key else access_key,
        domain=DOMAIN,
        url=URL or config.get('url', ''),
        level_overall_change=LEVEL_OVERALL_CHANGE or config.get('level_overall_change', ''),
        level_factor_change=LEVEL_FACTOR_CHANGE or config.get('level_factor_change', ''),
        level_new_issue_change=LEVEL_NEW_ISSUE_CHANGE or config.get('level_new_issue_change', ''),
        portfolio_ids=PORTFOLIO_IDS or config.get('portfolio_ids'),
        fetch_historical_data=FETCH_HISTORICAL_DATA or config.get('fetch_historical_data', False),
        user_config=user_config,
    )
    qpylib.log('Starting thread', level='info')
    thread.start()
    qpylib.log('Started thread', level='info')
    return True, "Success"

