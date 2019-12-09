class Helper(object):
    """ Mock for splunk helper."""

    input_type = 'test_input'
    index = 'main'
    sourcetype = 'expanse'

    def __init__(self, **kwargs):
        self.errors = []
        self.warnings = []
        self.infos = []
        self.debugs = []
        self.events = []

        self.checkpoints = {}

        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_input_type(self):
        return self.input_type

    def get_output_index(self):
        return self.index

    def get_sourcetype(self):
        return self.sourcetype

    def new_event(self, source=None, index=None, sourcetype=None, data=None):
        event = {
            'source': source,
            'index': index,
            'sourcetype': sourcetype,
            'data': data,
        }
        self.events.append(event)
        return event

    def get_arg(self, arg):
        return getattr(self, arg, None)

    def log_debug(self, message):
        self.debugs.append(message)

    def log_info(self, message):
        self.infos.append(message)

    def log_warning(self, message):
        self.warnings.append(message)

    def log_error(self, message):
        self.errors.append(message)

    def clear_logs(self):
        self.errors = []
        self.warnings = []
        self.infos = []
        self.debugs = []

    def get_proxy(self):
        return getattr(self, 'proxy', None)

    def set_checkpoints(self, data):
        self.checkpoints = data

    def get_check_point(self, key):
        return self.checkpoints.get(key)

    def save_check_point(self, key, value):
        self.checkpoints[key] = value


class EventWriter(object):
    """Mock for splunk event writer."""

    def __init__(self):
        self.events = []

    def write_event(self, event):
        self.events.append(event)

    def clear_events(self):
        self.events = []


class Company(object):
    def __init__(self, domain, portfolio_id=None, portfolio_name=None, **data):
        self.domain = domain

        if portfolio_id:
            self.portfolio_id = portfolio_id
        if portfolio_name:
            self.portfolio_name = portfolio_name

        self.overall_data = data.get('overall_data', [])
        self.factor_data = data.get('factor_data', [])
        self.issue_data = data.get('issue_data', ())
        # self.issue_data, self.issue_level_data = data.get('issue_data', ())
        # self.issue_level_data = data.get('issue_data', [])

    def get_overall_score(self, **config):
        return self.overall_data

    def get_factors(self, **config):
        return self.factor_data

    def get_issue_levels(self, **config):
        # return self.issue_data, self.issue_level_data
        return self.issue_data
