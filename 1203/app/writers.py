import datetime
import json
from collections import OrderedDict
from formatters import format_date_string

from config import (EVENT_ID_OVERALL, EVENT_ID_FACTOR, EVENT_ID_ISSUE,
                    PRODUCT_OVERALL, PRODUCT_FACTOR, PRODUCT_ISSUE, CHECKPOINT_NAME)
from scorecard_exceptions import InvalidAPIKeyError, InvalidJSONError, NoDataError, ServerError
from utils import build_leef


class CompanyWriter(object):

    def __init__(self, company, helper, leef_logger):
        self.__company = company
        self.leef_logger = leef_logger
        self.__helper = helper

    def write_overall(self, **config):
        self.__helper.log_info("Started processing Overall.")
        try:
            scores = self.__company.get_overall_score(**config)
        except KeyError:
            self.__helper.log_error("Getting overall score for {} to {} returned only "
                                    "1 entry for getting difference it needed  at least "
                                    "two entry".format(config['from_date'], config['to_date']))
        except InvalidAPIKeyError as e:
            self.__helper.log_error("API key is invalid or expired. "
                                    "Please validate that your token is entered correctly")
            self.__helper.log_error(str(e))
            return
        except NoDataError as e:
            self.__helper.log_error("No Overall data found in between {} to {}".format(config['from_date'],
                                                                                       config['to_date']))
            self.__helper.log_error(str(e))
        except InvalidJSONError as e:
            self.__helper.log_error("Data received from API is not in JSON format")
            self.__helper.log_error(str(e))
        except ServerError as e:
            self.__helper.log_error("Sever error occurred while calling the API")
            self.__helper.log_error(str(e))
        except Exception as e:
            self.__helper.log_error("Error in fetching company overall")
            self.__helper.log_error(str(e))
            raise
        else:
            # Write overall score for company
            self.__helper.log_info("Total overall data received = {} ".format(len(scores)))

            self.__helper.log_debug("overall data is {} ".format(scores))
            try:
                from_date = scores[-1]['todayDateValue'][:10]
                new_from_date = str(datetime.datetime.strptime(from_date, '%Y-%m-%d') + datetime.timedelta(days=1))[:10]
            except Exception as err:
                self.__helper.log_error('Error {} occurred while fetching from date'.format(err))
                self.__helper.log_debug('setting from date with empty value.')
                new_from_date = ''
            override = config.get('diff_override_portfolio_overall') \
                if config.get('portfolioId') and config.get('portfolioName') \
                else config.get('diff_override_own_overall')
            self.__helper.log_debug("Writing in overall file")
            with open("overall_log.txt", 'a+') as f:
                for score in scores:

                    if score.get('diff') != 0 or override:
                        # score.pop('diff', None)
                        score.update({'sev': config['level_overall_change']})

                        # Insert portfolio id and name if present
                        if config.get('portfolioId') and config.get('portfolioName'):
                            score.update({
                                'portfolioId': config['portfolioId'],
                                'portfolioName': config['portfolioName'],
                            })
                        try:
                            item = build_leef(score, EVENT_ID_OVERALL, PRODUCT_OVERALL,
                                              config.get('diff_override_overall', True))

                            f.write(item)
                            self.leef_logger.info(item)
                        except Exception as err:
                            self.__helper.log_error("Getting error as {}".format(err))
                            f.write("Getting error while building leef, as {}".format(err))

                else:
                    try:
                        self.__helper.log_info("Creating new checkpoint as {}".format(new_from_date))
                        self.__helper.save_check_point(CHECKPOINT_NAME, new_from_date)
                    except Exception as err:
                        self.__helper.log_error("Getting error while setting checkpoint, as {}".format(err))
                self.__helper.log_info("leef created for overall")

    def write_factors(self, **config):
        self.__helper.log_info("Started processing Factors.")
        try:
            factors = self.__company.get_factors(**config)
            # self.__helper.log_debug("Factor is --------{}".format(factors))
        except IndexError:
            self.__helper.log_error("Getting factor score from {} to {} returned only "
                                    "1 entry for getting difference it needed  at least "
                                    "two entry".format(config['from_date'], config['to_date']))
        except NoDataError as e:
            self.__helper.log_error("No factor data found in between {} to {}.".format(config['from_date'],
                                                                                       config['to_date']))
            self.__helper.log_error(str(e))
        except InvalidJSONError as e:
            self.__helper.log_error("Data received from API is not in JSON format")
            self.__helper.log_error(str(e))
        except ServerError as e:
            self.__helper.log_error("Server error occurred while calling the factors API")
            self.__helper.log_error(str(e))
        except Exception as e:
            self.__helper.log_error("Error in fetching company factors")
            self.__helper.log_error(str(e))
            raise
        else:
            self.__helper.log_info("Total Factors received = {} ".format(len(factors)))
            factor_flag = config.get('diff_override_portfolio_factor') \
                if config.get('portfolioId') and config.get('portfolioName') \
                else config.get('diff_override_own_factor')
            with open("factor.txt", 'a+') as f:
                for factor in factors:
                    try:
                        if factor.get('diff') != 0 or factor_flag:
                            # factor.pop('diff', None)
                            factor.update({'sev': config['level_factor_change']})

                            # Insert portfolio id and name if present
                            if config.get('portfolioId') and config.get('portfolioName'):
                                factor.update({
                                    'portfolioId': config['portfolioId'],
                                    'portfolioName': config['portfolioName'],
                                })

                            try:
                                item = build_leef(factor, EVENT_ID_FACTOR, PRODUCT_FACTOR, True)
                                # self.__helper.log_info("Factor item is  {}".format(item))
                                f.write(item)
                                self.leef_logger.info(item)
                            except Exception as err:
                                self.__helper.log_error("Getting error as {}".format(err))
                                f.write("Getting error while building leef, as {}".format(err))
                    except Exception as err:
                        self.__helper.log_error("Factor error is --------{}".format(err))

                self.__helper.log_info("Leef created for factor.")

    def write_issues(self, **config):
        self.__helper.log_info("Started processing Issues.")
        try:
            issues, issue_detail_list = self.__company.get_issue_levels(**config)
            self.__helper.log_info("issue detail len is {}".format(issue_detail_list))
            self.__helper.log_info("issue detail data is {}".format(issue_detail_list[:4]))
        except NoDataError as e:
            self.__helper.log_error("No issue data found in between {} to {}".format(config['from_date'], config['to_date']))
            self.__helper.log_error(str(e))
        except InvalidJSONError as e:
            self.__helper.log_error("Data received from API is not in JSON format.")
            self.__helper.log_error(str(e))
        except ServerError as e:
            self.__helper.log_error("Server error occurred while calling the API.")
            self.__helper.log_error(str(e))
        except Exception as e:
            self.__helper.log_error("Error in fetching company issues")
            self.__helper.log_error(str(e))
            raise
        else:
            self.__helper.log_info('Total Issues received = {} '.format(len(issues)))
            self.__helper.log_debug("Writing in issue file")
            with open("issue.txt", 'a+') as f:
                for issue in issues:
                    issue.update({'sev': config['level_new_issue_change']})
                    # issue.update({'diff': -1})

                    # Insert portfolio id and name if present
                    if config.get('portfolioId') and config.get('portfolioName'):
                        issue.update({
                            'portfolioId': config['portfolioId'],
                            'portfolioName': config['portfolioName'],
                        })
                    try:
                        item = build_leef(issue, EVENT_ID_ISSUE, PRODUCT_ISSUE, True)
                        f.write(item)
                        self.leef_logger.info(item)
                    except Exception as err:
                        self.__helper.log_error("Getting error as {}".format(err))
                        f.write("Getting error while building leef, as {}".format(err))

                self.__helper.log_info("Leef created for Issue.")
            try:
                if config['issue_level_findings']:
                    self.__helper.log_info("Writing in issue detail file, len of issue detail is {}".format(issue_detail_list))
                    # custom_issue_dict = {}
                    with open("issue_detail.txt", 'a+') as f:
                        for issue_details in issue_detail_list:

                            custom_issue_dict = OrderedDict([('cat', 'issue_Findings'),
                                                             ('eventType', 'Issues Findings'),
                                                             ('eventSource', 'Issue_Findings'),
                                                             ('domain', issue_details.get('parent_domain', 'not available')),
                                                             ('devTime', format_date_string(issue_details.get('first_seen_time'))),
                                                             ('eventID', issue_details.get('eventId', 'not available')),
                                                             ('groupStatus', issue.get('groupStatus', 'not available')),
                                                             ('issueType', issue_details.get('issueType', 'not available')),
                                                             ('issue_id', issue_details.get('issue_id', 'not available')),
                                                             ('ssc_domain', issue_details.get('ssc_domain', 'not available')),
                                                             ('parent_domain', issue_details.get('parent_domain', 'not available')),
                                                             ('custom_issue_details', "'{}'".format(json.dumps(issue_details))),
                                                             ('diff', -1), ])

                            self.__helper.log_info("created custom issue dict-----------------")

                            try:
                                self.__helper.log_info("Creating leef for issue level findings")
                                item = build_leef(custom_issue_dict, EVENT_ID_ISSUE, PRODUCT_ISSUE, True)
                                self.__helper.log_info("issue level is \n{}".format(item))

                                f.write(str(item))
                                self.leef_logger.info(item)
                            except Exception as err:
                                self.__helper.log_error("Getting error while building leef, as {}".format(err))
                                f.write("Getting error as {}".format(err))

                else:
                    self.__helper.log_info("Not fetching issue level findings.")
            except Exception as err:
                self.__helper.log_error("Getting error while calling issue level as {}.".format(err))
