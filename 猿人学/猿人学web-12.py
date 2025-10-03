import requests
import base64

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758551428',
    'sessionid': 'h3hf4cbh7jzgs200exaf226ghy8g60e8',
    'no-alert3': 'true',
    'm': '155',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/12',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758551428; sessionid=h3hf4cbh7jzgs200exaf226ghy8g60e8; no-alert3=true; m=155',
}

params = {
    'page': '2',
    'm': 'eXVhbnJlbnh1ZTI=',
}

total_sum = 0
for page in range(1, 6):
    params['page'] = str(page)
    params['m'] = base64.b64encode(('yuanrenxue' + str(page)).encode())

    response = requests.get('https://match.yuanrenxue.cn/api/match/12', params=params, cookies=cookies, headers=headers)
    print(response.json())
    total_sum += sum(int(item['value']) for item in response.json()['data'])
print(total_sum)