JWT_TOKEN = 'jwt.token.valid'
name = 'abc'
access_key = 'xyz'
domain= 'abc.com'
url = 'https://abcd.com'
level_overall_change = 77
level_factor_change = 65

level_new_issue_change = 76
portfolio_ids = 'all'
fetch_historical_data = 'no'
user_config = {"access_key": "xyz", "domain": "sacumen.com", "level_overall_change": "77",
                 "portfolio_ids": "all", "level_factor_change": "77", "last_run_date": "2019-11-29",
                 "url": "https://api.securityscorecard.io", "fetch_historical_data": 'false', "proxy": {},
                 "diff_override_config": {"diff_override_portfolio_overall": 'false',
                                          "diff_override_own_factor": 'false', "diff_override_own_overall": 'true',
                                          "diff_override_portfolio_factor": 'false'},
                 "monitor_config": {"username": "", "fetch_company_issues": 'false',
                                    "fetch_portfolio_factors": 'false', "level": "INFO", "logLevel": "info",
                                    "proxy_type": "http", "issue_level_findings": 'false',
                                    "fetch_portfolio_issues": 'false', "fetch_company_overall": 'true',
                                    "fetch_portfolio_overall": 'false', "host": "",
                                    "fetch_company_factors": 'false', "proxy": 'false', "password": "",
                                    "port": ""}, "level_new_issue_change": "77"}

OVERALL_SCORE_DATA = {
    "entries": [
        {
            "domain": "example.com",
            "score": 78,
            "date": "2018-09-02T00:00:00.000Z"
        },
        {
            "domain": "example.com",
            "score": 77,
            "date": "2018-09-03T00:00:00.000Z"
        },
        {
            "domain": "example.com",
            "score": 76,
            "date": "2018-09-04T00:00:00.000Z"
        },
        {
            "domain": "example.com",
            "score": 76,
            "date": "2018-09-05T00:00:00.000Z"
        },
    ],
}

OVERALL_SCORE_NO_DATA = {
    "entries": [],
}

OVERALL_SCORE_SINGLE_DAY_DATA = {
    "entries": [
        {
            "domain": "example.com",
            "score": 78,
            "date": "2018-09-02T00:00:00.000Z"
        },
    ],
}

FACTORS_METADATA = {
    "entries": [
        {
            "key": "network_security",
            "name": "Network Security",
            "description": "Detecting insecure network settings"
        },
        {
            "key": "dns_health",
            "name": "DNS Health",
            "description": "Detecting DNS insecure configurations and vulnerabilities"
        },
        {
            "key": "patching_cadence",
            "name": "Patching Cadence",
            "description": "Out of date company assets which may contain vulnerabilities or risks"
        },
        {
            "key": "endpoint_security",
            "name": "Endpoint Security",
            "description": "Measuring security level of employee workstations"
        },
        {
            "key": "ip_reputation",
            "name": "IP Reputation",
            "description": "Detecting suspicious activity, such as malware or spam, within your company network"
        },
        {
            "key": "application_security",
            "name": "Application Security",
            "description": "Detecting common website application vulnerabilities"
        },
        {
            "key": "cubit_score",
            "name": "Cubit Score",
            "description": "Proprietary algorithms checking for implementation of common security best practices"
        },
        {
            "key": "hacker_chatter",
            "name": "Hacker Chatter",
            "description": "Monitoring hacker sites for chatter about your company"
        },
        {
            "key": "leaked_information",
            "name": "Information Leak",
            "description": "Potentially confidential company information which may have been inadvertently leaked"
        },
        {
            "key": "social_engineering",
            "name": "Social Engineering",
            "description": "Measuring company awareness to a social engineering or phishing attack"
        },
    ],
}

