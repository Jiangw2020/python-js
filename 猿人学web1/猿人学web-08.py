
from PIL import Image
import easyocr
from bs4 import BeautifulSoup
import base64
from collections import Counter


def replace_matching_pixels(image_path, output_path):
    """
    遍历图片每个像素，如果与第一行任意像素相同，则设置为白色

    参数:
        image_path: 输入图片路径
        output_path: 输出图片路径
    """
    # 打开图片并转换为RGB模式
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    # 获取第一行所有像素
    first_row_pixels = []
    for x in range(width):
        pixel = img.getpixel((x, 1))
        first_row_pixels.append(pixel)
        # pixel = img.getpixel((x, 51))
        # first_row_pixels.append(pixel)
        # pixel = img.getpixel((x, 101))
        # first_row_pixels.append(pixel)
        #
        # pixel = img.getpixel((10, x))
        # first_row_pixels.append(pixel)
        # pixel = img.getpixel((60, x))
        # first_row_pixels.append(pixel)
        # pixel = img.getpixel((110, x))
        # first_row_pixels.append(pixel)
    # 将第一行像素转换为集合以提高查找效率
    first_row_set = set(first_row_pixels)

    # print(f"图片尺寸: {width} x {height}")
    # print(f"第一行唯一像素数量: {len(first_row_set)}")

    # 创建新图片用于修改（避免修改原图）
    new_img = img.copy()

    # 遍历每个像素
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # 如果当前像素在第一行像素集合中，则设置为白色
            if pixel in first_row_set:
                new_img.putpixel((x, y), (255, 255, 255))
            else:
                new_img.putpixel((x, y), (0,0,0))

    # 保存结果
    new_img.save(output_path)
    # print(f"处理完成，结果保存到: {output_path}")
    # # 使用 Tesseract OCR 识别文本
    # text = pytesseract.image_to_string(new_img, lang='chi_sim')
    #
    # return text.strip()


# 使用示例
# reader = easyocr.Reader(['ch_sim'])
# data = reader.readtext('./08/output_enhance.jpg')
# print(data)


import requests

cookies = {
    'sessionid': 'hnviszln1zobyixpu4aoxa3z5zrel70h',
    'no-alert3': 'true',
    'tk': '-5942336745486126056',
    'm': '91c8c980ef5f33e8d489299b93ea02df|1759128949000',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/8',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=hnviszln1zobyixpu4aoxa3z5zrel70h; no-alert3=true; tk=-5942336745486126056; m=91c8c980ef5f33e8d489299b93ea02df|1759128949000',
}

num_list = []
for i in range(1,6):
    params = {
        'page': str(i),
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/8', params=params, cookies=cookies, headers=headers)
    if  response.status_code == 400:
        verify_response = requests.get('https://match.yuanrenxue.cn/api/match/8_verify', cookies=cookies, headers=headers)
        soup = BeautifulSoup(verify_response.json()['html'], 'html.parser')

        p_tags = soup.find_all('p')
        keys = ''
        for p in p_tags:
            keys += p.text + ' '
        print(keys)
        img = soup.find('img')
        img_base64 = img.get('src', '')
        img_base64 = img_base64.replace('data:image/jpeg;base64,','')

        file_path = './08/' + str(i) + '.jpg'

        with open(file_path, 'wb') as f:
            f.write(base64.b64decode(img_base64))

        enhance_file_path = './08/' + str(i) + '_enhance.jpg'
        replace_matching_pixels(file_path, enhance_file_path)

        user_input = input("请输入一些四位验证码（1-9）: ")

        answer = ''
        for i in range(0,4):
            nums = str(user_input)
            num = int(nums[i])
            if num == 1:
                answer = answer + "155|"
            if num == 2:
                answer = answer + "165|"
            if num == 3:
                answer = answer + "175|"
            if num == 4:
                answer = answer + "455|"
            if num == 5:
                answer = answer + "465|"
            if num == 6:
                answer = answer + "475|"
            if num == 7:
                answer = answer + "755|"
            if num == 8:
                answer = answer + "765|"
            if num == 9:
                answer = answer + "775|"

        params['answer'] = answer
        print(answer)
        response = requests.get('https://match.yuanrenxue.cn/api/match/8', params=params, cookies=cookies,headers=headers)
        print(response.json())
        if response.status_code == 200:
            num_list.extend([int(item['value']) for item in response.json()['data']])

# 统计出现次数最多的数字
counter = Counter(num_list)
most_common = counter.most_common(1)
print(most_common[0][0])
