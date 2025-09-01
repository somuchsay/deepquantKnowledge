# encoding: utf-8
from deepquant.quest.apis import *


def init(context):
    # 定义标
    # CS ETF Convertible Future option
    context.market_code = ['000001.SZ']
    for market_code in context.market_code:
        """
            在日级别回测中不需要订阅合约。
            在分钟回测中，若策略只设置了股票账户则不需要订阅合约；若设置了期货账户，则需要订阅策略关注的期货合约，
            框架会根据订阅的期货合约品种触发对应交易时间的 handle_bar。为了方便起见，也可以以直接订阅主力连续合约。
            在 tick 回测中，策略需要订阅每一个关注的股票/期货合约，框架会根据订阅池触发对应标的的 handle_tick
        """
        subscribe(market_code)  # 订阅行情
        context.fired = False



def handle_bar(context, bar_dict):
    print("handle_bar.....", str(bar_dict), bar_dict.__len__())
    print(bar_dict[context.market_code[0]])
    print(bar_dict[context.market_code[0]].open_price)
    if not context.fired:
        order_target_value(context.market_code[0], 50000)  # 将000001.SZ调仓到市值为50000（按目标金额下单）
        order_target_percent(context.market_code[0], 0.4)  # 如果投资组合中已经有了平安银行股票的仓位，并且占据目前投资组合的30%的价值，那么以下代码会消耗相当于当前投资组合价值10%的现金买入平安银行股票（按目标数量下单）
        #order_shares(context.market_code[1], 1000)  # 按数量下单
        #order_shares(context.market_code[2], 1000)  # 按数量下单
        order_value(context.market_code[0], 10000)  # 按金额下单
        #order_value(context.market_code[1], 10000)  # 按金额下单
        #order_value(context.market_code[2], 10000)  # 按金额下单
        #buy_open(context.market_code[3], 1)  # 做多一手期货
        #buy_open(context.market_code[4], 1)  # 做多一手期货
        #sell_open(context.market_code[3], 1)  # 做空一手期权
        #sell_open(context.market_code[4], 1)  # 做空一手期权
        context.fired = True




