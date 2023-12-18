from development_tools.input_tool import read_input_to_list, process_input_list
from development_tools.ts_tool import columnNameListToTsTableTitle

if __name__ == '__main__':
    columnNameListToTsTableTitle(process_input_list(read_input_to_list(), ':'))
