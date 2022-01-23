# -*- coding: utf-8 -*-
from recipe_note_scraper import RecipeNoteScraper

test_html_file_path = "html/test.html"

recipe_note_scraper = RecipeNoteScraper(test_html_file_path)
recipe_note_text = recipe_note_scraper.note_text
print(recipe_note_text)
print(type(recipe_note_text))
print(recipe_note_scraper.title_text)

with open("test.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f'{recipe_note_scraper.title_text}\n')
    txt_file.write(recipe_note_scraper.note_text)
