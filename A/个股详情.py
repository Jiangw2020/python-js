import akshare as ak
import pandas as pd
from datetime import datetime, timedelta

def get_daily_info(symbol, name, start_date = datetime.now(), end_date = datetime.now()):
    final_time = end_date.replace(hour=15, minute=00, second=0, microsecond=0)
    yesterday_start_date = end_date - timedelta(days=1)
    yesterday_end_date = end_date - timedelta(days=1)
    start_date = start_date.replace(hour=9, minute=30, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
    end_date = final_time.strftime('%Y-%m-%d %H:%M:%S')
    yesterday_start_date = yesterday_start_date.replace(hour=9, minute=30, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
    yesterday_end_date = yesterday_end_date.replace(hour=15, minute=00, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')

    stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol=symbol, period="1", start_date=start_date, end_date=end_date, adjust='hfq')
    yesterday_stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol=symbol, period="1", start_date=yesterday_start_date, end_date=yesterday_end_date, adjust='hfq')

    df = pd.DataFrame(stock_zh_a_hist_min_em_df)
    yesterday_df = pd.DataFrame(yesterday_stock_zh_a_hist_min_em_df)
    latest_time = df['时间'].iloc[-1]
    is_closed = pd.to_datetime(latest_time) >= final_time
    def calculate_daily_summary(df):
        summary = {
            '日期': df['时间'].iloc[-1],
            '开盘价': df['开盘'].iloc[0],  # 第一条记录的开盘价
            '最新价': df['收盘'].iloc[-1],  # 最后一条记录的收盘价
            '收盘价': df['收盘'].iloc[-1] if is_closed else None,  # 收盘后才有收盘价
            '最高价': df['最高'].max(),  # 所有记录中的最高价
            '最低价': df['最低'].min(),  # 所有记录中的最低价
            '总成交量': df['成交量'].sum(),  # 成交量总和
            '总成交额': df['成交额'].sum(),  # 成交额总和
            '当日涨跌额': df['收盘'].iloc[-1] - df['开盘'].iloc[0],  # 最新价 - 开盘价
            '当日涨跌幅(%)': ((df['收盘'].iloc[-1] - df['开盘'].iloc[0]) / df['开盘'].iloc[0]) * 100,  # 涨跌幅百分比
            '涨跌额': df['收盘'].iloc[-1] - yesterday_df['收盘'].iloc[-1],  # 最新价 - 昨天收盘价
            '涨跌幅(%)': ((df['收盘'].iloc[-1] -yesterday_df['收盘'].iloc[-1]) / yesterday_df['收盘'].iloc[-1]) * 100,  # 涨跌幅百分比
            '均价': df['成交额'].sum() / df['成交量'].sum() if df['成交量'].sum() > 0 else 0,  # 成交额/成交量
        }
        return summary
    result = calculate_daily_summary(df)
    print("=" * 60)
    print(f"日期: {result['日期']}")
    print(f"代码：{symbol}    |   名称: {name}   |")
    print(f"开盘价: {result['开盘价']:.2f}    |   最新价: {result['最新价']:.2f}    |")
    print(f"最高价: {result['最高价']:.2f}    |   最低价: {result['最低价']:.2f}    |")
    print(f"当日涨跌额: {result['当日涨跌额']:+.2f}    |   当日涨跌幅: {result['当日涨跌幅(%)']:+.2f}%   |")
    print(f"涨跌额: {result['涨跌额']:+.2f}    |   涨跌幅: {result['涨跌幅(%)']:+.2f}%   |")

    # print(f"总成交量: {result['总成交量']:,}")
    # print(f"总成交额: {result['总成交额']:,.2f}")
    # print(f"均价: {result['均价']:.2f}")

# get_daily_info("001208","华凌线缆",datetime.now(), datetime.now())
