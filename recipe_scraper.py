# -*- coding: utf-8 -*-
import codecs
import os

from bs4 import BeautifulSoup

from make_file_safe_string import clean_filename


# import re


class RecipeScraper:

    def __init__(self, html_file_path):
        self._title_attr = "h1"
        self._title_dict = {"itemprop": "name"}
        self._notes_attr = "span"
        self._notes_dict = {"itemprop": "description"}
        self._codecs_encoding = "utf-8"
        self._os_root = os.path.dirname(os.path.abspath(__file__))
        self._html_file_path = html_file_path
        self._html_file = codecs.open(self.html_file_path, encoding=self._codecs_encoding).read()
        self._soup = BeautifulSoup(self.html_file, 'html.parser')
        self._recipe_title = self.soup.find(self._title_attr, self._title_dict).text
        self._txt_file_name = clean_filename(f"{self.recipe_title}.txt")
        self._notes_result_set = self.soup.find_all(self._notes_attr, self._notes_dict)

    @property
    def html_file_path(self):
        return self._html_file_path

    @property
    def html_file(self):
        return self._html_file

    @property
    def soup(self):
        return self._soup

    @property
    def recipe_title(self):
        return self._recipe_title

    @property
    def txt_file_name(self):
        return self._txt_file_name

    @property
    def notes_result_set(self):
        return self._notes_result_set
