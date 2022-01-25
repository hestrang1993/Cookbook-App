from dir_file_list import DirFileLister
from recipe_scraper import RecipeScraper

html_dir = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\html"
dfl = DirFileLister()
html_list = dfl.create_file_path_list(html_dir)

test_html_file_path = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\html\\CookBook-Recipe-Starter-Lasagna.html"
text_root = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\txt"

test_text_file_path = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\txt\\A_Family_Affair_Chicken_Parmesan_Sliders" \
                      ".txt"


def main_scraper():
    for html in html_list:
        rs = RecipeScraper(html, text_root)
        rs.write_text_file()


if __name__ == '__main__':
    main_scraper()