FACTORS_DATA = {
    "entries": [
        {
            "domain": "example.com",
            "factors": [
                {
                    "name": "application_security",
                    "score": 59
                },
                {
                    "name": "cubit_score",
                    "score": 100
                },
                {
                    "name": "dns_health",
                    "score": 36
                },
                {
                    "name": "endpoint_security",
                    "score": 100
                },
                {
                    "name": "hacker_chatter",
                    "score": 100
                },
                {
                    "name": "ip_reputation",
                    "score": 100
                },
                {
                    "name": "leaked_information",
                    "score": 100
                },
                {
                    "name": "network_security",
                    "score": 83
                },
                {
                    "name": "patching_cadence",
                    "score": 85
                },
                {
                    "name": "social_engineering",
                    "score": 100
                }
            ],
            "date": "2018-09-02T00:00:00.000Z"
        },
        {
            "domain": "example.com",
            "factors": [
                {
                    "name": "application_security",
                    "score": 59
                },
                {
                    "name": "cubit_score",
                    "score": 100
                },
                {
                    "name": "dns_health",
                    "score": 36
                },
                {
                    "name": "endpoint_security",
                    "score": 100
                },
                {
                    "name": "hacker_chatter",
                    "score": 100
                },
                {
                    "name": "ip_reputation",
                    "score": 100
                },
                {
                    "name": "leaked_information",
                    "score": 100
                },
                {
                    "name": "network_security",
                    "score": 84
                },
                {
                    "name": "patching_cadence",
                    "score": 80
                },
                {
                    "name": "social_engineering",
                    "score": 100
                }
            ],
            "date": "2018-09-03T00:00:00.000Z"
        },
        {
            "domain": "example.com",
            "factors": [
                {
                    "name": "application_security",
                    "score": 53
                },
                {
                    "name": "cubit_score",
                    "score": 100
                },
                {
                    "name": "dns_health",
                    "score": 36
                },
                {
                    "name": "endpoint_security",
                    "score": 100
                },
                {
                    "name": "hacker_chatter",
                    "score": 100
                },
                {
                    "name": "ip_reputation",
                    "score": 100
                },
                {
                    "name": "leaked_information",
                    "score": 100
                },
                {
                    "name": "network_security",
                    "score": 84
                },
                {
                    "name": "patching_cadence",
                    "score": 80
                },
                {
                    "name": "social_engineering",
                    "score": 100
                }
            ],
            "date": "2018-09-04T00:00:00.000Z"
        },
    ]
}

FACTORS_NO_DATA = {
    "entries": [],
}

