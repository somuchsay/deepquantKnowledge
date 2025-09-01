# encoding: utf-8
from deepquant.quest.apis import *


__config__ = {
    "base": {
        "data_bundle_path": "E:/Work/Coding/temp67/bundle",
        "start_date": '2024-01-13',  # 回测起始日期
        "end_date": '2024-02-25',  # 回测结束日期
        'frequency': '1d',
        "accounts": {
            "stock": 10000000
        },
    },
    "mod": {
        "sys_analyser": {
            "enabled" : True,
            #"lib" : deepquant.quest.mod.mod_sys_analyser_web,
            # 策略基准，该基准将用于风险指标计算和收益曲线图绘制
            #   若基准为单指数/股票，此处直接设置 market_code，如："000300.SH"
            #   若基准为复合指数，则需传入 market_code 和权重构成的字符串，如："000300.SH:0.2,000905.SH:0.8"
            "benchmark": None,
            # 当不输出 csv/pickle/plot 等内容时，关闭该项可关闭策略运行过程中部分收集数据的逻辑，用以提升性能
            "record": True,
            # 策略名称，可设置 summary 报告中的 strategy_name 字段，并展示在 plot 回测结果图中
            "strategy_name": None,
            # 回测结果输出的文件路径，该文件为 pickle 格式，内容为每日净值、头寸、流水及风险指标等；若不设置则不输出该文件
            "output_file": None,
            # 回测报告的数据目录，报告为 csv 格式；若不设置则不输出报告
            "report_save_path": None,
            # 是否在回测结束后绘制收益曲线图
            'plot': 'deepquant',
            # 收益曲线图路径，若设置则将收益曲线图保存为 png 文件
            'plot_save_file': None,
            # 收益曲线图设置
            'plot_config': {
                # 是否在收益图中展示买卖点
                'open_close_points': False,
                # 是否在收益图中展示周度指标和收益曲线
                'weekly_indicators': False
            },
        },
        "sys_accounts": {
            # 是否开启股票 T+1 限制
            "stock_t1": True,
            # 是否开启自动分红再投资
            "dividend_reinvestment": False,
            # 当持仓股票退市时，是否按照退市价格返还现金
            "cash_return_by_stock_delisted": True,
            # 股票下单因资金不足被拒时改为使用全部剩余资金下单
            "auto_switch_order_value": False,
            # 开启对股票仓位是否能满足平仓需求的检查
            "validate_stock_position": True,
            # 开启对期货仓位是否能满足平仓需求的检查
            "validate_future_position": True,
            # 融资利率/年
            "financing_rate": 0.00,
            # 是否开启融资可买入股票的限制
            "financing_stocks_restriction_enabled": False,
            # 逐日盯市结算价: settlement/close
            "futures_settlement_price_type": "close_price",
        },
        "sys_simulation": {
            # 撮合方式，其中：
            #   日回测的可选值为 "current_bar"|"vwap"（以当前 bar 收盘价｜成交量加权平均价撮合）
            #   分钟回测的可选值有 "current_bar"|"next_bar"|"vwap"（以当前 bar 收盘价｜下一个 bar 的开盘价｜成交量加权平均价撮合)
            #   tick 回测的可选值有 "last"|"best_own"|"best_counterparty"（以最新价｜己方最优价｜对手方最优价撮合）和 "counterparty_offer"（逐档撮合）
            #   matching_type 为 None 则表示根据回测频率自动选择。日/分钟回测下为 current_bar , tick 回测下为 last
            "matching_type": None,
            # 开启对于处于涨跌停状态的证券的撮合限制
            "price_limit": True,
            # 开启对于对手盘无流动性的证券的撮合限制（仅在 tick 回测下生效）
            "liquidity_limit": False,
            # 开启成交量限制
            #   开启该限制意味着每个 bar 的累计成交量将不会超过该时间段内市场上总成交量的一定比值（volume_percent）
            #   开启该限制意味着每个 tick 的累计成交量将不会超过当前tick与上一个tick的市场总成交量之差的一定比值
            "volume_limit": False,
            # 每个 bar/tick 可成交数量占市场总成交量的比值，在 volume_limit 开启时生效
            "volume_percent": 0.25,
            # 滑点模型，可选值有 "PriceRatioSlippage"（按价格比例设置滑点）和 "TickSizeSlippage"（按跳设置滑点）
            #    亦可自己实现滑点模型，选择自己实现的滑点模型时，此处需传入包含包和模块的完整类路径
            #    滑点模型类需继承自 yhalpha.mod.mod_sys_simulation.slippage.BaseSlippage
            "slippage_model": "PriceRatioSlippage",
            # 设置滑点值，对于 PriceRatioSlippage 表示价格的比例，对于 TickSizeSlippage 表示跳的数量
            "slippage": 0.001,
        },
        # 费用模块，该模块的配置项用于调整交易的税费
        "sys_transaction_cost": {
            # 股票最小手续费，单位元
            "cn_stock_min_commission": 5,
            # 股票佣金倍率,即在默认的手续费率基础上按该倍数进行调整，股票的默认佣金为万八
            "stock_commission_multiplier": 1,
            # 期货佣金倍率,即在默认的手续费率基础上按该倍数进行调整，期货默认佣金因合约而异
            "futures_commission_multiplier": 1,
            # 印花倍率，即在默认的印花税基础上按该倍数进行调整，股票默认印花税为万分之五，单边收取
            "tax_multiplier": 1,
            # 是否使用回测当时时间点对应的真实印花税率
            "pit_tax": False,
        },
        "option" : {
            "enabled" : False
        },
        "convertible" : {
            "enabled" : False
        },
        "spot" : {
            "enabled" : False
        },
        "fund" : {
            "enabled": False
        },
        "profile_web": {
            "enabled": False
        }
    },
    "extra": {
        # 系统日志级别，用于控制策略框架输出日志的详细程度（策略打印的日志不受该选项控制），设置为某一级别则框架会输出该级别及更"严重"的日志
        # 可选值："debug"|"info"|"warning"|"error"，通常推荐设置为 info 或 warning
        # error 日志一般为不可逆的错误，如策略抛出异常、加载 Mod 失败等
        # warning 日志一般为告警信息，如 API 废弃、订单创建失败等
        # info 日志一般为说明性的信息，如 Mod 在某种设置下被动关闭等
        # debug 日志一般为开发者关注的调试信息，如策略状态变更、事件触发等，用户通常不需要关注
        "log_level": "info",
        # 是否开启性能分析
        "enable_profiler": False,
        # 输出的日志文件路径
        "log_file": None,
        'backtest_id':'18870467177349160960001',
        'base_url':"http://apisix.tsxcph.chinastock.com.cn",
    },
}

