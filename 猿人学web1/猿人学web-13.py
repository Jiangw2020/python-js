import requests
import re

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758551428',
    'sessionid': 'h3hf4cbh7jzgs200exaf226ghy8g60e8',
    'no-alert3': 'true',
    'm': '155',
    'yuanrenxue_cookie': '1759324912|0QEeWNp7jKXppM10hDcXqigxBp0VqvcRWUwX2cLT7j0iC0W8',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://match.yuanrenxue.cn/match/13',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    # 'Cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758551428; sessionid=h3hf4cbh7jzgs200exaf226ghy8g60e8; no-alert3=true; m=155; yuanrenxue_cookie=1759324912|0QEeWNp7jKXppM10hDcXqigxBp0VqvcRWUwX2cLT7j0iC0W8',
}

def get_result ():
    response = requests.get('https://match.yuanrenxue.cn/match/13', cookies=cookies, headers=headers)
    print(response.text)

    pattern = r"'([1-9a-zA-Z=+/|_])'"
    match = re.findall(pattern, response.text)
    document_cookie = ''.join(match)

    cookies['yuanrenxue_cookie'] = document_cookie[18:]
    print(cookies['yuanrenxue_cookie'])

    num_list = []
    total_sum = 0
    for page in range(1, 6):
        params = {
            'page': page,
        }

        response = requests.get('https://match.yuanrenxue.cn/api/match/13', params=params, cookies=cookies,
                                headers=headers)
        print(response.json())
        num_list.extend(int(item['value']) for item in response.json()['data'])

    # yuanrenxue_cookie不是每次都能用，所以递归调用，直到 total_sum 不为 0
    total_sum += sum(num_list)
    if total_sum == 0:
        return get_result()
    return total_sum

print(get_result())
