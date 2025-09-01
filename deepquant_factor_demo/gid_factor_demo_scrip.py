import os
os.environ["deepquantsdk_env"] = 'inner'
import  deepquant.data.interface.gid
from  deepquant.factor.factor_analyzer import FactorAnalyzer
import pandas as pd
from deepquant.factor import oq_data
gid=deepquant.data.interface.gid

gid.init('<域用户名>', '<token>');
od = oq_data.OqData('<域用户名>', '<token>')

## 编写因子函数
def getPool(stockIndex):
    query=gid.index_con([stockIndex],fields=['con_code'],df=True)
    pool=sorted(query[0].con_code.tolist())
    return pool

def getCalender(market,start_time,end_time,index=True):
    query=gid.trade_calendar(market=[market],
        start_time=start_time,end_time=end_time,
        fields=[],df=True)
    out=query[0].sort_values('trade_days').set_index('trade_days')
    if index:
        out=out.index[out.exchange=='SH']
    else:
        out=out.loc[out.exchange=='SH']
    return out

def roic_ttm(task_info):
    stockIndex=task_info['stockIndex']
    start_time=f'{task_info["startDate"]} 00:00:00'
    end_time  =f'{task_info["endDate"]} 23:59:00'

    pool=getPool(stockIndex)

    tradingDays=getCalender('SH',start_time=start_time,
        end_time=end_time,index=True)

    query=gid.ttm_mrq_factor(market_code=pool,
        start_time=start_time,end_time=end_time,
        fields=['market_code','ann_date',
            'roic_ttm',
            'report_period'],
        df=True)
    df=query[0]

    df=df.sort_values(by=['ann_date','report_period']).set_index('ann_date')
    poolTmp=sorted(df.market_code.unique())
    tmp=df.market_code
    lst=[]
    for symbol in poolTmp:
        dftmp=df.loc[tmp==symbol].copy()
        dftmp['lastest']=dftmp['report_period'].cummax()
        dftmp['lastestDiff']=(dftmp['report_period'].astype(int)-
                                dftmp['lastest'].astype(int))
        dftmp=dftmp[dftmp['lastestDiff']>=0]
        dftmp=dftmp.loc[~dftmp.index.duplicated(keep='last')]

        fac=dftmp['roic_ttm']
        reindexdf=fac.reindex(tradingDays,method='ffill')
        lst.append(reindexdf)
    out=pd.DataFrame(lst,index=poolTmp).T
    out.ffill(inplace=True)
    out.index=pd.to_datetime(out.index)
    out.index.name='dt'
    return out

### 系统入口函数
def factor_calc(task_info):
    return roic_ttm(task_info)

def getFactor():
       # 因子参数
        task_info = {
            'stockIndex':'000300.SH',
            'startDate':'2021-10-01',
            'endDate':'2026-10-22'
        }
       # 计算因子值
        factor_value=factor_calc(task_info)

       # 获取价格矩阵
        prices = od.get_prices_data(
            '000300.SH',
            '2021-10-01 00:00:00',
            '2026-10-22 00:00:00',
        )
        # 转换价格矩阵格式
        prices = prices.pivot(index="dt", columns="code", values="close").bfill()
        prices.index.name = "Date"

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

