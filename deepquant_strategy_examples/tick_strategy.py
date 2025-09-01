# encoding: utf-8
from deepquant.quest.apis import *


__config__ = {
    "base": {
        "data_bundle_path": "E:/Work/Coding/temp67/bundle",
        "start_date": '2025-01-25',  # 回测起始日期
        "end_date": '2025-02-05',  # 回测结束日期
        'frequency': 'tick',
        "accounts": {
            "stock": 10000000
        },
    },
    "mod": {
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
}


def init(context):
    # 定义标
    # CS ETF Convertible Future option
    context.market_code = ['000002.SZ']
    subscribe(context.market_code)  # 订阅行情


# 盘前处理
def before_trading(context):
    pass

def handle_tick(context, tick):
    print("handle_tick.....", str(tick))
    print(tick.market_code)
    order_target_value(tick.market_code, 100)


# 盘后处理
def after_trading(context):
    pass


if __name__ == '__main__':
    from deepquant.quest.alpha import run_func
    data = run_func(init=init, before_trading=before_trading, after_trading=after_trading, handle_tick=handle_tick, config=__config__)
