
import pandas
import os

import yaml
import time
os.environ["deepquantsdk_env"] = 'inner'
import  deepquant.data.interface.gid
gid=deepquant.data.interface.gid
##第一步，登录
gid.init('<域用户名>', '<token>');
root = './inner/'

def get_all(pool):
    start = time.time()
    # 导出数据
    data, code, msg = gid.get_kline(market_code=pool, frequency='1d', start_time='2023-08-02 09:30:00',
                                    end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"get_kline执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_kline.csv', encoding=' utf-8', index=False)
    else:
        print("get_kline无数据")
		
	# 获取北交所K线
    data, code, msg = gid.get_kline(market_code=['837821.BJ','430139.BJ','830799.BJ','873593.BJ'], frequency='1d', start_time='2025-01-01 09:30:00',
                                    end_time='2025-04-19 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"get_kline_BJ执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_kline_BJ.csv', encoding=' utf-8', index=False)
    else:
        print("get_kline_BJ无数据")

    start = time.time()
    data, code, msg = gid.get_kline(market_code=['000300.SH'], frequency='1d', start_time='2023-08-02 09:30:00',
                                    end_time='2024-08-02 09:30:00', variety='index')
    end = time.time()
    execution_time = end - start
    print(f"get_kline_index执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_kline_index.csv', encoding=' utf-8', index=False)
    else:
        print("get_klin_index无数据")

    start = time.time()
    data, code, msg = gid.get_snapshot(market_code=['000001.SZ'], start_time='2024-08-01 09:30:00',
                                       end_time='2024-08-02 09:30:00', variety='stock')
    end = time.time()
    execution_time = end - start
    print(f"get_snapshot执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_snapshot.csv', encoding=' utf-8', index=False)
    else:
        print("get_snapshot无数据")
		
	# 获取北交所快照
    start = time.time()
    data, code, msg = gid.get_snapshot(market_code=['837821.BJ','430139.BJ','830799.BJ','873593.BJ'], start_time='2024-08-01 09:30:00',
                                       end_time='2024-08-02 09:30:00', variety='stock')
    end = time.time()
    execution_time = end - start
    print(f"get_snapshot_BJ执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_snapshot_BJ.csv', encoding=' utf-8', index=False)
    else:
        print("get_snapshot_BJ无数据")

    start = time.time()
    data, code, msg = gid.get_tick_execution(market_code=['000001.SZ'], start_time='2024-08-01 09:30:00',
                                             end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"get_tick_execution执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_tick_execution.csv', encoding=' utf-8', index=False)
    else:
        print("get_tick_execution无数据")

    start = time.time()
    data, code, msg = gid.get_tick_order(market_code=['000001.SZ'], start_time='2024-08-01 09:30:00',
                                         end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"get_tick_order执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_tick_order.csv', encoding=' utf-8', index=False)
    else:
        print("get_tick_order无数据")

    start = time.time()
    data, code, msg = gid.get_orderqueue(market_code=['000001.SZ'], start_time='2024-08-01 09:30:00',
                                         end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"get_orderqueue执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_orderqueue.csv', encoding=' utf-8', index=False)
    else:
        print("get_orderqueue无数据")

    # 资讯查询
    # 获取股票基本信息
    start = time.time()
    data, code, msg = gid.stock_basic(market_code=pool)
    end = time.time()
    execution_time = end - start
    print(f"stock_basic执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'stock_basic.csv', encoding=' utf-8', index=False)
    else:
        print("stock_basic无数据")

    # 行业分类信息
    start = time.time()
    data, code, msg = gid.industry(market_code=pool)
    end = time.time()
    execution_time = end - start
    print(f"industry执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'industry.csv', encoding=' utf-8', index=False)
    else:
        print("industry无数据")

    # 公司简介信息
    start = time.time()
    data, code, msg = gid.company(market_code=pool)
    end = time.time()
    execution_time = end - start
    print(f"company执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'company.csv', encoding=' utf-8', index=False)
    else:
        print("company无数据")

    # 股本信息
    start = time.time()
    data, code, msg = gid.sharehold(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"sharehold执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'sharehold.csv', encoding=' utf-8', index=False)
    else:
        print("sharehold无数据")

    # 公司主营业务信息
    start = time.time()
    data, code, msg = gid.segment(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"segment执行时间：{execution_time} 秒")

    if data is not None:
        data.to_csv(root + 'segment.csv', encoding=' utf-8', index=False)
    else:
        print("segment无数据")

    # 历史股票列表信息
    start = time.time()
    data, code, msg = gid.historysymbollist(start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00',
                                            variety='stock')
    end = time.time()
    execution_time = end - start
    print(f"historysymbollist执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'historysymbollist.csv', encoding=' utf-8', index=False)
    else:
        print("historysymbollist无数据")

    # 首次公开发行信息
    start = time.time()
    data, code, msg = gid.stock_ipo(market_code=pool)
    end = time.time()
    execution_time = end - start
    print(f"stock_ipo执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'stock_ipo.csv', encoding=' utf-8', index=False)
    else:
        print("stock_ipo无数据")

    # 增发数据信息
    start = time.time()
    data, code, msg = gid.listmore(market_code=pool)
    end = time.time()
    execution_time = end - start
    print(f"listmore执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'listmore.csv', encoding=' utf-8', index=False)
    else:
        print("listmore无数据")

    # 股票分红信息
    start = time.time()
    data, code, msg = gid.divident(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"divident执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'divident.csv', encoding=' utf-8', index=False)
    else:
        print("divident无数据")

    # 股票配股信息
    start = time.time()
    data, code, msg = gid.allotment(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"allotment执行时间：{execution_time} 秒")

    if data is not None:
        data.to_csv(root + 'allotment.csv', encoding=' utf-8', index=False)
    else:
        print("allotment无数据")

    # 股票除权除息信息
    start = time.time()
    data, code, msg = gid.exdiv(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"exdiv执行时间：{execution_time} 秒")

    if data is not None:
        data.to_csv(root + 'exdiv.csv', encoding=' utf-8', index=False)
    else:
        print("exdiv无数据")

    # 复权因子表信息
    start = time.time()
    data, code, msg = gid.exfactor(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"exfactor执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'exfactor.csv', encoding=' utf-8', index=False)
    else:
        print("exfactor无数据")

    # A股十大股东名单
    start = time.time()
    data, code, msg = gid.top10holders(market_code=pool, start_time='2023-08-02 09:30:00',
                                       end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"top10holders执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'top10holders.csv', encoding=' utf-8', index=False)
    else:
        print("top10holders无数据")

    # A限售股解禁明细
    start = time.time()
    data, code, msg = gid.restricted_free(market_code=pool, start_time='2023-08-02 09:30:00',
                                          end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"restricted_free执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'restricted_free.csv', encoding=' utf-8', index=False)
    else:
        print("restricted_free无数据")

    # 解禁数据
    start = time.time()
    data, code, msg = gid.freefloat(market_code=pool, limit=300)
    end = time.time()
    execution_time = end - start
    print(f"freefloat执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'freefloat.csv', encoding=' utf-8', index=False)
    else:
        print("freefloat无数据")

    # 股权持股冻结/质押情况信息
    start = time.time()
    data, code, msg = gid.pledge(market_code=['000002.SZ'], start_time='2023-08-02 09:30:00',
                                 end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"pledge执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'pledge.csv', encoding=' utf-8', index=False)
    else:
        print("pledge无数据")

    # A股一般企业资产负债表
    start = time.time()
    data, code, msg = gid.balancesheet(market_code=pool, start_time='2023-08-02 09:30:00',
                                       end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"balancesheet执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'balancesheet.csv', encoding=' utf-8', index=False)
    else:
        print("balancesheet无数据")

    # A股一般企业利润表
    start = time.time()
    data, code, msg = gid.income(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"income执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'income.csv', encoding=' utf-8', index=False)
    else:
        print("income无数据")

    # A股一般企业现金流表
    start = time.time()
    data, code, msg = gid.cashflow(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"cashflow执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'cashflow.csv', encoding=' utf-8', index=False)
    else:
        print("cashflow无数据")

        # A股财务指标
    start = time.time()
    data, code, msg = gid.fina_forecast(market_code=pool, start_time='0', end_time='0')
    end = time.time()
    execution_time = end - start
    print(f"fina_forecast执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'fina_forecast.csv', encoding=' utf-8', index=False)
    else:
        print("fina_forecast无数据")

    # A股财务指标
    start = time.time()
    data, code, msg = gid.fina_indicator(market_code=pool, start_time='0', end_time='0')
    end = time.time()
    execution_time = end - start
    print(f"fina_indicator执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'fina_indicator.csv', encoding=' utf-8', index=False)
    else:
        print("fina_indicator无数据")

    # A股财务衍生指标
    start = time.time()
    data, code, msg = gid.fina_indicator_derive(market_code=pool, start_time='2023-08-02 09:30:00',
                                                end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"fina_indicator_derive执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'fina_indicator_derive.csv', encoding=' utf-8', index=False)
    else:
        print("fina_indicator_derive无数据")

    # 交易日历
    start = time.time()
    data, code, msg = gid.trade_calendar(market=['SZ'], start_time='2023-08-02 09:30:00',
                                         end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"trade_calendar执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'trade_calendar.csv', encoding=' utf-8', index=False)
    else:
        print("trade_calendar无数据")

    # 大宗交易数据
    start = time.time()
    data, code, msg = gid.block_trade(market_code=pool, start_time='2023-08-02 09:30:00',
                                      end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"block_trade执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'block_trade.csv', encoding=' utf-8', index=False)
    else:
        print("block_trade无数据")

    # 机构龙虎榜
    start = time.time()
    data, code, msg = gid.top_inst(market_code=pool, start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"top_inst执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'top_inst.csv', encoding=' utf-8', index=False)
    else:
        print("top_inst无数据")

    # 融资融券交易明细信息
    start = time.time()
    data, code, msg = gid.margin_detail(market_code=pool, start_time='2023-08-02 09:30:00',
                                        end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"margin_detail执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'margin_detail.csv', encoding=' utf-8', index=False)
    else:
        print("margin_detail无数据")

    # 融资融券成交汇总信息
    start = time.time()
    data, code, msg = gid.margin(market=['SZ'], start_time='2023-08-02 09:30:00', end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"margin执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'margin.csv', encoding=' utf-8', index=False)
    else:
        print("margin无数据")

    # 基金最新指标信息
    start = time.time()
    data, code, msg = gid.fund_indicator(market_code=['159919.SZ'], start_time='2023-08-02 09:30:00',
                                         end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"fund_indicator执行时间：{execution_time} 秒")

    if data is not None:
        data.to_csv(root + 'fund_indicator.csv', encoding=' utf-8', index=False)
    else:
        print("fund_indicator无数据")

    # A股指数成分股
    start = time.time()
    data, code, msg = gid.index_con(index_code=['399001.SZ'])
    end = time.time()
    execution_time = end - start
    print(f"index_con执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'index_con.csv', encoding=' utf-8', index=False)
    else:
        print("index_con无数据")

    # A股指数成分股
    start = time.time()
    data, code, msg = gid.index_con_his(index_code=['399001.SZ'], start_time='2023-08-02 09:30:00',
                                        end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"index_con_his：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'index_con_his.csv', encoding=' utf-8', index=False)
    else:
        print("index_con_his无数据")

    #   获取ttm因子数据
    start = time.time()
    data, code, msg = gid.ttm_mrq_factor(market_code=pool, start_time='2023-08-02 09:30:00',
                                         end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"ttm_mrq_factor执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'ttm_mrq_factor.csv', encoding=' utf-8', index=False)
    else:
        print("ttm_mrq_factors无数据")

    #   查询A股日收益率

    start = time.time()
    data, code, msg = gid.yield_factor(market_code=pool, start_time='2023-08-02 09:30:00',
                                       end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"yield_factor执行时间：{execution_time} 秒")

    if data is not None:
        data.to_csv(root + 'yield_factor.csv', encoding=' utf-8', index=False)
    else:
        print("yield_factor无数据")

    #     查询A股日行情估值指标
    start = time.time()
    data, code, msg = gid.derivind_factor(market_code=pool, start_time='2023-08-02 09:30:00',
                                          end_time='2024-08-02 09:30:00')
    end = time.time()
    execution_time = end - start
    print(f"derivind_factor执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'derivind_factor.csv', encoding=' utf-8', index=False)
    else:
        print("derivind_factor无数据")

    start = time.time()
    data, code, msg = gid.get_factor_by_date(factor_name='zhouhuan_it.python1', start_time='2023-01-03 08:00:00',
                                             end_time='2024-09-04 08:00:00', freq='1d', symbol_pool=['000300.SH'])
    end = time.time()
    execution_time = end - start
    print(f"get_factor执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'get_factor.csv', encoding=' utf-8', index=False)
    else:
        print("get_factor无数据")

    start = time.time()
    data, code, msg = gid.allFactors(factorType='ALL')
    end = time.time()
    execution_time = end - start
    print(f"allFactors执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'allFactors.csv', encoding=' utf-8', index=False)
    else:
        print("allFactors无数据")

    start = time.time()
    data, code, msg = gid.dayprices(market_code=pool, start_time='2023-08-02', end_time='2024-08-02')
    end = time.time()
    execution_time = end - start
    print(f"dayprices执行时间：{execution_time} 秒")
    if data is not None:
        data.to_csv(root + 'dayprices.csv', encoding=' utf-8', index=False)
    else:
        print("dayprices无数据")


if __name__ == "__main__":

    query = gid.index_con(['000300.SH'], fields=['con_code'], df=True)
    pool = sorted(query[0].con_code.tolist())
    get_all(pool)
