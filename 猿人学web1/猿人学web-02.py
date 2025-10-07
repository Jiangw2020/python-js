import time
from idlelib.iomenu import encoding

import requests

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

with open('猿人学web-02.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)



cookies = {
    'sessionid': 'oesmn51cj5hgfm3h5t05am10ugnbo11x',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758638713',
    'Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3': '1758638713',
    'HMACCOUNT': '4BD7E2EC1FA429CE'
}
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/2',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# sessionid=oesmn51cj5hgfm3h5t05am10ugnbo11x; qpfccr=true; no-alert3=true; tk=-5942336745486126056; Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758638713; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1758638713; HMACCOUNT=4BD7E2EC1FA429CE; m=1faa9ca6906a547da7eea49239827c1a|1758638793000
#
# sessionid=oesmn51cj5hgfm3h5t05am10ugnbo11x; qpfccr=true; no-alert3=true; tk=-5942336745486126056; Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758638713; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1758638713; HMACCOUNT=4BD7E2EC1FA429CE; m=3a1554e6e8c0ebcc32790ffbce106fee|1758638886000
total = 0

for i in range(1, 6):
    timestamp = int(time.time() * 1000)
    m = ctx.call("get_m", timestamp)
    print(f"获取到的 m 值: {m}")
    cookies['m'] =  m
    params = {
        'page': str(i),
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/2', params=params, cookies=cookies, headers=headers)
    print(response.json())
    data_list = response.json().get('data', [])
    total += sum([item.get('value', 0) for item in data_list])

print(total)
