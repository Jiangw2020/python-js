from turtledemo.clock import datum

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

begin_js = """
    window = {}
    
    setInterval = function (){}
"""
end_js = """
    function get_v14(){
        return window
    }
"""
with open('猿人学web-14.js', 'r+', encoding='utf-8') as f:
    js_code = f.read()

ctx_m = execjs.compile(js_code)

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1758551428',
    'sessionid': 'h3hf4cbh7jzgs200exaf226ghy8g60e8',
    'no-alert3': 'true',
    'yuanrenxue_cookie': '1759327574|wMsx4W5hageQqrvqBXet4Hbzc9NovUn5s4ubPVXvQ6uDlSWo0Jg9wrGMHYiAS7QLsdOA7yE89qf3Gt7P4ZqWc8Id9ia6ie1CfXsCfgUCyeSX6kFNYFstWp258LODAfD4xmpOqrWNxhKhLVReyieveC2nAG3GEqEwmZ8o3WkpLu2kQP1u',
    'mz': 'TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0MS4wLjAuMCBTYWZhcmkvNTM3LjM2LFtvYmplY3QgTmV0d29ya0luZm9ybWF0aW9uXSx0cnVlLCxbb2JqZWN0IEdlb2xvY2F0aW9uXSwyMix6aC1DTix6aC1DTix6aCwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0MS4wLjAuMCBTYWZhcmkvNTM3LjM2LEdvb2dsZSBJbmMuLCxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLFtvYmplY3QgRGVwcmVjYXRlZFN0b3JhZ2VRdW90YV0sOTUyLDAsMCwxNjAwLDI0LDEwMDAsW29iamVjdCBTY3JlZW5PcmllbnRhdGlvbl0sMjQsMTYwMCxbb2JqZWN0IERPTVN0cmluZ0xpc3RdLGZ1bmN0aW9uIGFzc2lnbigpIHsgW25hdGl2ZSBjb2RlXSB9LCxtYXRjaC55dWFucmVueHVlLmNuLG1hdGNoLnl1YW5yZW54dWUuY24saHR0cHM6Ly9tYXRjaC55dWFucmVueHVlLmNuL21hdGNoLzE0LGh0dHBzOi8vbWF0Y2gueXVhbnJlbnh1ZS5jbiwvbWF0Y2gvMTQsLGh0dHBzOixmdW5jdGlvbiByZWxvYWQoKSB7IFtuYXRpdmUgY29kZV0gfSxmdW5jdGlvbiByZXBsYWNlKCkgeyBbbmF0aXZlIGNvZGVdIH0sLGZ1bmN0aW9uIHRvU3RyaW5nKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gdmFsdWVPZigpIHsgW25hdGl2ZSBjb2RlXSB9',
    'm': '729b674870b1d8d2452eed7e8ca7e515|1759455468000|14075643744000|1',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/14',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1758551428; sessionid=h3hf4cbh7jzgs200exaf226ghy8g60e8; no-alert3=true; yuanrenxue_cookie=1759327574|wMsx4W5hageQqrvqBXet4Hbzc9NovUn5s4ubPVXvQ6uDlSWo0Jg9wrGMHYiAS7QLsdOA7yE89qf3Gt7P4ZqWc8Id9ia6ie1CfXsCfgUCyeSX6kFNYFstWp258LODAfD4xmpOqrWNxhKhLVReyieveC2nAG3GEqEwmZ8o3WkpLu2kQP1u; mz=TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0MS4wLjAuMCBTYWZhcmkvNTM3LjM2LFtvYmplY3QgTmV0d29ya0luZm9ybWF0aW9uXSx0cnVlLCxbb2JqZWN0IEdlb2xvY2F0aW9uXSwyMix6aC1DTix6aC1DTix6aCwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0MS4wLjAuMCBTYWZhcmkvNTM3LjM2LEdvb2dsZSBJbmMuLCxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLFtvYmplY3QgRGVwcmVjYXRlZFN0b3JhZ2VRdW90YV0sOTUyLDAsMCwxNjAwLDI0LDEwMDAsW29iamVjdCBTY3JlZW5PcmllbnRhdGlvbl0sMjQsMTYwMCxbb2JqZWN0IERPTVN0cmluZ0xpc3RdLGZ1bmN0aW9uIGFzc2lnbigpIHsgW25hdGl2ZSBjb2RlXSB9LCxtYXRjaC55dWFucmVueHVlLmNuLG1hdGNoLnl1YW5yZW54dWUuY24saHR0cHM6Ly9tYXRjaC55dWFucmVueHVlLmNuL21hdGNoLzE0LGh0dHBzOi8vbWF0Y2gueXVhbnJlbnh1ZS5jbiwvbWF0Y2gvMTQsLGh0dHBzOixmdW5jdGlvbiByZWxvYWQoKSB7IFtuYXRpdmUgY29kZV0gfSxmdW5jdGlvbiByZXBsYWNlKCkgeyBbbmF0aXZlIGNvZGVdIH0sLGZ1bmN0aW9uIHRvU3RyaW5nKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gdmFsdWVPZigpIHsgW25hdGl2ZSBjb2RlXSB9; m=729b674870b1d8d2452eed7e8ca7e515|1759455468000|14075643744000|1',
}

num_list = []
for i in range(1, 6):
    response = requests.get('https://match.yuanrenxue.cn/api/match/14/m', cookies=cookies, headers=headers)

    ctx_v = execjs.compile(begin_js + response.text + end_js)

    v = ctx_v.call('get_v14')
    print(v)
    m = ctx_m.call('get_m', v['v14'], v['v142'], i)
    print(m)

    cookies['m'] = m


    params = {
        'page': i
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/14', params=params, cookies=cookies, headers=headers)
    print(response.text)
    for item in response.json()['data']:
        num_list.append(item['value'])
print(sum(num_list))
