import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)


import os
import requests
import base64
from fontTools.ttLib import TTFont
def init_num_map():
    map = {}
    font = TTFont('/Users/jw/PycharmProjects/python-js/猿人学/07/0.txt')
    glyphNames =font.getGlyphNames()[1:]
    # https: // wakamaifondue.com / 获取数字映射数据
    nums = [1,2,4,0,7,9,8,3,5,6]
    index = 0
    for glyphName in glyphNames:
        map[tuple(font['glyf'][glyphName].flags)] = nums[index]
        index += 1
    return map

def get_new_num_map(old_map,file_path):
    new_map = {}
    font = TTFont(file_path)
    glyphNames = font.getGlyphNames()[1:]
    for glyphName in glyphNames:
        old_key = tuple(font['glyf'][glyphName].flags)
        new_key = glyphName.replace('uni','')
        new_map[new_key] = old_map[old_key]
    return new_map




cookies = {
    'sessionid': 'hnviszln1zobyixpu4aoxa3z5zrel70h',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/7',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=hnviszln1zobyixpu4aoxa3z5zrel70h; no-alert3=true; tk=-5942336745486126056',
}


init_map = init_num_map()
font_base_url = 'http://data:font/truetype;charset=utf-8;base64,'
max_num = 0
for i in range(1, 6):
    params = {
        'page': '2',
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/7', params=params, cookies=cookies, headers=headers)
    woff = response.json()['woff']

    file_name = str(i)+ '.txt'
    file_dir = os.getcwd() + '/07/'
    file_path = file_dir + file_name
    directory = os.path.dirname(file_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(woff))

    new_map = get_new_num_map(init_map, file_path)

    for item in response.json()['data']:
        current_num = ''
        for uni in item['value'].split():

            current_num = current_num + str(new_map[uni.replace('&#x','')])
        max_num = max(max_num, int(current_num))

print(max_num)