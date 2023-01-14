from Arknights.util.process_operator_info import preprocess_data_from_wiki

source_folder_path = '/Volumes/mobile_hard_disk/project/PythonCode/Test/resource'


def get_local_information(rarity: str):
    file_path = f"{source_folder_path}/{rarity}_information_from_wiki.txt"
    return preprocess_data_from_wiki(_read_file(file_path))


def mock_information_from_wiki(rarity: str):
    file_path = f"{source_folder_path}/{rarity}_information_from_wiki.txt"
    return _read_file(file_path)


def mock_all_operator_name_from_wiki():
    file_path = f"{source_folder_path}/prts_html.txt"
    return _read_file(file_path)


def mock_hoshiguma_information_from_wiki():
    file_path = f"{source_folder_path}/hoshiguma_html.txt"
    return _read_file(file_path)


def _read_file(file_path):
    with open(file_path) as f:
        read_data = f.read()
    return read_data
