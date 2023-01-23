def write_path(data, path):
    with open(path, encoding="utf-8", mode="w") as txt:
        txt.writelines(data + '\n')


def read_line(path):
    with open(path, 'r') as txt:
        data = txt.read()
        return data
