import requests
from bs4 import BeautifulSoup

cookies = {
    'PHPSESSID': 'vv4thl19ilreqgdsm9uurm66o3',
    'Hm_lvt_52a07b6d5fe6c3d55a2a938c7c0ae78b': '1766372254',
    'HMACCOUNT': '7F77C2B6C739E12F',
    'Hm_lpvt_52a07b6d5fe6c3d55a2a938c7c0ae78b': '1766651376',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.iccgame.com/login/process',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'PHPSESSID=vv4thl19ilreqgdsm9uurm66o3; Hm_lvt_52a07b6d5fe6c3d55a2a938c7c0ae78b=1766372254; HMACCOUNT=7F77C2B6C739E12F; Hm_lpvt_52a07b6d5fe6c3d55a2a938c7c0ae78b=1766651376',
}

response = requests.get('https://passport.iccgame.com/login', cookies=cookies, headers=headers)
print(response.text)
# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(response.text, 'lxml')
# 也可以使用 'html.parser'

# 查找name为'token'的input标签
token_input = soup.find('input', {'name': 'token'})

# 获取该input标签的value属性
if token_input:
    token_value = token_input.get('value')
    print("Token value:", token_value)
else:
    print("Token input not found.")

cookies = {
    'PHPSESSID': 'vv4thl19ilreqgdsm9uurm66o3',
    'Hm_lvt_52a07b6d5fe6c3d55a2a938c7c0ae78b': '1766372254',
    'HMACCOUNT': '7F77C2B6C739E12F',
    'Hm_lpvt_52a07b6d5fe6c3d55a2a938c7c0ae78b': '1766651376',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://passport.iccgame.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.iccgame.com/login',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'PHPSESSID=vv4thl19ilreqgdsm9uurm66o3; Hm_lvt_52a07b6d5fe6c3d55a2a938c7c0ae78b=1766372254; HMACCOUNT=7F77C2B6C739E12F; Hm_lpvt_52a07b6d5fe6c3d55a2a938c7c0ae78b=1766651376',
}

data = {
    'returnUrl': '',
    'gameid': '400',
    'accountname': '245',
    'password': '1c383cd30b7c298ab50293adfecb7b18',
    'tncode_num': '79',
    'is_check_code': '1',
    'x': '109',
    'y': '16',
    'token': '77545996b115c6ecf12ebeb6a28b7394b11d670abf05e0f238b57cc021a0f44e',
    't': '0a5bd4150674ea31c5183ca93ed1d99717666513757677220',
}
# 图片验证码不知道怎么过，
# 参数t:加密逻辑，标准md5算法
# var _$ = ["\x59\x41\x51\x47\x4d\x4b\x4c\x4c\x4e\x45\x38\x37\x47", "", "\x69\x6e\x70\x75\x74", '\x68\x69\x64\x64\x65\x6e', '\x74', "\x64\x61\x6e\x63\x65\x72\x6c\x6f\x67\x69\x6e"];
# var O5e = _$[0];
# var O68 = navigator["\x75\x73\x65\x72\x41\x67\x65\x6e\x74"]["\x74\x6f\x4c\x6f\x77\x65\x72\x43\x61\x73\x65"]();
# if (O68 != _$[1]) {
#     O68 = O5e
# }
# ;var O6c = new Date();
# var c1e = O6c["\x67\x65\x74\x54\x69\x6d\x65"]() * 0x2710 + Math["\x72\x6f\x75\x6e\x64"](Math["\x72\x61\x6e\x64\x6f\x6d"]() * 0x2710);
# var O3a = this["\x6d\x64\x35"](O68 + c1e) + c1e;
# var O66 = window["\x64\x6f\x63\x75\x6d\x65\x6e\x74"]["\x63\x72\x65\x61\x74\x65\x45\x6c\x65\x6d\x65\x6e\x74"](_$[2]);
# O66["\x76\x61\x6c\x75\x65"] = O3a;
# O66["\x74\x79\x70\x65"] = _$[3];
# O66["\x6e\x61\x6d\x65"] = _$[4];
# window["\x64\x6f\x63\x75\x6d\x65\x6e\x74"]["\x67\x65\x74\x45\x6c\x65\x6d\x65\x6e\x74\x42\x79\x49\x64"](_$[5])["\x61\x70\x70\x65\x6e\x64\x43\x68\x69\x6c\x64"](O66);

response = requests.post('https://passport.iccgame.com/login/process', cookies=cookies, headers=headers, data=data)
print(response.text)