from settings.settings import *


def get_file_html(path: str=None) -> None:
    if path:
        return open(path, encoding='utf-8')

    return open(r'files_html/Март1.html', encoding='utf-8')


def __correct_data(info: str) -> tuple[str]:
    date, time = regex.findall(DATE_TIME, info)[0]
    return date, time


def __convert_to_datetime(data: list[str]) -> None:
    data[0] = datetime.datetime.strptime(data[0], '%d.%m.%Y')
    data[2] = datetime.datetime.strptime(data[2], '%d.%m.%Y')
    data[1] = datetime.datetime.strptime(data[1], '%H:%M')
    data[3] = datetime.datetime.strptime(data[3], '%H:%M')


def get_homeworks(path: str) -> list[list[str]]:
    homeworks: list[list[str]] = []
    for html in os.listdir(path):
        html = get_file_html(rf'{path}/{html}')

        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        data_a = soup.findAll('a', class_='block w-full cursor-pointer')
        for data in data_a:
            accept = data.find('div', class_='n-tag __tag-j9opmv-ps n-tag--strong n-tag--round').find('span', class_='n-tag__content').text
            check = data.find('div', class_='n-tag __tag-j9opmv-ss n-tag--strong n-tag--round').find('span', class_='n-tag__content').text
            accept_date, accept_time = __correct_data(accept)
            check_date, check_time = __correct_data(check)
            data = [accept_date, accept_time, check_date, check_time]
            __convert_to_datetime(data)
            if data not in homeworks:
                homeworks += [data]
    
    return sorted(homeworks, key=lambda x: x[0].day, reverse=True)


def show_homeworks(homeworks: list[list[str]], month: int=None) -> None:
    for homework in homeworks:
        if month:
            if homework[0].month == month:
                print(homework)
        
        else:
            print(homework)