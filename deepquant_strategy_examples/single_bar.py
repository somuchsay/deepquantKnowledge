# 单股票买入并持有策略（日级别）

from deepquant.quest import run_func
from deepquant.quest.apis import *


FREQUENCY = "1d" # 策略的频率，该策略可选为 1d, 1m

__config__ = {
    "base": {
        "data_bundle_path": "E:/Work/Coding/temp67/bundle",
        "start_date": "2023-01-04",
        "end_date": "2024-01-04",
        "frequency": FREQUENCY,
        "accounts": {
            "stock": 10000000
        }
    }
}


def init(context):
    context.s1 = "000001.SZ"
    context.fired = False


def handle_bar(context, bar_dict):
    print("###receive bar...", bar_dict)
    if not context.fired:
        order_shares(context.s1, 1000)
        context.fired = True


run_func(config=__config__, init=init, handle_bar=handle_bar)