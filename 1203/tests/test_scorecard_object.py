from collections import OrderedDict
import json

import pytest
import requests_mock

from app.scorecard import ScoreCard, format_date_string
from app.scorecard_exceptions import NoDataError
from tests.mock_data import (OVERALL_SCORE_DATA, OVERALL_SCORE_NO_DATA, OVERALL_SCORE_SINGLE_DAY_DATA, JWT_TOKEN,
                             FACTORS_METADATA, FACTORS_DATA, FACTORS_NO_DATA, ISSUE_TYPES_META_DATA, ISSUE_DATA,
                             ISSUE_NO_DATA)


class TestScorecardObject(object):
    def test_object_creation(self):
        scorecard = ScoreCard(access_key=JWT_TOKEN)

        assert scorecard._ScoreCard__access_key == JWT_TOKEN

    def test_without_access_key(self):
        with pytest.raises(TypeError):
            ScoreCard()


@requests_mock.Mocker()
class TestScorecardObjectWithMock(object):
    base_url = 'https://api.securityscorecard.io'
    company = 'example.com'
    access_key = 'test-key'

    def test_get_overall_score(self, mock):
        overall_score_url = '{}/companies/{}/history/score'.format(self.base_url, self.company)

        scorecard = ScoreCard(access_key=self.access_key)

        # Test success data
        mock.get(overall_score_url, text=json.dumps(OVERALL_SCORE_DATA))
        overall_score = scorecard.get_overall_score(self.company)[0]
        assert isinstance(overall_score, OrderedDict)
        # assert overall_score['cat'] == 'OverAll'
        # assert overall_score['eventType'] == "'scoreChange'"
        # assert overall_score['eventSource'] == 'OverallScore'
        # assert overall_score['domain'] == self.company
        # assert overall_score['dateYesterday'] == format_date_string(OVERALL_SCORE_DATA['entries'][-2]['date'])
        # assert overall_score['dateToday'] == format_date_string(OVERALL_SCORE_DATA['entries'][-1]['date'])
        # assert overall_score['scoreYesterday'] == OVERALL_SCORE_DATA['entries'][-2]['score']
        # assert overall_score['scoreToday'] == OVERALL_SCORE_DATA['entries'][-1]['score']
        # assert overall_score['scoreChange'] == (OVERALL_SCORE_DATA['entries'][-1]['score'] -
        #                                         OVERALL_SCORE_DATA['entries'][-2]['score'])
        # assert overall_score['diff'] == (OVERALL_SCORE_DATA['entries'][-1]['score'] -
        #                                  OVERALL_SCORE_DATA['entries'][-2]['score'])

        # Test with no entries
        mock.get(overall_score_url, text=json.dumps(OVERALL_SCORE_NO_DATA))
        with pytest.raises(NoDataError):
            scorecard.get_overall_score(self.company)

        # Test with data for single data
        # mock.get(overall_score_url, text=json.dumps(OVERALL_SCORE_SINGLE_DAY_DATA))
        # with pytest.raises(KeyError):
        #     scorecard.get_overall_score(self.company)

    def test_get_factors(self, mock):
        factors_url = '{}/companies/{}/history/factors/score'.format(self.base_url, self.company)
        factors_meta_url = '{}/metadata/factors'.format(self.base_url)

        scorecard = ScoreCard(access_key=self.access_key)
        mock.get(factors_meta_url, text=json.dumps(FACTORS_METADATA))

        # Test success data
        mock.get(factors_url, text=json.dumps(FACTORS_DATA))
        factors = scorecard.get_factors(self.company)

        assert isinstance(factors, list)
        assert isinstance(factors[0], OrderedDict)
        #assert len(factors) == len(FACTORS_METADATA['entries'])

        for factor in factors:
            assert factor['cat'] == 'Factor'
            assert factor['eventType'] == "'scoreChange'"
            assert factor['domain'] == self.company
            # :TODO: Assert remaining keys and values

        # Test with no entries
        mock.get(factors_url, text=json.dumps(FACTORS_NO_DATA))
        with pytest.raises(NoDataError):
            scorecard.get_factors(self.company)

    def test_get_issue_levels(self, mock):
        issues_url = '{}/companies/{}/history/events'.format(self.base_url, self.company)
        issues_meta_url = '{}/metadata/issue-types'.format(self.base_url)

        scorecard = ScoreCard(access_key=self.access_key)
        mock.get(issues_meta_url, text=json.dumps(ISSUE_TYPES_META_DATA))

        # Test success data
        mock.get(issues_url, text=json.dumps(ISSUE_DATA))
        issues = scorecard.get_issue_levels(self.company)

        assert isinstance(issues, tuple)
        #assert isinstance(issues[0], OrderedDict)
        #assert len(issues) == len(ISSUE_DATA['entries'])

        # for issue in issues:
        #     print issue[0]
        #     assert issue[0]['cat'] == 'Issue'
        #     assert issue[0]['domain'] == self.company
        #     # :TODO: Assert remaining keys and values
        #
        # # Test with no entries
        # mock.get(issues_url, text=json.dumps(ISSUE_NO_DATA))
        # with pytest.raises(NoDataError):
        #     scorecard.get_issue_levels(self.company)
