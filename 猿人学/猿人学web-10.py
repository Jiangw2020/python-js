import requests

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758551428',
    'sessionid': 'h3hf4cbh7jzgs200exaf226ghy8g60e8',
    'no-alert3': 'true',
    'm': 'pua',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/10',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758551428; sessionid=h3hf4cbh7jzgs200exaf226ghy8g60e8; no-alert3=true; m=pua',
}

params = {
    'page': '3',
    'm': '4UrkgIwjsrchfAKOC2qRltb4jx0ieHyhXvZItorSg8hL5lGtjcIt_woJEPyvWewABEIiJjuvPYIOUv86BABZmAn1OFJusdCOQ0deL6JHdFJusd5TSNQXJp3AlDeABroMWMo.qDPgCQvvv56CejnIu..YtJ03wPxr0BLuxeVwmkXtXIs6PXahaCjr2ulEJUyZZ.OvR1HojKbF2rlFiy7ZrAvBFdnnVX2o8x.7El8zJ5fSTpv4MjZBOHRQ6hhbR6u2_0MTJerAx23VOYKBmTumJeHtk',
}

response = requests.get('https://match.yuanrenxue.cn/api/match/10', params=params, cookies=cookies, headers=headers)
print(response.text)