def columnNameListToTsTableTitle(columnNameList: list):
    print("const temp = [")
    for columnName in columnNameList:
        print("    {")
        print(f"        title: '{columnName}',")
        print(f"        dataIndex: '{columnName}',")
        print("        valueType: 'text',")
        print("        ellipsis: true,")
        print("    },")
    print("]")


def columnNameListToTsClass(columnNameList: list):
    print("export type temp={")
    for columnName in columnNameList:
        print(f"{columnName}: string;")
    print("}")
