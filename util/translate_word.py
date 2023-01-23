import json
import requests


def covert_english_to_chinese(word):
    # 翻译函数，word 需要翻译的内容
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.ok:
        result = json.loads(response.text)
        return result['translateResult'][0][0]['tgt']
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None

