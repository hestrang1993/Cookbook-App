# -*- coding: utf-8 -*-
from recipe_note_scraper import RecipeNoteScraper

test_html_file_path = "html/test.html"
text_root = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\txt"

rns = RecipeNoteScraper(test_html_file_path, text_root)
rns.write_text_file()
