import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
with open('申能保险超市.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

import execjs
ctx = execjs.compile(js_code)

request_data = ctx.call('get_request_data')
print(request_data)
cookies = {
    'JSESSIONID': '89A3887C3B0D05CDBE98FD58F67028C9',
    'cookiesession1': '678A3E12F0D620648C165E0EE210ABA4',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://appaw.95505.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://appaw.95505.cn/tacpc/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'key': request_data['key'],
    'keys': request_data['keys'],
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'JSESSIONID=89A3887C3B0D05CDBE98FD58F67028C9; cookiesession1=678A3E12F0D620648C165E0EE210ABA4',
}

params = {
    'jsonKey': request_data['jsonKey']
}

json_data = {
    'jsonKey': request_data['jsonKey']
}

response = requests.post(
    'https://appaw.95505.cn/tacpc/tiananapp/marketing_product_commodity/commodityList',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)
encrypt_response = response.json()['returns']['encryctReturns']
print(encrypt_response)
decrypt_response = ctx.call('get_decrypt_data',encrypt_response)
print(decrypt_response)