ISSUE_TYPES_META_DATA = {
    "entries": [
        {
            "key": "admin_subdomain",
            "severity": "low",
            "factor": "cubit_score",
            "title": "Exposed Subdomain"
        },
        {
            "key": "csp_no_policy",
            "severity": "info",
            "factor": "application_security",
            "title": "Content Security Policy (CSP) Missing"
        },
        {
            "key": "open_resolver",
            "severity": "high",
            "factor": "dns_health",
            "title": "Open DNS Resolver Detected"
        },
        {
            "key": "spf_record_malformed",
            "severity": "low",
            "factor": "dns_health",
            "title": "Malformed SPF Record"
        },
        {
            "key": "spf_record_softfail",
            "severity": "low",
            "factor": "dns_health",
            "title": "SPF Record Contains a Softfail"
        },
        {
            "key": "spf_record_wildcard",
            "severity": "low",
            "factor": "dns_health",
            "title": "SPF Record Contains Wildcard"
        },
        {
            "key": "ddos_protection",
            "severity": "positive",
            "factor": "network_security",
            "title": "DDoS Protection Service Detected"
        },
        {
            "key": "csp_unsafe_policy",
            "severity": "info",
            "factor": "application_security",
            "title": "Content Security Policy Contains 'unsafe-*' Directive"
        },
        {
            "key": "csp_too_broad",
            "severity": "info",
            "factor": "application_security",
            "title": "Content Security Policy Contains Broad Directives"
        },
        {
            "key": "unsafe_sri",
            "severity": "info",
            "factor": "application_security",
            "title": "Unsafe Implementation Of Subresource Integrity"
        },
        {
            "key": "object_storage_bucket_with_risky_acl",
            "severity": "info",
            "factor": "application_security",
            "title": "Object Storage Bucket with Risky ACL"
        },
        {
            "key": "hosted_on_object_storage",
            "severity": "info",
            "factor": "application_security",
            "title": "Website Hosted on Object Storage"
        },
        {
            "key": "references_object_storage",
            "severity": "info",
            "factor": "application_security",
            "title": "Website References Object Storage"
        },
        {
            "key": "waf_detected",
            "severity": "positive",
            "factor": "application_security",
            "title": "Web Application Firewall (WAF) Detected"
        },
        {
            "key": "dnssec_detected",
            "severity": "positive",
            "factor": "dns_health",
            "title": "Valid DNSSEC Configuration Detected"
        },
        {
            "key": "service_mongodb",
            "severity": "high",
            "factor": "network_security",
            "title": "MongoDB Service Observed"
        },
        {
            "key": "new_booter_shell",
            "severity": "medium",
            "factor": "hacker_chatter",
            "title": "Booter Shells Identified"
        },
        {
            "key": "new_defacement",
            "severity": "medium",
            "factor": "hacker_chatter",
            "title": "Defacement"
        },
        {
            "key": "non_malware_events_last_month",
            "severity": "medium",
            "factor": "ip_reputation",
            "title": "P2P Activities"
        },
        {
            "key": "spf_record_missing",
            "severity": "medium",
            "factor": "dns_health",
            "title": "SPF Record Missing"
        },
        {
            "key": "attack_feed",
            "severity": "medium",
            "factor": "ip_reputation",
            "title": "Attack Detected"
        },
        {
            "key": "tlscert_no_revocation",
            "severity": "low",
            "factor": "network_security",
            "title": "TLS Certificate Without Revocation Control"
        },
        {
            "key": "employee_satisfaction",
            "severity": "low",
            "factor": "social_engineering",
            "title": "Employee Satisfaction"
        },
        {
            "key": "github_information_leak_disclosure",
            "severity": "low",
            "factor": "leaked_information",
            "title": "Sensitive Application Information Exposed (GitHub)"
        },
        {
            "key": "google_information_leak_disclosure",
            "severity": "low",
            "factor": "leaked_information",
            "title": "Sensitive Application Information Exposed (Google)"
        },
        {
            "key": "leaked_passwords",
            "severity": "low",
            "factor": "leaked_information",
            "title": "Credentials at Risk"
        },
        {
            "key": "chatter",
            "severity": "info",
            "factor": "hacker_chatter",
            "title": "Hacker Chatter Mention"
        },
        {
            "key": "marketing_site",
            "severity": "low",
            "factor": "social_engineering",
            "title": "Corporate Email Used on Marketing Sites"
        },
        {
            "key": "short_term_lending_site",
            "severity": "low",
            "factor": "social_engineering",
            "title": "Corporate Email Used on Short-Term Lending Sites"
        },
        {
            "key": "social_network_issues",
            "severity": "info",
            "factor": "social_engineering",
            "title": "Leaked Company Emails Open to Spear-Phishing"
        },
        {
            "key": "tor_node_events_last_month",
            "severity": "info",
            "factor": "ip_reputation",
            "title": "Tor Exit Nodes"
        },
        {
            "key": "domain_uses_hsts_preloading",
            "severity": "positive",
            "factor": "application_security",
            "title": "Domain Uses HSTS Preloading"
        },
        {
            "key": "uce",
            "severity": "info",
            "factor": "ip_reputation",
            "title": "Unsolicited Commercial Email"
        },
        {
            "key": "typosquat",
            "severity": "info",
            "factor": "cubit_score",
            "title": "Possible Typosquat Domains Detected"
        },
        {
            "key": "outdated_os",
            "severity": "medium",
            "factor": "endpoint_security",
            "title": "Outdated Operating System Observed"
        },
        {
            "key": "domain_missing_https",
            "severity": "high",
            "factor": "application_security",
            "title": "Site does not enforce HTTPS"
        },
        {
            "key": "hsts_incorrect",
            "severity": "medium",
            "factor": "application_security",
            "title": "Website Does Not Implement HSTS Best Practices"
        },
        {
            "key": "insecure_https_redirect_pattern",
            "severity": "medium",
            "factor": "application_security",
            "title": "Insecure HTTPS Redirect Pattern"
        },
        {
            "key": "redirect_chain_contains_http",
            "severity": "medium",
            "factor": "application_security",
            "title": "Redirect Chain Contains HTTP"
        },
        {
            "key": "x_frame_options_incorrect",
            "severity": "medium",
            "factor": "application_security",
            "title": "Website does not implement X-Frame-Options Best Practices"
        },
        {
            "key": "x_xss_protection_incorrect",
            "severity": "medium",
            "factor": "application_security",
            "title": "Website does not implement X-XSS-Protection Best Practices"
        },
        {
            "key": "x_content_type_options_incorrect",
            "severity": "low",
            "factor": "application_security",
            "title": "Website does not implement X-Content-Type-Options Best Practices"
        },
        {
            "key": "exposed_ports",
            "severity": "info",
            "factor": "network_security",
            "title": "Open TCP Ports Observed"
        },
        {
            "key": "outdated_browser",
            "severity": "medium",
            "factor": "endpoint_security",
            "title": "Outdated Web Browser Observed"
        },
        {
            "key": "cookie_missing_http_only",
            "severity": "low",
            "factor": "application_security",
            "title": "Session Cookie Missing 'HttpOnly' Attribute"
        },
        {
            "key": "cookie_missing_secure_attribute",
            "severity": "low",
            "factor": "application_security",
            "title": "Cookie Missing 'Secure' Attribute"
        },
        {
            "key": "patching_cadence_high",
            "severity": "high",
            "factor": "patching_cadence",
            "title": "High Severity CVEs Patching Cadence"
        },
        {
            "key": "patching_cadence_medium",
            "severity": "medium",
            "factor": "patching_cadence",
            "title": "Medium Severity CVEs Patching Cadence"
        },
        {
            "key": "patching_cadence_low",
            "severity": "low",
            "factor": "patching_cadence",
            "title": "Low Severity CVEs Patching Cadence"
        },
        {
            "key": "service_vuln_host_high",
            "severity": "high",
            "factor": "patching_cadence",
            "title": "High-Severity Vulnerability in Last Observation"
        },
        {
            "key": "service_vuln_host_low",
            "severity": "low",
            "factor": "patching_cadence",
            "title": "Low-Severity Vulnerability in Last Observation"
        },
        {
            "key": "web_vuln_host_high",
            "severity": "high",
            "factor": "application_security",
            "title": "High Severity Content Management System vulnerabilities identified"
        },
        {
            "key": "web_vuln_host_medium",
            "severity": "medium",
            "factor": "application_security",
            "title": "Medium Severity Content Management System vulnerabilities identified"
        },
        {
            "key": "web_vuln_host_low",
            "severity": "low",
            "factor": "application_security",
            "title": "Low Severity Content Management System vulnerabilities identified"
        },
        {
            "key": "service_cassandra",
            "severity": "medium",
            "factor": "network_security",
            "title": "Apache Cassandra Service Observed"
        },
        {
            "key": "service_couchdb",
            "severity": "medium",
            "factor": "network_security",
            "title": "Apache CouchDB Service Observed"
        },
        {
            "key": "service_elasticsearch",
            "severity": "high",
            "factor": "network_security",
            "title": "Unauthenticated Elasticsearch Service Observed"
        },
        {
            "key": "service_ftp",
            "severity": "low",
            "factor": "network_security",
            "title": "FTP Service Observed"
        },
        {
            "key": "service_imap",
            "severity": "medium",
            "factor": "network_security",
            "title": "IMAP Service Observed"
        },
        {
            "key": "service_microsoft_sql",
            "severity": "medium",
            "factor": "network_security",
            "title": "Microsoft SQL Server Service Observed"
        },
        {
            "key": "service_mysql",
            "severity": "medium",
            "factor": "network_security",
            "title": "MySQL Service Observed"
        },
        {
            "key": "service_pop3",
            "severity": "info",
            "factor": "network_security",
            "title": "POP3 Service Observed"
        },
        {
            "key": "service_postgresql",
            "severity": "medium",
            "factor": "network_security",
            "title": "PostgreSQL Service Observed"
        },
        {
            "key": "service_rdp",
            "severity": "medium",
            "factor": "network_security",
            "title": "RDP Service Observed"
        },
        {
            "key": "service_redis",
            "severity": "medium",
            "factor": "network_security",
            "title": "Redis Service Observed"
        },
        {
            "key": "service_rsync",
            "severity": "medium",
            "factor": "network_security",
            "title": "rsync Service Observed"
        },
        {
            "key": "service_smb",
            "severity": "medium",
            "factor": "network_security",
            "title": "SMB Service Observed"
        },
        {
            "key": "service_telnet",
            "severity": "low",
            "factor": "network_security",
            "title": "Telnet Service Observed"
        },
        {
            "key": "service_vnc",
            "severity": "medium",
            "factor": "network_security",
            "title": "VNC Service Observed"
        },
        {
            "key": "ssh_weak_mac",
            "severity": "medium",
            "factor": "network_security",
            "title": "SSH Supports Weak MAC"
        },
        {
            "key": "ssh_weak_cipher",
            "severity": "medium",
            "factor": "network_security",
            "title": "SSH Supports Weak Cipher"
        },
        {
            "key": "service_end_of_life",
            "severity": "medium",
            "factor": "patching_cadence",
            "title": "End-of-Life Product"
        },
        {
            "key": "service_end_of_service",
            "severity": "medium",
            "factor": "patching_cadence",
            "title": "End-of-Service Product"
        },
        {
            "key": "tlscert_excessive_expiration",
            "severity": "low",
            "factor": "network_security",
            "title": "Certificate Lifetime Is Longer Than Best Practices"
        },
        {
            "key": "tlscert_revoked",
            "severity": "high",
            "factor": "network_security",
            "title": "Certificate Is Revoked"
        },
        {
            "key": "no_standard_browser_policy",
            "severity": "info",
            "factor": "endpoint_security",
            "title": "Multiple Browsers Detected"
        },
        {
            "key": "tlscert_self_signed",
            "severity": "medium",
            "factor": "network_security",
            "title": "Certificate Is Self-Signed"
        },
        {
            "key": "tlscert_expired",
            "severity": "medium",
            "factor": "network_security",
            "title": "Certificate Is Expired"
        },
        {
            "key": "tls_weak_cipher",
            "severity": "medium",
            "factor": "network_security",
            "title": "TLS Protocol Uses Weak Cipher"
        },
        {
            "key": "tlscert_weak_signature",
            "severity": "medium",
            "factor": "network_security",
            "title": "SSL Certificate Uses Weak Signature"
        },
        {
            "key": "tlscert_extended_validation",
            "severity": "positive",
            "factor": "network_security",
            "title": "Extended Validation Certificate Observed"
        },
        {
            "key": "service_vuln_host_medium",
            "severity": "medium",
            "factor": "patching_cadence",
            "title": "Medium-Severity Vulnerability in Last Observation"
        },
        {
            "key": "malware_1_day",
            "severity": "high",
            "factor": "ip_reputation",
            "title": "Malware Events, Last Day"
        },
        {
            "key": "malware_30_day",
            "severity": "medium",
            "factor": "ip_reputation",
            "title": "Malware Events, Last Month"
        },
        {
            "key": "malware_365_day",
            "severity": "low",
            "factor": "ip_reputation",
            "title": "Malware Events, Last Year"
        },
        {
            "key": "tls_ocsp_stapling",
            "severity": "positive",
            "factor": "network_security",
            "title": "TLS Certificate Status Request (\"OCSP Stapling\") Detected"
        },
        {
            "key": "ssh_weak_protocol",
            "severity": "high",
            "factor": "network_security",
            "title": "SSH Software Supports Vulnerable Protocol"
        },
    ],
}

