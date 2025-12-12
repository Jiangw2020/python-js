import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
with open('火龙果.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

import execjs
ctx = execjs.compile(js_code)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Authorization': '',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DeviceInfo': '{"version":"4.12.1","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36","os":"web","macAddress":"","ppt_fp_id":"32da50a4-7121-4355-9fce-f4a1562a46b4"}',
    'Language': 'zh',
    'Origin': 'https://web.mypitaya.com',
    'Pragma': 'no-cache',
    'Referer': 'https://web.mypitaya.com/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://api.mypitaya.com/api/serverkey', headers=headers)
print(response.text)


# json_data = {
#     'sign': '0b5ca82a7400b1485a3eb37da31fc06c',
#     'salt': '007cb748-ff2d-40a5-884a-ff086c26a4be',
#     'time': 1765520105,
#     'md5': '31643fa824c68710c9f5b6a321a30ec7',
#     'phone': '+8615871112345',
# }
phone = '+8615871112345'
print(phone)
server_key = response.text.replace('"', '')
print(server_key)
json_data = ctx.call('get_sign', phone, server_key)
print(json_data)
json_data['phone'] = phone
response = requests.post('https://api.mypitaya.com/api/sendSMS/v3', headers=headers, json=json_data)
print(response.text)
