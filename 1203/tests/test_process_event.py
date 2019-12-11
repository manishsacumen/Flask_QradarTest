import pytest
import requests_mock

from mockers import Company, CompanyWriter, Helper, EventWriter, build_portfolio
from app.qpylib import qpylib
from mock import MagicMock
from mock_data import MONITOR_CONFIG, FACTORS_DATA, OVERALL_SCORE_DATA, ISSUE_DATA, HISTORY_EVENT
import json

@requests_mock.Mocker()
class Test_event(object):
    domain = "www.example.com"
    factor_url =  "https://api.securityscorecard.io/metadata/factors"
    score ="https://api.securityscorecard.io/companies/www.example.com/history/score"
    factor_score = "https://api.securityscorecard.io/companies/www.example.com/history/factors/score"
    issues_url = "https://api.securityscorecard.io/metadata/issue-types"
    history_event = "https://api.securityscorecard.io/companies/www.example.com/history/events"
    config = None
    access_key = 'test-key'
    
    def url_mocking(self,mock):

        mock.get(self.factor_url, text=json.dumps(FACTORS_DATA))
        mock.get(self.score, text=json.dumps(OVERALL_SCORE_DATA))
        mock.get(self.factor_score, text=json.dumps(OVERALL_SCORE_DATA))
        mock.get(self.issues_url, text=json.dumps(OVERALL_SCORE_DATA))
        mock.get(self.history_event, text=json.dumps(HISTORY_EVENT))
        qpylib.get_console_address = MagicMock(return_value = None)
        qpylib.log =  MagicMock(return_value = None)
       

    def test_event_with_data(self, mock):

        helper = Helper()
        ew = EventWriter()
        company = Company(self.access_key,self.domain)
        writer  =  CompanyWriter(company, helper)
        from app.poll_n_write import process_events
        self.url_mocking(mock)
        process = process_events(MONITOR_CONFIG, self.access_key, self.domain)
        assert process == None
        if MONITOR_CONFIG['fetch_company_overall']:
            overll_data = writer.write_overall(self.config)
            assert overll_data == "Company overall logged"
        if MONITOR_CONFIG['fetch_company_factors']:
            fact_data = writer.write_factors(self.config)
            assert fact_data  ==   "Company factors logged"
        if MONITOR_CONFIG['fetch_company_issues']:
            issue_data = writer.write_issues(self.config)
            assert issue_data  == "Company issues logged"
        if MONITOR_CONFIG['portfolio_ids']:
            ids = None if MONITOR_CONFIG['portfolio_ids'] == 'all' else MONITOR_CONFIG['portfolio_ids']
            portfolio = build_portfolio(helper, self.access_key, ids,config=None)
            for company in portfolio:
                company_writer = CompanyWriter(company, helper)
                MONITOR_CONFIG.update({
                    'portfolioId': company['portfolio_id'],
                    'portfolioName': "'" + company['portfolio_name'] + "'",
                })
                # Fetch overall score for company
                if MONITOR_CONFIG['fetch_portfolio_overall']:
                    c_overall = company_writer.write_overall(self.config)
                    assert c_overall == "Company overall logged"
                # Fetch factors for company
                if MONITOR_CONFIG['fetch_portfolio_factors']:
                    c_factors = company_writer.write_factors(self.config)
                    assert c_factors == "Company factors logged"
                # Fetch issues and issue level details for company
                if MONITOR_CONFIG['fetch_portfolio_issues']:
                    c_issues = company_writer.write_issues(self.config)
                    assert c_issues == "Company issues logged"
    
    def test_event_without(self, mock):  
        MONITOR_CONFIG = {}
        self.url_mocking(mock)
        from app.poll_n_write import process_events
        with pytest.raises(KeyError):
            process_events(MONITOR_CONFIG, self.access_key, self.domain)
    