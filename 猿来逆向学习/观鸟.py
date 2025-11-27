from encodings.utf_16 import decode

import requests
import urllib3
from fontTools.misc.eexec import decrypt
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
with open('观鸟.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

import execjs
ctx = execjs.compile(js_code)

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.birdreport.cn',
    'Referer': 'https://www.birdreport.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'requestId': '8661d43bd682ad479cd9be0d0ace4d59',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': '2b9d0327691f0fbacb0afd1fd417d971',
    'timestamp': '1762577163000',
}

encrypt_data = ctx.call('get_encrypt_data', 'page=1&limit=20')
print(encrypt_data)
data = encrypt_data['data']
headers['sign'] = encrypt_data['sign']
headers['timestamp'] = str(encrypt_data['timestamp'])
headers['requestId'] = encrypt_data['requestId']
response = requests.post('https://api.birdreport.cn/front/activity/search', headers=headers, data=data)
decrypt_data = ctx.call('decrypt_data', response.json()['data'])
print(decrypt_data)
