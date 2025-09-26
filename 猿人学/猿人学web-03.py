
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)

from collections import Counter



def parse_cookie(cookie_str):
    """解析cookie字符串为字典"""
    parts = cookie_str.split(';')
    cookie_dict = {}

    for part in parts:
        part = part.strip()
        if '=' in part:
            key, value = part.split('=', 1)
            cookie_dict[key] = value
        else:
            # 处理没有值的属性（如HttpOnly）
            cookie_dict[part] = True

    return cookie_dict


headers = {
    'content-length': '0',
    'sec-ch-ua-platform': '"Windows"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'accept': '*/*',
    'origin': 'https://match.yuanrenxue.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.cn/match/3',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'Cookie': 'm=85c3a103a042f2da0b003fac9b8cf29e|1758898514000; sessionid=g2hqbpd5sx2l3z9ei7fww49in2komemy; qpfccr=true; no-alert3=true; tk=-5942336745486126056',
}
session = requests.session()
session.headers = headers

nums = []
for i in range(1, 6):
    params = {
        'page': str(i),
    }
    jssm_response = session.post('https://match.yuanrenxue.cn/jssm', verify=False)
    cookies = parse_cookie(jssm_response.headers['Set-Cookie'])

    response = session.get('https://match.yuanrenxue.cn/api/match/3', params=params, cookies=cookies)
    # 提取数字,并添加到列表中
    numbers = [int(item['value']) for item in response.json()['data']]
    nums.extend(numbers)

# 统计出现次数最多的数字
counter = Counter(nums)
most_common = counter.most_common(1)
print(most_common[0][0])

