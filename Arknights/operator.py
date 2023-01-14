import requests
from bs4 import BeautifulSoup

from Arknights.util.process_operator_info import get_general_info, preprocess_data_from_wiki, get_attribute_info, \
    get_talent_info, get_potential_info, get_skill_info, get_module_info


class Operator(object):

    def __init__(self):
        pass


def update_operator_info(operator_name: str):
    source = preprocess_data_from_wiki(
        get_information_from_wiki(operator_name)
    )
    operator_information = {}
    if source:
        operator_information['基本信息'] = get_general_info(source)
        operator_information['属性'] = get_attribute_info(source)
        operator_information['天赋'] = get_talent_info(source)
        operator_information['潜能'] = get_potential_info(source)
        operator_information['技能'] = get_skill_info(source)
        operator_information['模组'] = get_module_info(source)

    return operator_information


def get_information_from_wiki(operator_name: str):
    response = requests.get(rf'https://prts.wiki/index.php?title={operator_name}&action=edit')
    if response.ok:
        return BeautifulSoup(response.text, features='html.parser').find(id='wpTextbox1')
    else:
        print(f"ERROR: 未找到干员 ** {operator_name} ** 的wiki页面")
        return None
