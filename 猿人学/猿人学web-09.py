from venv import logger

import requests
import re
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

with open('猿人学web-09.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758551428',
    'sessionid': 'h3hf4cbh7jzgs200exaf226ghy8g60e8',
    'no-alert3': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://match.yuanrenxue.cn/match/9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    # 'Cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758551428; sessionid=h3hf4cbh7jzgs200exaf226ghy8g60e8; no-alert3=true; m=5cTQGEmqPqJHOyubFOOyiiK6HB82jfarnrq76aK5VFmTbtdwb83ZcyFL9Dtivhhsm0NtaCN3eJl1QuQPr7jzz26Np%2BPJypEiw1dfC6F0MeWPOlzvEkFiPdlJcAOpU7V2kLVRSmhtoY%2FMMcOa%2FdfjnlEWgk0RA9O2vj2Yuq30pBNyj3msha7wSITVuDwa62zgK4su3%2BHLCAdNnF8AzuouJRBQg7ZwrqAiFqTGgc8FCTBwxp8xyQGuqjIpmD2ergEpJQPRb0ZiJzdFGCYvjhsA29mgDmHRXNMjxTrNpCzNXhHZ%2FdwR5a5hsAAVKb4TME17OhnR3TnAYeGjlvVdEStANkA%3D%3Dr',
}

response = requests.get('https://match.yuanrenxue.cn/match/9', cookies=cookies, headers=headers)

time = re.findall(r"\(m,(\d+)\)", response.text)[0]
data = re.findall(r"\(decrypt,'(\w+)'\)", response.text)[0]
print(time)
print(data)

m = ctx.call('get_m', int(time), str(data))
print(m)
cookies['m'] = m

num_list = []
for i in range(1,6):
    params = {
        'page': i,
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/9', params=params, cookies=cookies, headers=headers)
    print(response.json())
    num_list.extend(int(item['value']) for item in response.json()['data'])


total = 0
for num in num_list:
    total += num
print(total/len(num_list))
