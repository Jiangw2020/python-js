from idlelib.iomenu import encoding

import requests

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

cookies = {
    'sessionid': '9jubjt1skh3luocwn53w4et6ra0mtj0g',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/1',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': 'sessionid=9jubjt1skh3luocwn53w4et6ra0mtj0g; qpfccr=true; no-alert3=true; tk=-5942336745486126056',
}

with open('猿人学web-01.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

params = {

}
total = 0
count = 0
avg = 0
for i in range(1, 6):
    params['page'] = i
    params['m'] = ctx.call('get_m')
    response = requests.get('https://match.yuanrenxue.cn/api/match/1', params=params, cookies=cookies, headers=headers)
    print(response.json())
    data_list = response.json().get('data', [])
    count += len(data_list)
    total += sum([item.get('value', 0) for item in data_list])

if count > 0:
    avg = total / count
print(avg)
