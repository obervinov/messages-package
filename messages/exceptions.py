"""
This module contains custom exceptions that are used in the application.
"""


class ConfigurationIsNotValid(Exception):
    """
    Exception raised when the configuration file is not valid JSON.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TemplateNotFound(Exception):
    """
    Exception raised when the template is not found in the configuration file.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TemplatesIsNotValid(Exception):
    """
    Exception raised when the templates is not valid.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
