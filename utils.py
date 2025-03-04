from settings.library import *


def get_file_html(path: str=None) -> None:
    if path:
        return open(path, encoding='utf-8')

    return open(r'files_html/Март1.html', encoding='utf-8')


def __correct_data(info: str) -> tuple[str]:
    date, time = regex.findall(DATE_TIME, info)[0]
    return date, time


def get_homeworks(path: str) -> list[list[str]]:
    homeworks: list[list[str]] = []
    for html in os.listdir(path):
        html = get_file_html(rf'{path}/{html}')

        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        data_div = soup.findAll('a', class_='block w-full cursor-pointer')
        for data in data_div:
            accept = data.find('div', class_='n-tag __tag-j9opmv-ps n-tag--strong n-tag--round').find('span', class_='n-tag__content').text
            check = data.find('div', class_='n-tag __tag-j9opmv-ss n-tag--strong n-tag--round').find('span', class_='n-tag__content').text
            accept_date, accept_time = __correct_data(accept)
            check_date, check_time = __correct_data(check)
            homeworks += [[accept_date, accept_time, check_date, check_time]]
    
    return homeworks


def show_homeworks(homeworks: list[list[str]]) -> None:
    for homework in homeworks:
        print(homework)