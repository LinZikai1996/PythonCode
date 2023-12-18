def read_input_to_list():
    print("请输入值，输入 'end' 结束：")
    result = []
    while True:
        user_input = input()
        if user_input == 'end':
            break
        result.append(user_input)
    return result


def process_input_list(input_list: list, separator: str = ',', get_data_index: int = 0):
    result = []
    for value in input_list:
        result.append(str(value).split(separator)[get_data_index].strip())
    return result
