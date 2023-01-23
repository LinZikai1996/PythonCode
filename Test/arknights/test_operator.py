from unittest import mock
from unittest.mock import Mock, patch

import pytest

from Arknights.operator import get_information_from_wiki, get_all_operator_name_from_wiki, \
    get_operator_info_by_name
from Test.arknights import get_local_information, mock_information_from_wiki, mock_all_operator_name_from_wiki, \
    mock_hoshiguma_information_from_wiki
from util.process_operator_info import get_general_info, get_attribute_info, get_talent_info, \
    get_potential_info, get_skill_info, get_module_info
from util.translate_word import covert_english_to_chinese

information_list = [
    get_local_information("6"), get_local_information("5"), get_local_information("4"), get_local_information("3"),
    get_local_information("2"), get_local_information("1")
]


def test_get_all_operator_name_from_wiki():
    with patch('requests.get') as mock_data:
        mock_data.return_value.status_code = 200
        mock_data.return_value.text = mock_all_operator_name_from_wiki()
        print(get_all_operator_name_from_wiki())


def test_get_information_from_wiki_200():
    with patch('requests.get') as mock_data:
        mock_data.return_value.status_code = 200
        mock_data.return_value.text = mock_hoshiguma_information_from_wiki()
        print(get_information_from_wiki("星熊").text)


def test_get_general_info():
    print("Test get general information")
    for information in information_list:
        print(
            get_general_info(information)
        )


def test_get_attribute_info():
    print("Test get attribute information")
    for information in information_list:
        print(
            get_attribute_info(information)
        )


def test_get_talent_info():
    print("Test get talent information")
    for information in information_list:
        print(
            get_talent_info(information)
        )


def test_get_potential_info():
    print("Test get potential information")
    for information in information_list:
        print(
            get_potential_info(information)
        )


def test_get_skill_info():
    print("Test get skill information")
    for skill in information_list:
        print(
            get_skill_info(skill)
        )


def test_get_module_info():
    print("Test get module information")
    for module in information_list:
        print(
            get_module_info(module)
        )


@mock.patch('Arknights.operator.get_information_from_wiki', new=Mock(return_value=mock_information_from_wiki("6")))
def test_update_operator_info():
    print(get_operator_info_by_name("XXX"))


@pytest.mark.skip(reason="翻译函数，不能访问超过1000次/小时")
def test_translate_key_name():
    for key in get_general_info(information_list[0]).keys():
        print(f"{key} : {str(covert_english_to_chinese(key))}")

    for key in get_attribute_info(information_list[0]).keys():
        print(f"{key} : {str(covert_english_to_chinese(key))}")

    for key in get_talent_info(information_list[0]).keys():
        print(f"{key} : {str(covert_english_to_chinese(key))}")

    for key in get_potential_info(information_list[0]).keys():
        print(f"{key} : {str(covert_english_to_chinese(key))}")

    for key in get_skill_info(information_list[0]).keys():
        print(f"{key} : {str(covert_english_to_chinese(key))}")

    for key in get_module_info(information_list[0]).keys():
        print(f"{key} : {str(covert_english_to_chinese(key))}")
