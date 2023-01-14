from Arknights.operator import get_information_from_wiki
from Arknights.util.process_operator_info import get_general_info, get_attribute_info, get_talent_info, \
    get_potential_info, get_skill_info
from Test.arknights import get_local_information

information_list = [
    get_local_information("6"), get_local_information("5"), get_local_information("4"), get_local_information("3"),
    get_local_information("2"), get_local_information("1")
]


def test_get_information_from_wiki():
    print(get_information_from_wiki("伊芙利特").text)


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
