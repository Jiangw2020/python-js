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

with open('02.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)


cookies = {
    'no-alert3': 'true',
    'tk': '-2572785031734475209',
    'sessionid': 'b59bueipn0yer6tdnsea4ju2bip0py1j',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'origin': 'https://match2023.yuanrenxue.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://match2023.yuanrenxue.cn/topic/2',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    # 'cookie': 'no-alert3=true; tk=-2572785031734475209; sessionid=b59bueipn0yer6tdnsea4ju2bip0py1j',
}


num_list = []
client = httpx.Client(http2=True)
for page in range(1, 6):
    data = ctx.call('get_data',page)
    print(data)
    # 使用urlencode函数将字典转换为URL编码的查询字符串
    query_string = urllib.parse.urlencode(data)
    print(query_string)
    response = client.post('https://match2023.yuanrenxue.cn/api/match2023/2?'+query_string, cookies=cookies, headers=headers)
    print(response.text)
    num_list.extend([int(item['value']) for item in response.json()['data']])
client.close()
print(sum(num_list))
