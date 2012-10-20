"""
Sublime-Pokemonize

Plugin with text command for randomizing letter case
("pokemonizing") of selected text region.

:author: Karol Kuczmarski "Xion"
"""
import unicodedata
from random import random

from sublime_plugin import TextCommand


class Pokemonize(TextCommand):
    """Class for the 'pokemonize' text command."""

    def run(self, edit):
        selected = (reg for reg in self.view.sel() if not reg.empty())
        for region in selected:
            text = pokemonize(self.view.substr(region))
            self.view.replace(edit, region, text)


def pokemonize(text, intensity=1.0):
    """Randomizes case of letters in given text.

    :param intensity: Probability for a letter to have its case randomized
                      rather than being left as is

    :return: Transformed text (as Unicode string)
    """
    if not isinstance(text, unicode):
        text = text.decode('ascii', 'ignore')

    is_letter = lambda c: unicodedata.category(c).startswith('L')
    random_case = lambda c: c.upper() if random() < 0.5 else c.lower()
    transform = lambda c: (random_case(c)
                           if is_letter(c) and random() < intensity else c)

    return u''.join(map(transform, text))
