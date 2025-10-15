import httpx
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial
import urllib.parse

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

with open('04.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)


cookies = {
    'no-alert3': 'true',
    'sessionid': 'ce46b7aojp380htuj0s15s0g1n1q6uwl',
    'tk': '-12677262069270400',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://match2023.yuanrenxue.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://match2023.yuanrenxue.cn/topic/4',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'no-alert3=true; sessionid=ce46b7aojp380htuj0s15s0g1n1q6uwl; tk=-12677262069270400',
}


num_list = []
client = httpx.Client(http2=True)
for page in range(1, 6):
    params = {
        'page': str(page),
        'yt4':ctx.call('get_params')
    }
    print(params)
    response = client.post('https://match2023.yuanrenxue.cn/api/match2023/4',params=params, cookies=cookies, headers=headers)
    print(response.text)
    num_list.extend([int(item['value']) for item in response.json()['data']])
client.close()
print(sum(num_list))
