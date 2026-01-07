import tushare as ts
import pandas as pd

ts.set_token('40c70336182dc5cd2f7dfe94e11cf6635653dbae41ef1ae061f80641')
pro = ts.pro_api()
#获取今日开盘以来所有创业板实时日线和成交笔数
# df = pro.rt_k(ts_code='3*.SZ')

#获取今日开盘以来全市场所有股票实时日线和成交笔数（不建议一次提取全市场，可分批提取性能更好）
# df = pro.rt_k(ts_code='3*.SZ,6*.SH,0*.SZ,9*.BJ')
# print(df)

#获取当日开盘以来单个股票实时日线和成交笔数
df = pro.daily(ts_code='600000.SH,002938.SZ', trade_date='20260106')

df = pd.DataFrame(df)

# 方法1：转换为字典列表
list_data = df.to_dict('records')
print(list_data)
print(df)