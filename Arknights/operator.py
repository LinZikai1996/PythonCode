import requests
from bs4 import BeautifulSoup

from util.process_operator_info import get_general_info, preprocess_data_from_wiki, get_attribute_info, \
    get_talent_info, get_potential_info, get_skill_info, get_module_info
from util.file_util import write_path
from util.json_util import dict_to_json


# 跟新干员信息
def update_operator_info(operator_name=None):
    if operator_name is not None:
        print(f"更新 {operator_name} 的数据")
        write_path(dict_to_json(get_operator_info_by_name(operator_name)),
                   f'/Volumes/mobile_hard_disk/project/PythonCode/Arknights/operator_data/{operator_name}.json')
    else:
        name_list = get_all_operator_name_from_wiki()
        print(f"总共有 {len(name_list)} 干员")
        for name in name_list:
            print(f"更新 {name} 的数据")
            write_path(dict_to_json(get_operator_info_by_name(name)),
                       f'/Volumes/mobile_hard_disk/project/PythonCode/Arknights/operator_data/{name}.json')
    print("更新完毕")


def get_all_operator_name_from_wiki():
    operator_list = []
    response = requests.get("https://prts.wiki/w/CHAR?filter=AAAAAAAggAAAAAAAAAAAAAAAAAAAAAAA")
    if response.ok:
        for soup in BeautifulSoup(response.text, features='html.parser').find_all('div', class_='smwdata'):
            operator_list.append(soup['data-cn'])
    return operator_list


def get_operator_info_by_name(operator_name: str):
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
    response = requests.get(f'https://prts.wiki/index.php?title={operator_name}&action=edit')
    if response.ok:
        return BeautifulSoup(response.text, features='html.parser').find(id='wpTextbox1').text
    else:
        print(f"ERROR: 未找到干员 ** {operator_name} ** 的wiki页面")
        return None


# 展示数据
