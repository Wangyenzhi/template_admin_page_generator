import requests
from hashlib import md5
import random
import json


def get_user_input(placeholder):
    res = input(f'{placeholder}\n')
    return res


#  字符串驼峰命名
def convert(one_string, space_character):
    string_list = str(one_string).split(space_character)  # 将字符串转化为list
    first = string_list[0].lower()
    others = string_list[1:]
    others_capital = [f'{word[0].capitalize()}{word[1:]}' for word in others]  # str.capitalize():将字符串的首字母转化为大写
    others_capital[0:0] = [first]
    hump_string = ''.join(others_capital)  # 将list组合成为字符串，中间无连接符。
    return hump_string


#  list排序
def sort_p(s_arr):
    print('intP', [f'{index}、{s_arr[index]["label"]}' for index in range(len(s_arr))])
    is_sort = input('输入调整后的参数顺序以,或、分割（不需要请直接按回车）')
    if is_sort:
        # print(is_sort.split(','))
        return [s_arr[int(index)] for index in is_sort.split(',' if ',' in is_sort else '、')]
    else:
        return s_arr


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


# 翻译
def translate(string):
    # Set your own appid/appkey.
    appid = '20221008001377553'
    appkey = 'cUpgqYUPOSf9Xv8ULudK'

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'zh'
    to_lang = 'en'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = string

    # Generate salt and sign

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    result = json.dumps(result, indent=4, ensure_ascii=False)
    result = json.loads(result)
    # print()

    print(result["trans_result"][0])
    # print(result['trans_result'][0]['dist'])
    try:
        return result['trans_result'][0]['dst']
    except:
        return False
