from dir_file_list import DirFileLister
from recipe_scraper import RecipeScraper

html_dir = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\html"
dfl = DirFileLister()
html_list = dfl.create_file_path_list(html_dir)

test_html_file_path = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\html\\CookBook-Recipe-Starter-Lasagna.html"
text_root = "C:\\Users\\harri\\PycharmProjects\\Cookbook-App\\txt"


def main():
    for html in html_list:
        rs = RecipeScraper(html, text_root)
        rs.write_text_file()


if __name__ == '__main__':
    main()
