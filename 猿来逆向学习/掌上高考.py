import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.gaokao.cn',
    'priority': 'u=1, i',
    'referer': 'https://www.gaokao.cn/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

json_data = {
    'autosign': '',
    'like_spname': '',
    'local_batch_id': '14',
    'local_province_id': '31',
    'local_type_id': '3',
    'page': 1,
    'platform': '2',
    'school_id': '263',
    'sg_xuanke': '',
    'signsafe': '3ca2e0500bac008794f57ead368415d5',
    'size': 5,
    'special_group': '',
    'uri': 'v1/school/special_plan',
    'year': '2025',
}

response = requests.post(
    'https://api-gaokao.zjzw.cn/apidata/web?autosign=&like_spname=&local_batch_id=14&local_province_id=31&local_type_id=3&page=1&platform=2&school_id=263&sg_xuanke=&size=5&special_group=&uri=v1/school/special_plan&year=2025&signsafe=3ca2e0500bac008794f57ead368415d5',
    headers=headers,
    json=json_data,
)

print(response.text)