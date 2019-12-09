from collections import OrderedDict

from tests.mockers import Company, Helper, EventWriter
from writers import CompanyWriter


class TestCompanyWriter(object):
    domain = 'example.com'

    def test_write_overall(self):
        data = [OrderedDict([
            ('cat', 'OverAll'),
            ('type', "'scoreChange'"),
            ('src', 'OverallScore'),
            ('subject', self.domain),
            ('scoreYesterday', '100'),
            ('scoreToday', '99'),
            ('scoreChange', '-1'),
            ('diff', '-1'),
        ]),OrderedDict([
            ('cat', 'OverAll'),
            ('type', "'scoreChange'"),
            ('src', 'OverallScore'),
            ('subject', self.domain),
            ('scoreYesterday', '95'),
            ('scoreToday', '96'),
            ('scoreChange', '1'),
            ('diff', '1'),
        ])]
        config = {
            'diff_override_own_overall': True,
            'level_overall_change': '10',
        }
        helper = Helper()
        ew = EventWriter()

        company = Company(self.domain, overall_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_overall(**config)

        assert len(ew.events) == 2
        event_data = ew.events[0]['data']
        assert 'cat=OverAll' in event_data
        assert "type='scoreChange'" in event_data
        assert 'src=OverallScore' in event_data
        assert 'subject={}'.format(self.domain) in event_data
        assert 'scoreYesterday=100' in event_data
        assert 'scoreToday=99' in event_data
        assert 'scoreChange=-1' in event_data
        assert 'severity=10' in event_data

        # Test with zero difference and no override
        ew.clear_events()
        data[0].update({'diff': 0})
        config.update({'diff_override_own_overall': False})

        company = Company(self.domain, overall_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_overall(**config)

        assert len(ew.events) == 1

        # Test with zero difference and override
        ew.clear_events()
        config.update({'diff_override_own_overall': True})

        company = Company(self.domain, overall_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_overall(**config)

        assert len(ew.events) == 2

    def test_write_factors(self):
        data = [
            OrderedDict([
                ('body', 'Factor'),
                ('type', "'scoreChange'"),
                ('src', 's1'),
                ('subject', self.domain),
                ('scoreYesterday', '99'),
                ('scoreToday', '98'),
                ('scoreChange', 1),
                ('diff', 1),
                ('factorDescription', "'desc1'")
            ]),
            OrderedDict([
                ('body', 'Factor'),
                ('type', "'scoreChange'"),
                ('src', 's2'),
                ('subject', self.domain),
                ('scoreYesterday', '89'),
                ('scoreToday', '88'),
                ('scoreChange', 11),
                ('diff', 11),
                ('factorDescription', "'desc2'")
            ]),
        ]
        config = {
            'diff_override_own_factor': True,
            'level_factor_change': '10',
        }
        helper = Helper()
        ew = EventWriter()

        company = Company(self.domain, factor_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_factors(**config)

        event_data_1 = ew.events[0]['data']
        assert 'body=Factor' in event_data_1
        assert "type='scoreChange'" in event_data_1
        assert 'src=s1' in event_data_1
        assert 'subject={}'.format(self.domain) in event_data_1
        assert 'scoreYesterday=99' in event_data_1
        assert 'scoreToday=98' in event_data_1
        assert 'scoreChange=1' in event_data_1
        assert 'severity=10' in event_data_1

        # event_data_2 = ew.events[1]['data']
        # assert 'body=Factor' in event_data_2
        # assert "type='scoreChange'" in event_data_2
        # assert 'src=s2' in event_data_2
        # assert 'domain={}'.format(self.domain) in event_data_2
        # assert 'scoreYesterday=89' in event_data_2
        # assert 'scoreToday=88' in event_data_2
        # assert 'scoreChange=11' in event_data_2
        # assert 'severity=10' in event_data_2

        # Test with zero difference and no override
        ew.clear_events()
        data[0].update({'diff': 0})
        config.update({'diff_override_own_factor': False})

        company = Company(self.domain, factor_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_factors(**config)

        assert len(ew.events) == 1

        # Test with zero difference and override
        ew.clear_events()
        config.update({'diff_override_own_factor': True})

        company = Company(self.domain, factor_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_factors(**config)

        assert len(ew.events) == 2

    def test_write_issues(self):
        data = ([
            OrderedDict([
                ('body', 'Issue'),
                ('type', "'type1'"),
                ('src', 'es1'),
                ('eventID', 'e1'),
                ('subject', self.domain),
            ])],[]
        )
        config = {
            'level_new_issue_change': 5,
            'fetch_issue_level_data': False
        }
        helper = Helper()
        ew = EventWriter()

        company = Company(self.domain, issue_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_issues(**config)

        assert len(ew.events) == 1

        event_data = ew.events[0]['data']
        assert 'body=Issue' in event_data
        assert "type='type1'" in event_data
        assert 'subject=example.com' in event_data
        assert 'src=es1' in event_data
        assert 'eventID=e1' in event_data
        assert 'severity=5' in event_data

    def test_write_issues_with_issue_level(self):
        data = ([
            OrderedDict([
                ('body', 'Issue'),
                ('type', "'type1'"),
                ('src', 'es1'),
                ('eventID', 'e1'),
                ('subject', self.domain),
            ]),
        ],[{'count': 5, 'eventId': 383887, 'issuer_organization_name': 'COMODO CA Limited',
            'ssc_domain': 'sacumen.com', 'first_seen_time': '2019-08-09T01:24:49.268Z',
            'last_seen_time': '2019-09-08T23:52:09.401Z', 'subject_common_name': 'ssl946379.cloudflaressl.com',
            'parent_domain': 'sacumen.com', 'not_valid_after': '2020-02-26T23:59:59.000Z',
            'issueType': 'tls_ocsp_stapling', 'group_status': 'active',
            'issue_id': '36c7697d-cafd-5b79-b3e2-0a11254d6054', 'not_valid_before': '2019-08-20T00:00:00.000Z',
            'factor': 'network_security', 'effective_date': '2019-09-08T00:00:00.000Z',
            'connection_attributes': {'dst_ip': '104.19.246.1', 'dst_port': 443}},
           {'count': 5, 'eventId': 383887, 'issuer_organization_name': 'COMODO CA Limited',
            'ssc_domain': 'sacumen.com', 'first_seen_time': '2019-08-09T01:24:49.268Z',
            'last_seen_time': '2019-09-08T23:52:09.401Z', 'subject_common_name': 'ssl946379.cloudflaressl.com',
            'parent_domain': 'sacumen.com', 'not_valid_after': '2020-02-26T23:59:59.000Z',
            'issueType': 'tls_ocsp_stapling', 'group_status': 'active',
            'issue_id': '36c7697d-cafd-5b79-b3e2-0a11254d6054', 'not_valid_before': '2019-08-20T00:00:00.000Z',
            'factor': 'network_security', 'effective_date': '2019-09-08T00:00:00.000Z',
            'connection_attributes': {'dst_ip': '104.19.246.1', 'dst_port': 443}}
           ])
        config = {
            'level_new_issue_change': 5,
            'fetch_issue_level_data': True
        }
        helper = Helper()
        ew = EventWriter()

        company = Company(self.domain, issue_data=data)
        writer = CompanyWriter(company, helper, ew)

        writer.write_issues(**config)

        assert len(ew.events) == 3

        event_data = ew.events[0]['data']
        import json
        issue_level_data = ew.events[1]['data']
        assert type(issue_level_data) == str
        assert 'ssc_domain' in json.dumps(issue_level_data)
        assert 'body=Issue' in event_data
        assert "type='type1'" in event_data
        assert 'subject=example.com' in event_data
        assert 'src=es1' in event_data
        assert 'eventID=e1' in event_data
        assert 'severity=5' in event_data
