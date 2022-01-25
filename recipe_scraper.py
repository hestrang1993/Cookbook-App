# -*- coding: utf-8 -*-
"""
The :module:`recipe_scraper` module allows me to scrape HTML files exported directly from the CookBook App and create 
text 
files from the recipe.
"""
import codecs
import os

from bs4 import BeautifulSoup

from make_file_safe_string import clean_filename


class RecipeScraper:
    """
    The :class:`RecipeScraper` class that will scrape the title, ingredients, and directions from HTML files directly 
    exported from the CookBook App.
    """

    def __init__(self, html_file_path, text_dir):
        """
        Create a new :class:`RecipeScraper` instance.
        
        Parameters
        ----------
        html_file_path : str
            The absolute file path to the HTML file exported from the CookBook App.
        text_dir : str
            The absolute file path to the directory that will store the text files.
        """
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
        """str: The absolute filepath to the HTML file that holds the recipe."""
        return self._html_file_path

    @property
    def text_dir(self):
        """str: The absolute filepath to the text file directory."""
        return self._text_dir

    @property
    def title_attr(self):
        """str: The HTML attribute that contains the title of the recipe."""
        return self._title_attr

    @property
    def title_dict(self):
        """dict: The search criteria for the title of the recipe."""
        return self._title_dict

    @property
    def notes_attr(self):
        """str: The HTML attribute that contains the ingredients and directions for the recipe."""
        return self._notes_attr

    @property
    def notes_dict(self):
        """dict: The search criteria for the ingredients and directions for the recipe."""
        return self._notes_dict

    @property
    def codecs_encoding(self):
        """str: The encoding used to read the HTML files. Default is UTF-8."""
        return self._codecs_encoding

    @property
    def os_root(self):
        """str: A OS formatter to create absolute filepaths."""
        return self._os_root

    @property
    def html_file(self):
        """str: The HTML file with the recipe I want to scrape."""
        return self._html_file

    @property
    def soup(self):
        """BeautifulSoup: The BeautifulSoup object that contains the recipe I want to scrape."""
        return self._soup

    @property
    def recipe_title(self):
        """str: The title of the recipe."""
        return self._recipe_title

    @property
    def text_file_name(self):
        """str: The file name to use for the text file."""
        return self._text_file_name

    @property
    def notes_result_set(self):
        """ResultSet: The description, ingredients, and directions for the recipe."""
        return self._notes_result_set

    @property
    def notes_text(self):
        """str: The ingredients and directions for the recipe. This object has been formatted with newlines to 
        improve readability."""
        return self._notes_text

    @property
    def notes_tag(self):
        """PageElement: The BeautifulSoup object that contains the notes and directions for the recipe."""
        return self._notes_tag

    @property
    def text_file_path(self):
        """str: The absolute file path for the text file that will contain the recipe title, ingredients, 
        and directions."""
        return self._text_file_path

    @staticmethod
    def format_text(tag):
        """
        Replace the :code:`<br/>` with :code:`/n`.
        
        Parameters
        ----------
        tag : PageElement
            The section of the notes I want to add newlines to.

        Returns
        -------
        str
            The recipe notes with newlines in the proper places.
        """
        tag_str = str(tag)
        tag_str = tag_str.replace("<br/>", "\n")
        tag_soup = BeautifulSoup(tag_str, "html.parser")
        return tag_soup.text

    def create_file_path_list(self, root_dir):
        """
        Parse through a specific directory.
        Then, create an absolute path string for every file in a directory (exclude subdirectories).
        Finally, return all these paths as a list.
        
        Parameters
        ----------
        root_dir : str
            The absolute path to the directory.
        Returns
        -------
        list:
            A list of all absolute filepaths for all files in a specific directory.
        """
        files = [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f))]
        files_list = []
        for file in files:
            file_path = os.path.join(self._os_root, root_dir, file)
            files_list.append(file_path)
        return files_list

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
