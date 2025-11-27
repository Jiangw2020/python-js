import httpx
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

with open('01.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758263295',
    'HMACCOUNT': '7F77C2B6C739E12F',
    'Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3': '1758270572',
    'no-alert3': 'true',
    'tk': '244997616161430321',
    'sessionid': '3l6sf9pmmqwoforwfoaw3zcz5aownftm',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://match2023.yuanrenxue.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://match2023.yuanrenxue.cn/topic/1',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758263295; HMACCOUNT=7F77C2B6C739E12F; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1758270572; no-alert3=true; tk=244997616161430321; sessionid=3l6sf9pmmqwoforwfoaw3zcz5aownftm',
}

num_list = []
client = httpx.Client(http2=True)
for page in range(1, 6):
    data = ctx.call('get_data',page)
    print(data)
    response = client.post('https://match2023.yuanrenxue.cn/api/match2023/1', data=data, cookies=cookies, headers=headers)
    print(response.text)
    num_list.extend([int(item['value']) for item in response.json()['data']])
client.close()
print(sum(num_list))
