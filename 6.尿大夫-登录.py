import hashlib

import requests
import time

headers = {
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded',
}

t = int(time.time())


def md5(data_string):
    obj = hashlib.md5()
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


def get_sign():
    v1 = md5(f"niaodaifu{t}")[12:30]
    v2 = md5(f"android{t}")[12:26]
    sign = v1 + v2
    return sign


sign = get_sign()
print(sign)
data = {
    'devisetoken': '170976fa8bbc7c13dd4',
    'password': 'lqz12345',
    'mobile': '18953675221',
    'channel': 'android',
    'sign': sign,
    'time': t,
    'mechanism': '0',
    'platform': '1',
}

response = requests.post('https://api.niaodaifu.cn/v4/site/loginnew', headers=headers, data=data)
print(response.json())