def order_event(context, event):
    print(event.event_type, event.market_code, event.reason)


def init(context):
    # 定义标
    # CS ETF Convertible Future option
    context.market_code = ['000001.SZ']
    #print("get_all_instruments:   ", yhdatac.all_instruments(type_="stock", date='2003-01-01'))
    #print("get_share_transformation:   ", yhdatac.get_share_transformation())
    # print("get_ex_factor:   ", yhdatac.get_ex_factor(order_book_ids=['000001.SZ', '600000.SH'], start_date="2005-01-01",
    #                                                end_date="2024-01-01"))
    #print("get_dividend:   ", yhdatac.get_dividend(order_book_ids=['000001.SZ','600000.SH'], start_date="2005-01-01", end_date="2024-01-01"))
    #print("get_factor:   ", get_factor(market_code=['000001.SZ', '601988.SH'], factors="public.eps_ttm", count=10))
    #print("get_instrument_industry:   ", get_instrument_industry(market_code=['000001.SZ', '601988.SH']))
    #print("get_turnover_rate:   ", get_turnover_rate(market_code=['000001.SZ', '601988.SH'], count=30, expect_df=True))
    #print("get_shares:   ", get_shares(market_code=['000001.SZ','601988.SH'], count=30, expect_df=True))
    #from deepquant.quest.datac.services.calendar import get_trading_dates
    #print(get_trading_dates(start_date="2005-01-04", end_date="2026-01-01"))
    #print(get_price(market_code=['000001.SZ'], start_date="2019-04-10", frequency='1d'))
    #print(get_price(market_code=['000001.SZ'], start_date="2014-04-10", frequency='1m', end_date="2014-04-11"))
    #print(get_price(market_code=['000002.SZ'], start_date="2025-01-08", frequency='tick'))
    #print(get_price(market_code=['000001.SH','000002.SH','000003.SH','000004.SH'], start_date="2015-01-10", frequency='1d', variety='index'))
    #print("get_securities_margin...  ", get_securities_margin(market_code=['000001.SZ','601988.SH'], count=300, expect_df=True))
    #yhdatac.get_suspend_days(market_code=['000001.SZ','600000.SH'], start_date="2005-01-01", end_date="2024-01-01")
    #print(get_industry("农业"))
    #print(concept('民营医院', '国企改革'))
    """
    事件类型：
        ORDER_PENDING_NEW
        订单创建成功
        ORDER_CREATION_PASS
        订单已报
        ORDER_CREATION_REJECT
        订单创建被拒
        ORDER_PENDING_CANCEL
        订单待撤
        ORDER_CANCELLATION_PASS
        订单撤单成功
        ORDER_CANCELLATION_REJECT
        订单撤单被拒
        ORDER_UNSOLICITED_UPDATE
        订单已报被拒
        TRADE
        成交
    """
    subscribe_event(EVENT.ORDER_CREATION_REJECT, order_event)
    context.count = 1


