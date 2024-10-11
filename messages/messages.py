"""This module contains classes and methods for assembling and sending telegram messages to the bot."""
import os
import json
import math
import re
import emoji
from .exceptions import ConfigurationIsNotValid, TemplateNotFound, TemplatesIsNotValid


class Messages:
    """
    This class contains methods for assembling and sending telegram messages to the bot.

    Attributes:
        configuration (dict): the contents of the configuration file.

    Exceptions:
        ConfigurationIsNotValid: raised when the configuration file is not valid JSON.
        TemplateNotFound: raised when the template is not found in the configuration file.
        TemplatesIsNotValid: raised when the templates is not valid.

    Examples:
        >>> from messages import Messages
        >>> messages = Messages('configs/messages.json')
        >>> messages.render_template('test_message', username='pytest')
    """

    def __init__(self, config_path: str = 'configs/messages.json') -> None:
        """
        Method for create a new messages instance.

        Args:
            config (str): the path as a file containing a dictionary with message templates.
        """
        env_variable = os.environ.get("MESSAGES_CONFIG", None)

        if env_variable:
            config_file = env_variable
        else:
            config_file = config_path

        self.configuration = self._read_configuration(config_file=config_file)

        if not self._templates_is_valid():
            raise TemplatesIsNotValid(
                "Templates have invalid elements. Please check your configuration file. "
                "Otherwise, check examples: https://github.com/obervinov/messages-package?tab=readme-ov-file#-usage-examples"
            )

    def _read_configuration(self, config_file: str = None) -> dict:
        """
        Method for checking the validity of the configuration file and reading its contents.

        Args:
            config_file (str): the path as a file containing a dictionary with message templates.

        Returns:
            dict: the contents of the configuration file.
        """
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='UTF-8') as config_json:
                try:
                    return json.load(config_json)
                except json.JSONDecodeError as json_error:
                    raise ConfigurationIsNotValid(
                        "Configuration file structure is not valid JSON. Please check examples: "
                        "https://github.com/obervinov/messages-package?tab=readme-ov-file#-usage-examples"
                    ) from json_error
        else:
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

    def _templates_is_valid(self) -> bool:
        """
        Method for checking the validity of the templates in the configuration file.

        Returns:
            bool: True if the templates are valid, False otherwise.
        """
        if 'templates' in self.configuration:
            for template in self.configuration['templates'].values():
                if 'text' not in template or 'args' not in template.values():
                    print(f"[Messages]: there are no text or args in template {template}")
                    return False
                if not isinstance(template['text'], str) or not isinstance(template['args'], list):
                    print(f"[Messages]: text or args in template {template} has an invalid data type")
                    return False
                args_provided = len(template['args'])
                args_expected = len(re.findall(r"{.*?}", template['text']))
                if args_provided != args_expected:
                    print(f"[Messages]: the number of arguments in the template {template} does nots match")
                    return False
        return True

    def render_template(
        self,
        template_alias: str = None,
        **kwargs
    ) -> str | None:
        """
        Method for reading the text from the configuration file.

        Args:
            template_alias (str): the name of the template key for extracting text from config.

        Keyword Args:
            **kwargs: passing additional parameters for message assembly.

        Returns:
            str: the text of the message assembled from the template.
            None: if the template is not found in the configuration file.

        Examples:
            >>> from messages import Messages
            >>> messages = Messages('configs/messages.json')
            >>> messages.render_template('test_message', username='pytest')
        """
        try:
            template = self.configuration['templates'][template_alias]
            arguments = []
            for arg in template['args']:
                if re.match(r":.*:", arg):
                    # Rendering emojis
                    arguments.append(emoji.emojize(arg))
                else:
                    # Rendering kwargs variables
                    arguments.append(kwargs.get(arg))
            # Building full message
            return template['text'].format(*arguments)
        except KeyError as error:
            print(f"[Messages]: template not found: {template_alias}")
            raise TemplateNotFound(
                "Template not found in the configuration file. Please check your configuration file."
            ) from error

    def render_progressbar(
        self,
        total_count: int = 0,
        current_count: int = 0
    ) -> str | None:
        """
        A Method for generating string with a progress bar based
        on the transmitted statistics data.

        Args:
            total_count (int): an integer with the total counter value for the progress bar.
                Defaults to 0.
            current_count (int): counter of the current integer to calculate the percentage of total_count.
                Defaults to 0.
        Returns:
            str: string with a progress bar.
            None: if the total_count is 0.

        Examples:
            >>> from messages import Messages
            >>> messages = Messages('configs/messages.json')
            >>> messages.render_progressbar(100, 19)
        """
        percentage = math.ceil((current_count / total_count) * 100)
        progressbar = (
            f"\r[{emoji.emojize(':black_medium-small_square:') * int(percentage)}"
            f"{emoji.emojize(':white_medium_square:') * int((100 - percentage))}]{str(percentage)}%"
        )
        return progressbar
