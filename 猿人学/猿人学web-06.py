import time

import requests

import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import requests

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

params = {
    'page': '3',
    'm': 'ntWN3Fnq4Gs5MJ1flodtfFvS5ULHNk3D%2BrFa0SgfEGR2rZ3TaBVcLG9%2BK%2BGp15cn8clu2YxXwOM4Q5mX0UbN9a23OkNr98Nj%2FJhh3htPv%2FXMZnuKuAQ10pZXrYqWPVTP6%2BigqKV6J3O5Tvw0Pb2pTKA%2BovVvFBb4HmtuifnGb8g%3D',
    'q': '1-1758979518000|2-1758979590000|3-1758979649000|4-1758979717000|5-1758979734000|',
}

response = requests.get('https://match.yuanrenxue.cn/api/match/6', params=params, cookies=cookies, headers=headers)
print(response.json())