# 开盘集合竞价
def open_auction(context, bar_dict):
    if context.count == 1:
        print(bar_dict[context.market_code[0]].low_limited)
        order_shares(context.market_code[0], 1000)


# 盘前处理
def before_trading(context):
    if context.count == 1:
        price_df = history_bars(context.market_code[0], 10, frequency="1d")  # 历史数据的拉取
        #factor_df = get_factor(context.market_code[0], 'MA30', 1)  # 获取因子
        #print(price_df, factor_df)


def handle_bar(context, bar_dict):
    print("handle_bar.....", str(bar_dict), bar_dict.__len__())
    print(bar_dict[context.market_code[0]])
    print(bar_dict[context.market_code[0]].open_price)

    if context.count == 1:
        deposit('STOCK', 10000)  # 盘前股票账户入金10000
        #deposit('FUTURE', 10000)  # 盘前期货账户入金10000
        withdraw('STOCK', 10000)  # 盘前股票账户出金10000
        #withdraw('FUTURE', 10000)  # 盘前期货账户出金10000
        print(f'订单数量：{get_open_orders()}')
        #order_shares(context.market_code[0], 1000, TWAPOrder(931, 945))  # 按数量下单（twap算法単）
        #order_shares(context.market_code[0], 1000, VWAPOrder(931, 945))  # 按数量下单（vwap算法単）
        order_target_value(context.market_code[0], 50000)  # 将000001.SZ调仓到市值为50000（按目标金额下单）
        order_target_percent(context.market_code[0], 0.4)  # 如果投资组合中已经有了平安银行股票的仓位，并且占据目前投资组合的30%的价值，那么以下代码会消耗相当于当前投资组合价值10%的现金买入平安银行股票（按目标数量下单）
        '''
        order_shares(context.market_code[1], 1000)  # 按数量下单
        order_shares(context.market_code[2], 1000)  # 按数量下单
        order_value(context.market_code[0], 10000)  # 按金额下单
        order_value(context.market_code[1], 10000)  # 按金额下单
        order_value(context.market_code[2], 10000)  # 按金额下单

        buy_open(context.market_code[3], 1)  # 做多一手期货
        buy_open(context.market_code[4], 1)  # 做多一手期货
        sell_open(context.market_code[3], 1)  # 做空一手期权
        sell_open(context.market_code[4], 1)  # 做空一手期权
        '''

# 盘后处理
def after_trading(context):
    if context.count == 1:
        for p in get_positions():
            print(f'{p.market_code} 持仓: {p.quantity}')
        print(f'可用资金: {context.stock_account.cash}')
    context.count += 1


if __name__ == '__main__':
    from deepquant.quest.alpha import run_func

    data = run_func(init=init, before_trading=before_trading, after_trading=after_trading, handle_bar=handle_bar,
                    config=__config__, open_auction=open_auction)
