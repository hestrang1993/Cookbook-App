# -*- coding: utf-8 -*-
import codecs
import os

from bs4 import BeautifulSoup

from make_file_safe_string import clean_filename


class RecipeScraper:

    def __init__(self, html_file_path, text_dir):
        self._html_file_path = html_file_path
        self._text_dir = text_dir
        self._title_attr = "h1"
        self._title_dict = {"itemprop": "name"}
        self._notes_attr = "span"
        self._notes_dict = {"itemprop": "description"}
        self._codecs_encoding = "utf-8"
        self._os_root = os.path.dirname(os.path.abspath(__file__))
        self._html_file = codecs.open(self.html_file_path, encoding=self.codecs_encoding).read()
        self._soup = BeautifulSoup(self.html_file, 'html.parser')
        self._recipe_title = self.soup.find(self.title_attr, self.title_dict).text
        self._text_file_name = clean_filename(f"{self.recipe_title}.txt")
        self._notes_result_set = self.soup.find_all(self.notes_attr, self.notes_dict)
        self._notes_tag = self.notes_result_set[1]
        self._notes_text = self.format_text(self.notes_tag)
        self._text_file_path = os.path.join(self.os_root, self.text_dir, self.text_file_name)

    @property
    def html_file_path(self):
        return self._html_file_path

    @property
    def text_dir(self):
        return self._text_dir

    @property
    def title_attr(self):
        return self._title_attr

    @property
    def title_dict(self):
        return self._title_dict

    @property
    def notes_attr(self):
        return self._notes_attr

    @property
    def notes_dict(self):
        return self._notes_dict

    @property
    def codecs_encoding(self):
        return self._codecs_encoding

    @property
    def os_root(self):
        return self._os_root

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
    def text_file_name(self):
        return self._text_file_name

    @property
    def notes_result_set(self):
        return self._notes_result_set

    @property
    def notes_text(self):
        return self._notes_text

    @property
    def notes_tag(self):
        return self._notes_tag

    @property
    def text_file_path(self):
        return self._text_file_path

    @staticmethod
    def format_text(tag):
        tag_str = str(tag)
        tag_str = tag_str.replace("<br/>", "\n")
        tag_soup = BeautifulSoup(tag_str, "html.parser")
        return tag_soup.text

    def write_text_file(self):
        """
        Write a text file with the notes of a recipe.
        Save the text file to a designated directory.

        Returns
        -------
        None
        """
        with open(self.text_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(f'{self.recipe_title}\n')
            txt_file.write(self.notes_text)
