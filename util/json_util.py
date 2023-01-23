import json


def dict_to_json(source: dict, format_or_not=True):
    if format_or_not:
        return json.dumps(source, ensure_ascii=False, indent=4, separators=(',', ':'))

    else:
        return json.dumps(source)