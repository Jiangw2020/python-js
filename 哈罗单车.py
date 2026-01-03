import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import time
from datetime import datetime, time as dt_time, timedelta

# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)

# 公共常量定义
BASE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.148 MYWeb/0.11.0.250416151924 UWS/3.22.2.9999 UCBS/3.22.2.9999_220000000000 Mobile Safari/537.36 NebulaSDK/1.8.100112 Nebula AlipayDefined(nt:WIFI,ws:411|0|2.625) AliApp(AP/10.7.28.8000) AlipayClient/10.7.28.8000 Language/zh-Hans useStatusBar/true isConcaveScreen/true Region/CNAriver/1.0.0 MiniProgram APXWebView',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/json',
    'Origin': 'https://m.hellobike.com',
    'X-Requested-With': 'com.eg.android.AlipayGphone',
    'Referer': 'https://m.hellobike.com/',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'x-mass-tappid': '2017050407110255',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

COMMON_DATA = {
    "businessId": "5",
    "token": "9cdaa3eb7ca244499f41a21a6a671b6f",
    "cityCode": "021",
    "adCode": "310115"
}


# 第一个请求：获取活动列表
def first_request():
    url = 'https://marketingapi.hellobike.com/api?shopaholic.zone.activityList'

    headers = BASE_HEADERS.copy()
    headers['requestId'] = '5fkJDvWOCEtXQ0s'  # 第一个请求专用requestId

    data = {
        **COMMON_DATA,
        "action": "shopaholic.zone.activityList",
        "sceneKey": "citySecKill",
        "futureTimestamp": 1758470399775,
        "date": 1758382373775,
        "takeItByCity": True
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print("第一个请求响应:" + response.text)
    return response


# 第二个请求：获取SKU列表
def second_request(activity_code):
    url = 'https://marketingapi.hellobike.com/api?shopaholic.activity.skuList'

    headers = BASE_HEADERS.copy()
    headers['requestId'] = '5fkJDBrbIS0Gk5L'  # 第二个请求专用requestId

    data = {
        **COMMON_DATA,
        "action": "shopaholic.activity.skuList",
        "activityCode": activity_code,
        "port": "2"
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print("\n第二个请求响应:")
    print(response.text)
    return response


# 第三个请求：提交秒杀订单
def third_request(activity_code, sku_id=None, item_id=None, sale_price=None):
    url = 'https://marketingapi.hellobike.com/api?mall.goods.kill'

    headers = BASE_HEADERS.copy()
    headers['requestId'] = '5fj9xJUFnSxwxqr'  # 第三个请求专用requestId

    data = {
        **COMMON_DATA,
        "action": "mall.goods.kill",
        "activityCode": activity_code,
        "longitude": 121.588237,
        "latitude": 31.296032,
        "payAmount": sale_price,
        "skuId": sku_id,  # 支持动态传入SKU ID
        "systemCode": "65",
        "salePrice": sale_price,
        "purchaseNum": 1,
        "version": "6.41.0",
        "orderPort": "2",
        "itemId": item_id,
        "needQueryUnPayOrder": 1,
        "ext": {
            "adSource": "syjgw",
            "adsource": "syjgw"
        }
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print("=" * 50)
    print("第三个请求响应:")
    print(response.text)
    return response


# 等待到指定的时间
def wait_until_target_time(target_time):
    now = datetime.now()
    target = datetime.combine(now.date(), target_time)

    # 如果目标时间已经过去，则等到明天的同一时间
    if now.time() > target_time:
        target += timedelta(days=1)

    wait_seconds = (target - now).total_seconds()
    print(f"等待 {wait_seconds:.2f} 秒直到 {target_time}...")
    time.sleep(wait_seconds)
    print(f"到达目标时间 {target_time}，开始执行请求")


# 执行高频请求
def execute_high_frequency_requests(activity_code, sku_id=None, item_id=None, sale_price=None):
    total_requests = 200  # 减少请求数量，避免被封禁
    interval = 0.01  # 增加间隔时间

    print(f"开始执行 {total_requests} 次请求，间隔 {interval}  毫秒")

    for i in range(total_requests):
        response = third_request(activity_code, sku_id, item_id, sale_price)
        print(f"\n已完成 {i + 1}/{total_requests} 次请求")

        # 检查是否秒杀成功
        try:
            if response.json().get("code") == 0:
                print("秒杀成功！")
                break
        except:
            pass

        if i < total_requests - 1:  # 最后一次请求不等待
            time.sleep(interval)


# 执行两个请求
if __name__ == "__main__":
    # 执行第一个请求
    first_response = first_request()

    activity_code = None  # 默认值
    start_time = None

    # 解析第一个响应，提取activityCode
    if first_response.json().get("code") == 0:
        try:
            response_data = first_response.json()
            # 假设响应结构为{"data": {"list": [{"activityCode": "..."}]}}
            activity_rules = response_data.get('data', [])[0].get('activityRules', [])
            for rule in activity_rules:

                effective_start_time = datetime.strptime(rule.get('effectiveStartTime'), "%Y-%m-%d %H:%M:%S")

                # 获取当前时间
                current_time = datetime.now()

                # 比较时间
                if effective_start_time > current_time:
                    activity_code = rule.get('activityCode')
                    start_time = effective_start_time - timedelta(microseconds=1000)
                    print(f"从响应中提取到activityCode: {activity_code}")
                    break
        except Exception as e:
            print(f"解析第一个响应失败: {e}")
    else:
        print("第一个请求失败")

    second_response = second_request(activity_code)
    sku_id = None
    item_id = None
    sale_price = None

    # 尝试从第二个响应中提取skuId
    if second_response.json().get("code") == 0:
        try:
            response_data = second_response.json()
            sku_list = response_data.get('data', [])
            # 遍历SKU列表，查找符合条件的SKU
            target_sku_name = "不限次卡"
            target_sale_price = [0.01,0.99,1.99]
            for sku in sku_list:
                if target_sku_name in sku.get('skuName') and target_sale_price.index(sku.get('salePrice')) != -1:
                    sku_id = sku.get('skuId')
                    item_id = sku.get('itemId')
                    sale_price = sku.get('salePrice')
                    print(f"找到目标SKU: {sku_id} (名称: {sku.get('skuName')}, 价格: {sale_price}, ItemId: {item_id})")
                    break

            if not sku_id:
                print(f"未找到名称为'{target_sku_name}'且价格为{target_sale_price}的SKU")
        except Exception as e:
            print(f"解析第二个响应失败: {e}")
    else:
        print("第二个请求失败或返回错误状态码")

    # third_request('7341321042502161094017679425', '7269025983949836018017638651', '101_17554', 0.01)
    # 设置目标时间为 00:00:00
    target_time = dt_time(16, 59, 59, 999000)

    # target_time = datetime.time(0, 0, 0)
    wait_until_target_time(start_time.time())

    execute_high_frequency_requests(activity_code, sku_id, item_id, sale_price)
