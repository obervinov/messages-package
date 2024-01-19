"""
This module contains classes and methods
for assembling and sending telegram messages to the bot.
"""
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
        config_path: str = 'configs/messages.json'
    ) -> None:
        """
        Method for create a new messages instance.

        :param config: The path as a file containing a dictionary with message templates.
        :type config: str
        :default config: configs/messages.json
        """
        self.config_path = config_path
        with open(self.config_path, 'r', encoding='UTF-8') as config_json:
            self.data = json.load(config_json)
        config_json.close()

    def render_template(
        self,
        template_alias: str = None,
        **kwargs
    ) -> str | None:
        """
        Method for reading the text from the configuration file.

        :param template_alias: The name of the template key for extracting text from conifg.
        :type template_alias: str
        :default template_alias: None
        :param **kwargs: Passing additional parameters for message assembly.
        :type **kwargs: dict
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
            return None

    def render_progressbar(
        self,
        total_count: int = 0,
        current_count: int = 0
    ):
        """
        A Method for generating string with a progress bar based
        on the transmitted statistics data.

        :param total_count: An integer with the total counter value for the progress bar.
        :type total_count: int
        :default total_count: 0
        :param current_count: Counter of the current integer
            to calculate the percentage of self.total_count.
        :type current_count: int
        :default current_count: 0
        """
        procentage = math.ceil((current_count / total_count) * 100)
        progressbar = (
            f"\r[{emoji.emojize(':black_medium-small_square:') * int(procentage)}"
            f"{emoji.emojize(':white_medium_square:') * int((100 - procentage))}]{str(procentage)}%"
        )
        return progressbar
