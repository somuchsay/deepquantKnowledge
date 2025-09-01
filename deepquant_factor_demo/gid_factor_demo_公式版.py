import os
os.environ["deepquantsdk_env"] = 'inner'
import  deepquant.data.interface.gid
import inspect
from  deepquant.factor.factor_analyzer import FactorAnalyzer
from  deepquant.factor.factor_cal import calc_factor
gid=deepquant.data.interface.gid
gid.init('<域用户名>', '<token>');



## 使用公有参数自定义函数
def alpha101(close):
    return close ;

def swMean(close):
    return TS_MEAN(close,5)/close;  #金融算子

def getFactor():
        # 获取股票池
        query = gid.index_con(['000300.SH'], fields=['con_code'], df=True)
        pool = sorted(query[0].con_code.tolist())
        # 计算因子值 factor_name=inspect.getsource(XXX),XXX是自定义的因子函数名
        factor_value, price = calc_factor(market_code=pool,
                                          factor_name=inspect.getsource(swMean),
                                          start_time="2023-08-01",
                                          end_time="2024-08-02", frequency="1d")

        # 转换价格矩阵格式
        prices = price.pivot(index='dt', columns='code', values='close').bfill()
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