ISSUE_DATA = {
    "entries": [
{
            "id": 138107,
            "date": "2019-08-29T00:00:00.000Z",
            "event_type": "issues",
            "group_status": "departed",
            "issue_count": 2,
            "total_score_impact": 0,
            "issue_type": "typosquat",
            "severity": "info",
            "factor": "cubit_score",
            "detail_url": "https://api.securityscorecard.io/companies/sacumen.com/history/events/2019-08-29/issues/typosquat?group_status=departed"
        },
        {
            "id": 228555,
            "date": "2019-08-28T00:00:00.000Z",
            "event_type": "issues",
            "group_status": "departed",
            "issue_count": 1,
            "total_score_impact": 0,
            "issue_type": "waf_detected",
            "severity": "positive",
            "factor": "application_security",
            "detail_url": "https://api.securityscorecard.io/companies/sacumen.com/history/events/2019-08-28/issues/waf_detected?group_status=departed"
        },
        {
            "id": 228556,
            "date": "2019-08-28T00:00:00.000Z",
            "event_type": "issues",
            "group_status": "departed",
            "issue_count": 1,
            "total_score_impact": 0.09963073358916574,
            "issue_type": "hsts_incorrect",
            "severity": "medium",
            "factor": "application_security",
            "detail_url": "https://api.securityscorecard.io/companies/sacumen.com/history/events/2019-08-28/issues/hsts_incorrect?group_status=departed"
        },
    ],
}

