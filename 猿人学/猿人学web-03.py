import time
from idlelib.iomenu import encoding

import requests

import subprocess
from functools import partial

# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
#
# import execjs
#
# with open('猿人学web-02.js', 'r+', encoding='utf-8') as f:
#     js_code = f.read()
#
# ctx = execjs.compile(js_code)


import requests

cookies = {
    'sessionid': '5dpkiwi4jbwzy4xlpgckrfpbrmgfh3a9',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
    'm': 'aa6024ad7b2a0dcf10a5053db6db006a|1758808447000',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/3',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=5dpkiwi4jbwzy4xlpgckrfpbrmgfh3a9; no-alert3=true; tk=-5942336745486126056; m=aa6024ad7b2a0dcf10a5053db6db006a|1758808447000',
}

for i in range(1, 6):
    # timestamp = int(time.time() * 1000)
    # m = ctx.call("get_m", timestamp)
    # print(f"获取到的 m 值: {m}")
    # cookies['m'] =  m
    params = {
        'page': str(i),
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/3', params=params, cookies=cookies, headers=headers)
    print(response.text)

