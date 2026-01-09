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
df = pro.daily(ts_code='600000.SH,002938.SZ', trade_date='20260109')

df = pd.DataFrame(df)

# 方法1：转换为字典列表
list_data = df.to_dict('records')
print(list_data)
print(df)


# 股票列表
stocks = [
    '002115.SZ',  # 三维通信
    '002413.SZ',  # 雷科防务
    '000901.SZ',  # 航天科技
    '002046.SZ',  # 国机精工
    '600879.SH',  # 航天电子
    '001208.SZ',  # 华菱线缆
    '002324.SZ',  # 普利特
    '002465.SZ',  # 海格通信
    '002446.SZ',  # 盛路通信
    '002792.SZ',  # 通宇通讯
    '600118.SH',  # 中国卫星
    '002179.SZ',  # 中航光电
    '002935.SZ',  # 天奥电子
    '002246.SZ',  # 北化股份
    '000561.SZ',  # 烽火电子
    '002338.SZ',  # 奥普光电
]

# 将股票代码列表转换为逗号分隔的字符串
ts_codes = ','.join(stocks)

# 查询指定日期的行情数据（这里用20260106作为示例）
df = pro.daily(ts_code=ts_codes, trade_date='20260106')

# 转换为 DataFrame
df = pd.DataFrame(df)

# 选择需要显示的列
if not df.empty:
    # 按涨跌幅排序
    df_sorted = df.sort_values('pct_chg', ascending=False)

    # 显示关键信息
    print("=" * 80)
    print("股票今日行情数据（2026-01-06）")
    print("=" * 80)
    print(df_sorted[['ts_code', 'close', 'pct_chg', 'change', 'vol', 'amount']].to_string(index=False))
    print("=" * 80)

    # 统计信息
    print(f"上涨股票数量: {len(df[df['pct_chg'] > 0])}")
    print(f"下跌股票数量: {len(df[df['pct_chg'] < 0])}")
    print(f"平均涨跌幅: {df['pct_chg'].mean():.2f}%")
    print(f"最大涨幅: {df['pct_chg'].max():.2f}%")
    print(f"最大跌幅: {df['pct_chg'].min():.2f}%")

    # 转换为字典列表（如果需要）
    list_data = df.to_dict('records')
