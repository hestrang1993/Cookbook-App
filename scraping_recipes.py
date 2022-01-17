# -*- coding: utf-8 -*-
from recipe_note_scraper import RecipeNoteScraper

test_html_file_path = "html/test.html"

recipe_note_scraper = RecipeNoteScraper(test_html_file_path)
recipe_note_text = recipe_note_scraper.note_text
print(recipe_note_text)
print(type(recipe_note_text))
