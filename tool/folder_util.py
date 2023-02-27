import os


def get_all_files_under_folder(path, file_type=None):
    file_list = []
    list_path = os.listdir(path)
    for file_name in list_path:
        if file_type is not None and str(path).endswith(file_type):
            file_list.append(f"{path}/{file_name}")
        else:
            file_list.append(f"{path}/{file_name}")

    return file_list
