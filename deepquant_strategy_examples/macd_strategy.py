# encoding: utf-8
from deepquant.quest.apis import *

import pandas as pd

__config__ = {
    "base": {
        "data_bundle_path": "E:/Work/Coding/temp67/bundle",
        "start_date": '2022-09-05',  # 回测起始日期
        "end_date": '2022-09-29',  # 回测结束日期
        'frequency': '1d',
        "accounts": {
            "stock": 10000000
        },
    },
    "mod": {
        "sys_analyser": {
            # 策略基准，该基准将用于风险指标计算和收益曲线图绘制
            #   若基准为单指数/股票，此处直接设置 order_book_id，如："000300.SH"
            #   若基准为复合指数，则需传入 order_book_id 和权重构成的字符串，如："000300.SH:0.2,000905.SH:0.8"
            "benchmark": '000001.SZ',
            # 当不输出 csv/pickle/plot 等内容时，关闭该项可关闭策略运行过程中部分收集数据的逻辑，用以提升性能
            "record": False,
            # 策略名称，可设置 summary 报告中的 strategy_name 字段，并展示在 plot 回测结果图中
            "strategy_name": 'mack.pickle',
            # 回测结果输出的文件路径，该文件为 pickle 格式，内容为每日净值、头寸、流水及风险指标等；若不设置则不输出该文件
            "output_file": '/output',
            # 回测报告的数据目录，报告为 csv 格式；若不设置则不输出报告
            "report_save_path": './backtest',
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
            "enabled" : False
        },
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
    }
}
def init(context):
    # 设置沪深300指数作为标的
    #context.s1 = "000001.SH"
    context.order_book_ids = ['000001.SZ']
    # 设置MACD参数
    context.short = 12
    context.long = 26
    context.m = 9
    # 订阅数据
    subscribe(context.order_book_ids[0])

def handle_bar(context, bar_dict):
    # 获取历史数据
    #price_df = history_bars(context.order_book_ids[0], 10, frequency="1d")  # 历史数据的拉取
    prices = history_bars(context.order_book_ids[0], context.long + context.m, frequency="1d",fields="close_price")

    p = pd.Series(prices)
    # 计算EMA
    #short_ema = prices[-context.short:].mean()
    short_ema = p.ewm(span=context.short, adjust=False).mean()
    #long_ema = prices[-context.long:].mean()
    long_ema = p.ewm(span=context.long, adjust=False).mean()
    # 计算MACD和信号线
    macd = short_ema - long_ema
    # s = pd.Series(macd)
    signal = macd.ewm(span=context.m, adjust=False).mean()
    
    # 获取当前持仓
    cur_position = context.portfolio.positions[context.order_book_ids[0]].quantity

    print(macd.iloc[-1])
    # 交易逻辑
    if macd.iloc[-1] > signal.iloc[-1] and macd.iloc[-2] <= signal.iloc[-2] and cur_position == 0:
        # 买入信号
        print('买入')
        order_target_percent(context.order_book_ids[0], 0.1)
    elif macd.iloc[-1] < signal.iloc[-1] and macd.iloc[-2] >= signal.iloc[-2] and cur_position > 0:
        # 卖出信号
        print('卖出')
        order_target_percent(context.order_book_ids[0], 0)

def before_trading(context):
    #prices = history_bars(context.order_book_ids[0], context.long + context.m, '1d')
    pass

def after_trading(context):
    pass

if __name__ == '__main__':
    from deepquant.quest.alpha import run_func

    data = run_func(init=init, before_trading=before_trading, after_trading=after_trading, handle_bar=handle_bar,
                    config=__config__)