import akshare as ak
import pandas as pd
from collections import defaultdict

# target_sectors = ['商业航天', '人脑工程']
target_sectors = ['商业航天', '可控核聚变', "人脑工程", "人形机器人"]
stock_sectors = defaultdict(list)
def get_stocks_by_sectors(target_sectors, min_sector_count=2):
    for sector in target_sectors:
        try:
            stock_board_concept_cons_em_df = ak.stock_board_concept_cons_em(symbol=sector)
            df = pd.DataFrame(stock_board_concept_cons_em_df)
            for _, row in df.iterrows():
                code = row['代码']
                name = row['名称']
                stock_sectors[code].append({
                    'name': name,
                    'sector': sector
                })
        except Exception as e:
            print(f"  ✗ 获取板块 {sector} 失败: {e}")
    result = []
    for code, sectors_info in stock_sectors.items():
        sector_list = [s['sector'] for s in sectors_info]
        if len(sector_list) >= min_sector_count:
            name = sectors_info[0]['name']
            if 'ST' in name or not code.startswith(('00', '60')):
                continue

            result.append({
                '代码': code,
                '名称': name,
                '匹配板块': ', '.join(sector_list),
                '板块数量': len(sector_list)
            })
    result_df = pd.DataFrame(result)
    if not result_df.empty:
        result_df = result_df.sort_values('板块数量', ascending=False)

    return result_df


print(get_stocks_by_sectors(target_sectors))
