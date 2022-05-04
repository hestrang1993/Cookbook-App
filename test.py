from dir_file_list import DirFileLister
from dir_selector import DirSelector
from recipe_scraper import RecipeScraper


html_dir = DirSelector(title="Select Input Directory").dir_path
dfl = DirFileLister()
html_list = dfl.create_file_path_list(html_dir)

txt_dir = DirSelector(title="Select Output Directory").dir_path


def main_scraper():
    for html in html_list:
        rs = RecipeScraper(html, txt_dir)
        rs.write_text_file()


if __name__ == '__main__':
    main_scraper()
