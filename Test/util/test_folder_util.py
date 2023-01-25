from Util.folder_util import get_all_files_under_folder


def test_get_all_files_under_folder():
    result = get_all_files_under_folder(
        "/Volumes/mobile_hard_disk/project/PythonCode/Recognition_credit_card_number/resource/image")

    print(result)