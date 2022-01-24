from recipe_scraper import RecipeScraper

test_html_file_path = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\html\\CookBook-Recipe-Starter-Lasagna.html"
text_root = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\txt"

rs = RecipeScraper(test_html_file_path, text_root)
print(rs.recipe_title)
print(rs.text_file_path)
print(rs.notes_tag.text)
# rs.write_text_file()
