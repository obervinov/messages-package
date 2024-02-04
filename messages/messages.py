"""
This module contains classes and methods
for assembling and sending telegram messages to the bot.
"""
import os
import json
import math
import re
import emoji


class Messages:
    """
    This class contains methods
    for assembling and sending telegram messages to the bot.
    """

    def __init__(
        self,
        config_path: str = None
    ) -> None:
        """
        Method for create a new messages instance.

        Args:
            config (str): the path as a file containing a dictionary with message templates.

        Returns:
            None

        Examples:
            >>> from messages import Messages
            >>> messages = Messages('configs/messages.json')
        """
        if os.environ.get("MESSAGES_CONFIG", None) is not None:
            self.config_path = os.environ.get("MESSAGES_CONFIG", None)
        elif config_path:
            self.config_path = config_path
        else:
            self.config_path = 'configs/messages.json'

        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='UTF-8') as config_json:
                try:
                    self.data = json.load(config_json)
                    config_json.close()
                except json.JSONDecodeError as json_error:
                    # pylint: disable=no-value-for-parameter
                    raise json.JSONDecodeError(
                        f"Configuration file {self.config_path} is not valid JSON: {json_error}\n"
                        "https://github.com/obervinov/messages-package?tab=readme-ov-file#-usage-examples"
                    )
        else:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

    def render_template(
        self,
        template_alias: str = None,
        **kwargs
    ) -> str | None:
        """
        Method for reading the text from the configuration file.

        Args:
            template_alias (str): the name of the template key for extracting text from conifg.

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
            template = self.data['templates'][template_alias]
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
        except KeyError:
            print(f"[Messages]: template not found: {template_alias}")
            return None

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
