import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)


import os
import requests
import base64
from fontTools.ttLib import TTFont
def init_num_map():
    map = {}
    font = TTFont('./07/0.txt')
    glyphNames =font.getGlyphNames()[1:]
    # https: // wakamaifondue.com / 获取数字映射数据
    nums = [1,2,4,0,7,9,8,3,5,6]
    index = 0
    for glyphName in glyphNames:
        map[tuple(font['glyf'][glyphName].flags)] = nums[index]
        index += 1
    return map

def get_new_num_map(old_map,file_path):
    new_map = {}
    font = TTFont(file_path)
    glyphNames = font.getGlyphNames()[1:]
    for glyphName in glyphNames:
        old_key = tuple(font['glyf'][glyphName].flags)
        new_key = glyphName.replace('uni','')
        new_map[new_key] = old_map[old_key]
    return new_map




cookies = {
    'sessionid': 'hnviszln1zobyixpu4aoxa3z5zrel70h',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/7',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=hnviszln1zobyixpu4aoxa3z5zrel70h; no-alert3=true; tk=-5942336745486126056',
}


init_map = init_num_map()
font_base_url = 'http://data:font/truetype;charset=utf-8;base64,'
max_num = 0
max_num_index = 0
name_index = 0
for i in range(1, 6):
    params = {
        'page': i,
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/7', params=params, cookies=cookies, headers=headers)
    woff = response.json()['woff']

    file_name = str(i)+ '.txt'
    file_dir = os.getcwd() + '/07/'
    file_path = file_dir + file_name
    directory = os.path.dirname(file_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(woff))

    new_map = get_new_num_map(init_map, file_path)
    index = 1
    for item in response.json()['data']:
        name_index = 10* (i-1) + index
        index += 1
        current_num = ''
        for uni in item['value'].split():
            current_num = current_num + str(new_map[uni.replace('&#x','')])
        max_num = max(max_num, int(current_num))
        if max_num == int(current_num):
            max_num_index = name_index
names = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];
print(max_num)
print(max_num_index)
print(names[max_num_index])