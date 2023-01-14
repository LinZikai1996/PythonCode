from Arknights.util.process_operator_info import preprocess_data_from_wiki

source_folder_path = '/Volumes/mobile_hard_disk/project/PythonCode/Test/resource'


def get_local_information(rarity: str):
    file_path = f"{source_folder_path}/{rarity}_information_from_wiki.txt"
    with open(file_path) as f:
        read_data = f.read()
    return preprocess_data_from_wiki(read_data)


def mock_information_from_wiki(rarity: str):
    file_path = f"{source_folder_path}/{rarity}_information_from_wiki.txt"
    with open(file_path) as f:
        read_data = f.read()
    return read_data