ISSUE_NO_DATA = {
    "entries": [],
}

PORTFOLIO_ID_1 = "5b36444aa317bf001ac86289"

PORTFOLIO_ID_2 = "5d3ad75fbcf3060022622348"

PORTFOLIO_ID_INVALID = 'abc123'

PORTFOLIO_LIST_DATA = {
    "entries": [
        {
            "id": PORTFOLIO_ID_1,
            "name": "Portfolio 1",
            "description": "These are all the vendors we monitor for security risk",
            "privacy": "private",
        },
        {
            "id": PORTFOLIO_ID_2,
            "name": "Portfolio 2",
            "description": "These are all the vendors we monitor for security risk",
            "privacy": "private"
        },
    ],
}

PORTFOLIO_1_COMANIES = {
    "entries": [
        {
            "domain": "example.com",
            "name": "example.com",
            "score": 90,
            "grade": "A",
            "grade_url": "https://s3.amazonaws.com/ssc-static/grades/factor_a.svg",
            "last30days_score_change": -6,
            "industry": "entertainment",
            "size": "unknown",
            "is_custom_vendor": False,
        },
        {
            "domain": "example.net",
            "name": "example.net",
            "score": 84,
            "grade": "B",
            "grade_url": "https://s3.amazonaws.com/ssc-static/grades/factor_b.svg",
            "last30days_score_change": 7,
            "industry": "information_services",
            "size": "unknown",
            "is_custom_vendor": False,
        },
    ],
}

