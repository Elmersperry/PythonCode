# import requests
# from bs4 import BeautifulSoup as Bs
#
# def get_html(url: str) -> str:
#     response = requests.get(url)
#     status = response.status_code
#     print(f"Код ответа - {status}")
#     html = response.text
#     print(html)
#     return  html
#
# def parse_html(html: str):
#     soup: Bs = Bs(html, "html.parser")
#     current_date = soup.find("h2", class_="h2 blue").text.split("\n")
#     pass
#
#
# URL = "https://www.alta.ru/currency/"
# html = get_html(URL)
# parse_html(html)
import json
from textwrap import indent

import requests
from bs4 import BeautifulSoup as BS
from requests.exceptions import ConnectionError
def get_HTML(url: str) -> str|None:
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200 and str(status)[0] != 3:  # 404,503,301
            # print(f'Ошибка запроса. Код ответа - {status}')
            print(f"Код ответа - {status}")
            return None
        html = response.text
    except Exception as error:
        print('Нет ответа от сервера')
        print(error)
        return None
def parse_html(html: str):
    soup: BS = BS(html, "html.parser")
    current_date = (soup.find("h2", class_="h2 blue").text.split("\n")[-1].strip()[:10])
    table = soup.find("div", class_="module-tableSort")
    rows = table.find_all('tr')[2:]
    for row in rows:
        if not row.find('td', class_='t-center'):
            continue
            code = row.find('td', class_='t-center').text
            number_code = code.split()[0]
            txt_code = code.split()[1]
        name = row.find('td', class_='t-left').text
        value = row.find('td', class_='t-right').text
        print(f'{code} {name} {value}')
        pass

def write_data_to_json(data: dict) -> None:
    with open("courses.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_data_from_json(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

url = "https://www.alta.ru/currency/"
html = get_HTML(url)
if html:
    courses = parse_html(html)
    write_data_to_json(data=courses)



# почитать про статус-код (400 - ошибки на стороне клиента, 500 - ошибки на стороне сервера)