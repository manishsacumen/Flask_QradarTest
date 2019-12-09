import json

import pytest
import requests_mock

from scorecard import Portfolio
from tests.mock_data import (PORTFOLIO_ID_1, PORTFOLIO_ID_2, PORTFOLIO_LIST_DATA, PORTFOLIO_1_COMANIES,
                             PORTFOLIO_2_COMANIES, PORTFOLIO_ID_INVALID)


@requests_mock.Mocker()
class TestPortfolioObject(object):
    portfolios_url = 'https://api.securityscorecard.io/portfolios'
    access_key = 'test-key'

    def setup_mocking(self, mock):
        mock.get(self.portfolios_url, text=json.dumps(PORTFOLIO_LIST_DATA))
        mock.get(
            '{}/{}/companies'.format(self.portfolios_url, PORTFOLIO_ID_1),
            text=json.dumps(PORTFOLIO_1_COMANIES),
        )
        mock.get(
            '{}/{}/companies'.format(self.portfolios_url, PORTFOLIO_ID_2),
            text=json.dumps(PORTFOLIO_2_COMANIES),
        )

    def test_without_ids(self, mock):
        self.setup_mocking(mock)

        portfolio = Portfolio(access_key=self.access_key)

        assert len(portfolio.companies) == (len(PORTFOLIO_1_COMANIES['entries']) + len(PORTFOLIO_2_COMANIES['entries']))
        assert len(portfolio.valid_ids) == 2
        assert not portfolio.invalid_ids

    def test_with_ids(self, mock):
        self.setup_mocking(mock)

        ids = [PORTFOLIO_ID_1, PORTFOLIO_ID_2, PORTFOLIO_ID_INVALID]

        portfolio = Portfolio(access_key=self.access_key, ids=ids)

        assert len(portfolio.companies) == (len(PORTFOLIO_1_COMANIES['entries']) + len(PORTFOLIO_2_COMANIES['entries']))
        assert len(portfolio.valid_ids) == 2
        assert len(portfolio.invalid_ids) == 1
        assert PORTFOLIO_ID_INVALID in portfolio.invalid_ids
