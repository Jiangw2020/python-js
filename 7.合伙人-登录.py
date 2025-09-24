import hashlib

import requests
import time
from urllib.parse import urlencode

reqTime = time.time()
noncestr = '123456'


def md5(data_string):
    obj = hashlib.md5()
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


password = md5("sdhhdhdhjj")
data = {
    'phone': '15876421245',
    'password': password,
}

sb = urlencode(data)

print("sb:" + sb)


def get_sign():
    return md5(str(reqTime) + noncestr[2:] + sb).lower()


sign = get_sign()
print("sign:" + sign)

headers = {
    'User-Agent': 'okhttp/3.10.0',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-App': 'native',
    'X-Noncestr': noncestr,
    'X-OS': 'partnerApp_android',
    'X-Req-Time': str(reqTime),
    'X-Sign': sign,
}

response = requests.post('https://chinayltx.com/app/api/v1/partnerLogin/login', headers=headers, data=data)
print(response.json())
