from PIL import Image
import easyocr
import pytesseract

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
        # pixel = img.getpixel((x, 1))
        # first_row_pixels.append(pixel)
        # pixel = img.getpixel((x, 51))
        # first_row_pixels.append(pixel)
        # pixel = img.getpixel((x, 101))
        # first_row_pixels.append(pixel)

        pixel = img.getpixel((10, x))
        first_row_pixels.append(pixel)
        pixel = img.getpixel((60, x))
        first_row_pixels.append(pixel)
        pixel = img.getpixel((110, x))
        first_row_pixels.append(pixel)
    # 将第一行像素转换为集合以提高查找效率
    first_row_set = set(first_row_pixels)

    print(f"图片尺寸: {width} x {height}")
    print(f"第一行唯一像素数量: {len(first_row_set)}")

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
    print(f"处理完成，结果保存到: {output_path}")
    # # 使用 Tesseract OCR 识别文本
    # text = pytesseract.image_to_string(new_img, lang='chi_sim')
    #
    # return text.strip()



# 使用示例
replace_matching_pixels('./08/output.png', './08/output_enhance.jpg')

reader = easyocr.Reader(['ch_sim'])
data = reader.readtext('./08/output_enhance.jpg')
print(data)