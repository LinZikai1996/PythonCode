from tool.folder_util import get_all_files_under_folder


def test_get_all_files_under_folder():
    result = get_all_files_under_folder(
        "/opencv_learn_code/resource/image")

    print(result)