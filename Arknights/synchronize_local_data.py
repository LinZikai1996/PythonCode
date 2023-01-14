import requests
from bs4 import BeautifulSoup


def get_all_operator():
    response = requests.get("https://prts.wiki/w/CHAR?filter=AAAAAAAggAAAAAAAAAAAAAAAAAAAAAAA")
    html_source_info = BeautifulSoup(response.text, features='html.parser')
    # for operator in html_source_info.find_all('div', class_="smwdata")
    # return


if __name__ == '__main__':
    print(get_all_operator())
