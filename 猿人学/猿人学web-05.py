import time

import requests

import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

with open('猿人学web-05.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

cookies = {
    'sessionid': 'np2rfrnv74j2g0j8ztu14k30in5emmn6',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
    'm': 'faf539055b0de877d35b30c35f3526fd',
    'RM4hZBv0dDon443M': 'Zz/8D6oL+LBCRtPrqC1I6lYJ3wZICwyVhB2ihxCnx53zvF44+fvP6O/V67HW/QHTgHeUD79ymDQNt3wVLW+kV+7WUD3+Vu5zSRc0QRsNYzLo8QJTBxGh30dUOetjU3z3mZ+h30X/47pCnodHSoS+t/Xdf5i0fdcITSsr4XSGdDABMfz9b/irqbxyD8w+uLjNzVAUAqbPKLxrbjjNjvO4mORaXA1qZm9geCinTYxIOHI='
}

headers = {
    'sec-ch-ua-platform': '"Windows"',
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.cn/match/5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
}
hot = []
for i in range(1, 6):

    params = {
        'page': str(i),
        'f': int(time.time() * 1000),
    }

    data = ctx.call('get_m')
    cookies['RM4hZBv0dDon443M'] = data['RM4hZBv0dDon443M']
    cookies['m'] = data['m']
    params['m'] = data['param_m']

    response = requests.get('https://match.yuanrenxue.cn/api/match/5', params=params, cookies=cookies, headers=headers,verify= False)
    hot.extend([int(item['value']) for item in response.json()['data']])

hot.sort()
hot.reverse()
sum = 0
for item in hot[:5]:
    print(item)
    sum += item
print(sum)
