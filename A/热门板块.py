import akshare as ak
import pandas as pd

# 技术指标：量价齐升，连续上涨，创新高
# 资讯数据：财经快讯
# 涨停板行情： 涨停股池
# 板块异动详情
# 盘口异动
# 股票热度： 人气榜-A股，飙升榜-A股
# 行业板块：东方财富-行业板块，东方财富-成份股（筛选某个板块股份）
# 概念板块：东方财富-概念板块，东方财富-成份股（筛选某个板块股份），概念资金流
# 大宗交易：活跃营业部统计，活跃 A 股统计
# 资金流向
# 财经内容精选（市场动态，今日热点）
# 千股千评详情：机构参与度
# 风险警示板
# 股市日历：公司动态
# 历史行情数据： 后复权后




def analyze_hot_sectors(top_n=5):
    # 行业板块数据
    # stock_board_industry_name_em_df = ak.stock_board_industry_name_em()
    # df = pd.DataFrame(stock_board_industry_name_em_df)
    # industry_data = df.to_dict('records')
    industry = []

    # 概念板块数据
    stock_board_concept_name_em_df = ak.stock_board_concept_name_em()
    df = pd.DataFrame(stock_board_concept_name_em_df)
    concept = df.to_dict('records')

    all_sectors = []
    for sector in industry:
        total_stocks = sector['上涨家数'] + sector['下跌家数']
        rise_ratio = sector['上涨家数'] / total_stocks if total_stocks > 0 else 0
        score = sector['排名']

        all_sectors.append({
            '类型': '行业板块',
            '板块名称': sector['板块名称'],
            '涨跌幅': f"{sector['涨跌幅']:.2f}%",
            '换手率': f"{sector['换手率']:.2f}%",
            '上涨家数': sector['上涨家数'],
            '下跌家数': sector['下跌家数'],
            '上涨占比': f"{rise_ratio * 100:.1f}%",
            '总市值': f"{sector['总市值'] / 1e8:.0f}亿",
            '领涨股票': f"{sector['领涨股票']}(+{sector['领涨股票-涨跌幅']:.2f}%)",
            '综合得分': score,
            '原始排名': sector['排名']
        })

    exclude_keywords = ['昨日', '涨停', '连板', '触板']
    for sector in concept:
        if any(keyword in sector['板块名称'] for keyword in exclude_keywords):
            continue

        total_stocks = sector['上涨家数'] + sector['下跌家数']
        rise_ratio = sector['上涨家数'] / total_stocks if total_stocks > 0 else 0
        score = sector['排名']
        # score = (
        #         sector['涨跌幅'] * 0.40 +
        #         sector['换手率'] * 0.20 +
        #         rise_ratio * 100 * 0.25 +
        #         (sector['总市值'] / 1e11) * 0.15
        # )

        all_sectors.append({
            '类型': '概念板块',
            '板块名称': sector['板块名称'],
            '涨跌幅': f"{sector['涨跌幅']:.2f}%",
            '换手率': f"{sector['换手率']:.2f}%",
            '上涨家数': sector['上涨家数'],
            '下跌家数': sector['下跌家数'],
            '上涨占比': f"{rise_ratio * 100:.1f}%",
            '总市值': f"{sector['总市值'] / 1e8:.0f}亿",
            '领涨股票': f"{sector['领涨股票']}(+{sector['领涨股票-涨跌幅']:.2f}%)",
            '综合得分': score,
            '原始排名': sector['排名']
        })
    all_sectors.sort(key=lambda x: x['综合得分'], reverse=False)
    hot_sectors = all_sectors[:top_n]
    for i, sector in enumerate(hot_sectors, 1):
        print(f"🔥 第{i}名：{sector['板块名称']} ({sector['类型']})")
        print(f"   涨跌幅: {sector['涨跌幅']}  |  换手率: {sector['换手率']}")
        print(f"   上涨家数: {sector['上涨家数']}家  下跌家数: {sector['下跌家数']}家  (上涨占比: {sector['上涨占比']})")
        print(f"   总市值: {sector['总市值']}  |  领涨股: {sector['领涨股票']}")
        # print(f"   综合得分: {sector['综合得分']:.2f}")
        print("-" * 80)
    return hot_sectors
# hot_sectors = analyze_hot_sectors(industry_data, concept_data)

