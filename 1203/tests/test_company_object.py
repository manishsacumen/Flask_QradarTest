from collections import OrderedDict
import json

import pytest
import requests_mock

from scorecard import Company
from scorecard_exceptions import NoDataError
from tests.mock_data import (OVERALL_SCORE_DATA, OVERALL_SCORE_NO_DATA, OVERALL_SCORE_SINGLE_DAY_DATA, JWT_TOKEN,
                             FACTORS_METADATA, FACTORS_DATA, FACTORS_NO_DATA, ISSUE_TYPES_META_DATA, ISSUE_DATA,
                             ISSUE_NO_DATA)


class TestCompanyObject(object):
    def test_without_access_key(self):
        with pytest.raises(TypeError):
            Company(domain='example.com')

    def test_without_domain(self):
        with pytest.raises(TypeError):
            Company(access_key='test-key')


@requests_mock.Mocker()
class TestCompanyObjectWithMock(object):
    base_url = 'https://api.securityscorecard.io'
    domain = 'example.com'
    access_key = 'test-key'

    def test_get_overall_score(self, mock):
        overall_score_url = '{}/companies/{}/history/score'.format(self.base_url, self.domain)

        company = Company(access_key=self.access_key, domain=self.domain)

        # Test success data
        mock.get(overall_score_url, text=json.dumps(OVERALL_SCORE_DATA))
        overall_score = company.get_overall_score()
        assert isinstance(overall_score, OrderedDict)
        assert overall_score['cat'] == 'OverAll'
        assert overall_score['eventType'] == "'scoreChange'"
        assert overall_score['eventSource'] == 'OverallScore'
        assert overall_score['domain'] == self.domain

        # Test with no entries
        mock.get(overall_score_url, text=json.dumps(OVERALL_SCORE_NO_DATA))
        with pytest.raises(NoDataError):
            company.get_overall_score()

    def test_get_factors(self, mock):
        factors_url = '{}/companies/{}/history/factors/score'.format(self.base_url, self.domain)
        factors_meta_url = '{}/metadata/factors'.format(self.base_url)

        company = Company(access_key=self.access_key, domain=self.domain)
        mock.get(factors_meta_url, text=json.dumps(FACTORS_METADATA))

        # Test success data
        mock.get(factors_url, text=json.dumps(FACTORS_DATA))
        factors = company.get_factors()

        assert isinstance(factors, list)
        assert isinstance(factors[0], OrderedDict)
        assert len(factors) == len(FACTORS_METADATA['entries'])

        for factor in factors:
            assert factor['cat'] == 'Factor'
            assert factor['eventType'] == "'scoreChange'"
            assert factor['domain'] == self.domain
            # :TODO: Assert remaining keys and values

        # Test with no entries
        mock.get(factors_url, text=json.dumps(FACTORS_NO_DATA))
        with pytest.raises(NoDataError):
            company.get_factors()

    def test_get_issue_levels(self, mock):
        issues_url = '{}/companies/{}/history/events'.format(self.base_url, self.domain)
        issues_meta_url = '{}/metadata/issue-types'.format(self.base_url)

        company = Company(access_key=self.access_key, domain=self.domain)
        mock.get(issues_meta_url, text=json.dumps(ISSUE_TYPES_META_DATA))

        # Test success data
        mock.get(issues_url, text=json.dumps(ISSUE_DATA))
        issues = company.get_issue_levels()

        assert isinstance(issues, list)
        assert isinstance(issues[0], OrderedDict)
        assert len(issues) == len(ISSUE_DATA['entries'])

        for issue in issues:
            assert issue['cat'] == 'Issue'
            assert issue['domain'] == self.domain
            # :TODO: Assert remaining keys and values

        # Test with no entries
        mock.get(issues_url, text=json.dumps(ISSUE_NO_DATA))
        with pytest.raises(NoDataError):
            company.get_issue_levels()
