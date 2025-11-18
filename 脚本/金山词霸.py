import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

with open('金山词霸.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

content = '执炬迎风'
content = 'Hold the torch and welcome the wind'

sign =  ctx.call('get_sign', content)
url = "https://ifanyi.iciba.com/index.php?c=trans&m=fyV2&client=6&auth_user=key_web_new_fanyi&sign=" + sign

payload = {
    "from": "auto",
    "to": "auto",
    "q": content
}
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https",
    "Pragma": "no-cache",
    "Referer": "https",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}

response = requests.post(url, data=payload, headers=headers)
print(response.json())

data = ctx.call('decrypt_data', response.json()['content'])
print(data)