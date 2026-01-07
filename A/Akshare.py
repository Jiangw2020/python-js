import akshare as ak
import pandas as pd

# stock_concept_cons_futu_df = ak.stock_concept_cons_futu(symbol="")
# print(stock_concept_cons_futu_df)
stock_board_concept_spot_em_df = ak.stock_board_concept_spot_em(symbol="商业航天")
print(stock_board_concept_spot_em_df)

df = pd.DataFrame(stock_board_concept_spot_em_df)

# 方法1：转换为字典列表
list_data = df.to_dict('records')
print(list_data)