PORTFOLIO_2_COMANIES = {
    "entries": [
        {
            "domain": "example.org",
            "name": "example.org",
            "score": 90,
            "grade": "A",
            "grade_url": "https://s3.amazonaws.com/ssc-static/grades/factor_a.svg",
            "last30days_score_change": -6,
            "industry": "entertainment",
            "size": "unknown",
            "is_custom_vendor": False,
        },
    ],
}

ACCESS_KEY = "ABC**********",
DOMAIN = "sacumen.com",
URL = "https://api.securityscorecard.io",
LEVEL_OVERALL_CHANGE = "77",
LEVEL_FACTOR_CHANGE = "77",
LEVEL_NEW_ISSUE_CHANGE = "77",
PORTFOLIO_IDS = None,
FETCH_HISTORICAL_DATA = False,
MONITOR_CONFIG = {"username": "", "fetch_company_issues": False, "fetch_portfolio_factors": False,
                       "level": "INFO", "logLevel": "info", "proxy_type": "http", "issue_level_findings": False,
                       "fetch_portfolio_issues": False, "fetch_company_overall": True,
                       "fetch_portfolio_overall": False, "host": "", "fetch_company_factors": False, "proxy": False,
                       "password": "", "port": ""},
DIFF_OVERRIDE_CONFIG = {"diff_override_portfolio_overall": False, "diff_override_own_factor": False,
                             "diff_override_own_overall": True, "diff_override_portfolio_factor": False},
proxy = None


RESULT_DATA = [ACCESS_KEY, DOMAIN, URL, LEVEL_OVERALL_CHANGE, LEVEL_FACTOR_CHANGE,
               LEVEL_NEW_ISSUE_CHANGE, PORTFOLIO_IDS, FETCH_HISTORICAL_DATA, MONITOR_CONFIG, DIFF_OVERRIDE_CONFIG, proxy]

RESULT_DATA1 = {

    "access_key": ACCESS_KEY,
    "domain": DOMAIN,
    "level_overall_change": LEVEL_OVERALL_CHANGE,
    "portfolio_ids": PORTFOLIO_IDS,
    "level_factor_change": LEVEL_FACTOR_CHANGE ,
    "level_new_issue_change": LEVEL_NEW_ISSUE_CHANGE,
    "last_run_date": "2019-11-29",
    "url": URL,
    "fetch_historical_data": FETCH_HISTORICAL_DATA,
    "proxy": {},
    "diff_override_config": DIFF_OVERRIDE_CONFIG,
    "monitor_config": MONITOR_CONFIG
}


JSON_DATA = {
    "key": "value"
}

