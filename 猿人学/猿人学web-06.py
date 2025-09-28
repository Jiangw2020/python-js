import requests
import time
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
with open('猿人学web-06.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

import execjs
ctx = execjs.compile(js_code)


cookies = {
    'sessionid': 'h5uf8e8ctvjh2olq85t46npz7y9auurg',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/6',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=h5uf8e8ctvjh2olq85t46npz7y9auurg; qpfccr=true; no-alert3=true; tk=-5942336745486126056',
}
total = 0
for i in range(1, 6):
    time_tamp = int(time.time() * 1000)
    m = ctx.call('r',time_tamp,i)
    params = {
        'page': i,
        'q': str(i)+"-"+str(time_tamp)+"|",
        'm':m
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/6', params=params, cookies=cookies, headers=headers)
    print(response.json())
    for item in response.json()['data']:
        total += int(item['value'])

print(total * 24)
