import requests
from bs4 import BeautifulSoup

from Arknights.util.process_operator_info import get_general_info


class Operator(object):

    def __init__(self):
        pass


def update_operator_info(operator_name: str):
    source = get_information_from_wiki(operator_name)
    if source:
        print(get_general_info(source.text))


def get_information_from_wiki(operator_name: str):
    response = requests.get(rf'https://prts.wiki/index.php?title={operator_name}&action=edit')
    if response.ok:
        return BeautifulSoup(response.text, features='html.parser').find(id='wpTextbox1')
    else:
        print(f"ERROR: 未找到干员 ** {operator_name} ** 的wiki页面")
        return None
