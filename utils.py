from library import *


def get_file_html(path: str=None) -> None:
    return open(r'files_html/Март1.html')


def get_homework() -> None:
    soup = BeautifulSoup(get_file_html(), 'html.parser')
    data_div = soup.findAll('a', class_='block w-full cursor-pointer')
    for data in data_div:
        accept = data.find('div', class_='n-tag __tag-j9opmv-ps n-tag--strong n-tag--round').find('span', class_='n-tag__content').text
        date_accept, time_accept = regex.findall(r'(?<date>[0-9]{2}\.[0-9]{2}\.[0-9]{4}),\s(?<time>[0-9]{2}:[0-9]{2})', accept)[0]
        check = data.find('div', class_='n-tag __tag-j9opmv-ss n-tag--strong n-tag--round').find('span', class_='n-tag__content').text
        date_check, time_check = regex.findall(r'(?<date>[0-9]{2}\.[0-9]{2}\.[0-9]{4}),\s(?<time>[0-9]{2}:[0-9]{2})', check)[0]
        print(accept, date_accept, time_accept, check, date_check, time_check)
        # break