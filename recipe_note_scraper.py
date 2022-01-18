# -*- coding: utf-8 -*-
import codecs

from bs4 import BeautifulSoup


class RecipeNoteScraper:
    """
     The RecipeNoteScraper class uses codecs and BeautifulSoup to scrape the notes from my mom's recipe app.
    """

    def __init__(self, recipe_note_html_path):
        """
        Create a new instance of RecipeNoteScraper.

        Parameters
        ----------
        recipe_note_html_path : str
            The absolute file path to the HTML file containing the recipe text.
        """
        self._html_attr = 'span'
        self._attr_class = 'recipe-notes theme-action-text ng-binding ng-scope'
        self._recipe_note_html_path = recipe_note_html_path
        self._html_file = codecs.open(
            self._recipe_note_html_path, encoding='utf-8').read()
        self._soup = BeautifulSoup(self._html_file, 'html.parser')
        self._note_text = str(self._soup.find(
            self.html_attr, class_=self._attr_class))

    @property
    def html_attr(self):
        """
        str: The HTML attribute that contains the recipe notes.
        """
        return self._html_attr

    @property
    def attr_class(self):
        """
        str: The class for the HTML tag that contains the recipe notes.
        """
        return self._attr_class

    @property
    def recipe_note_html_path(self):
        """
        str: The absolute file path to the HTML file containing the recipe text.
        """
        return self._recipe_note_html_path

    @property
    def html_file(self):
        """
        _Decoded: The HTML file object, read and decoded into UTF-8.
        """
        return self._html_file

    @property
    def soup(self):
        """
        BeautifulSoup: A BeautifulSoup object that contains the recipe notes.
        """
        return self._soup

    @property
    def note_text(self):
        """
        str: The text within the recipe notes.
        """
        return self._note_text
