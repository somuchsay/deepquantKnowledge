import os
os.environ["deepquantsdk_env"] = 'inner'
from  deepquant.factor.factor_analyzer import FactorAnalyzer
from deepquant.factor import oq_data

def getFactor():

    # 设置用户名和token
    od = oq_data.OqData('<域用户名>', '<token>')

    # 获取平台提供的公共因子值
    data = od.get_factor_rows(
        factor_name='public.cashflow_per_share_ttm',
        start_time='2023-11-01 00:00:00',
        end_time='2024-11-01 00:00:00',
        freq='1d',
        symbol_pool=['000300.SH'])

    # 转换因子值数据的矩阵格式
    factor_value = data.pivot(index='date', values='factor', columns='asset')

    # 获取价格矩阵
    prices = od.get_prices_data(
        '000300.SH',
        '2023-01-01 00:00:00',
        '2024-11-01 00:00:00',
    )
    # 转换价格矩阵格式
    prices = prices.pivot(index='dt', columns='code', values='close').bfill()
    prices.index.name = 'Date'


    # 创建因子分析工具类
    far = FactorAnalyzer(factor_value, prices, groupby=None, weights=1,
                                 quantiles=5, bins=None, periods=(1, 5, 10),
                                 binning_by_group=False, max_loss=0.7, zero_aware=False)

    # 输出因子分析报表到html文件
    far.create_full_tear_sheet(
        demeaned=False,
        group_adjust=False,
        by_group=True,
        turnover_periods=None,
        avgretplot=(5, 15),
        std_bar=True,
        html_output=True
    )

if __name__ == "__main__":

    getFactor()



