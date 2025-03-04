from library import *


def get_file_html(path: str=None) -> None:
    return open(r'files_html\Март1.html')


def get_homework() -> None:
    soup = BeautifulSoup(get_file_html(), 'html.parser')
    print(soup)