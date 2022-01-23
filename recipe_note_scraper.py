# -*- coding: utf-8 -*-
import codecs
import re

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
        self._note_attr = 'span'
        self._note_class = 'recipe-notes theme-action-text ng-binding ng-scope'
        self._recipe_note_html_path = recipe_note_html_path
        self._html_file = codecs.open(
            self._recipe_note_html_path, encoding='utf-8').read()
        self._soup = BeautifulSoup(self.html_file, 'html.parser')
        self._note_tag = self.soup.find_all(
            self.note_attr, class_=self.note_class)
        self._note_text = self._split_soup_text(self.note_tag)
        self._title_attr = 'h3'
        self._title_class = 'recipe-title ng-binding ng-scope'
        self._title_tag = self.soup.find(self.title_attr, class_=self.title_class)
        self._title_text = self.title_tag.text

    @property
    def note_attr(self):
        """
        str: The HTML attribute that contains the recipe notes.
        """
        return self._note_attr

    @property
    def note_class(self):
        """
        str: The class for the HTML tag that contains the recipe notes.
        """
        return self._note_class

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
    def note_tag(self):
        """
        ResultSet: The BeautifulSoup object that contains the text within the recipe notes.
        """
        return self._note_tag

    @property
    def note_text(self):
        return self._note_text

    @property
    def title_attr(self):
        """
        str: The HTML tag that contains the title of the recipe.
        """
        return self._title_attr

    @property
    def title_class(self):
        """
        str: The class used within the HTML tag that contains the title of the recipe.
        """
        return self._title_class

    @property
    def title_tag(self):
        """
        Tag: The BeautifulSoup object that contains the title of the recipe.
        """
        return self._title_tag

    @property
    def title_text(self):
        """
        str: The title of the recipe.
        """
        return self._title_text

    @staticmethod
    def _split_soup_text(soup_instance):
        """
        Remove all the extra spaces from text within a soup instance.
        Replace these extra spaces with newlines.
        
        Parameters
        ----------
        soup_instance : ResultSet
            The BeautifulSoup instance containing the text.
            
        Returns
        -------
        str
            A string containing the desired text, with useful formatting.
        """
        text_list = [element.string for element in soup_instance]
        text_list = [re.sub(r'[\t\r\n]\s{2,}', "", element) for element in text_list]
        text_str = str(text_list[0])
        text_str_sub = re.sub(r'\s{2,}', "\n", text_str)
        return text_str_sub
