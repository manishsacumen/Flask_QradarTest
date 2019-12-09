class QpLib:

    def __init__(self):
        self.log_list = []

    def log(self, message, level='info'):
        self.log_list.append(message)

    def create_log(self):
        """
        self.add_log_handler(logger)
        self.log("Created log " + loggerName, 'info')
        :return:
        """
        self.log_list.append("Created log")

    def set_log_level(self, log_level='info'):
        return log_level

    def register_jsonld_endpoints(self):
        return True

    def get_console_address(self):
        return True
