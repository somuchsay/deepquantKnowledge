# -*- coding: utf-8 -*-

from deepquant.quest.apis import *
from deepquant.quest import run_func


def init(context):
    logger.info("init")
    context.s1 = "000001.SZ"
    update_universe(context.s1)
    context.fired = False


def before_trading(context):
    pass


def handle_bar(context, bar_dict):
    if not context.fired:
        # order_percent并且传入1代表买入该股票并且使其占有投资组合的100%
        order_percent(context.s1, 1)
        context.fired = True


config = {
  "base": {
    "data_bundle_path": "E:/Work/Coding/temp2/bundle",
    "start_date": "2016-06-01",
    "end_date": "2016-12-01",
    "accounts": {
      "stock": 100000
    }
  },
  "extra": {
    # "log_level": "verbose",
  },
  "mod": {
    "sys_analyser": {
      "benchmark": "000300.SH",
      "enabled": True,
      "plot": True
    }
  }
}

# 您可以指定您要传递的参数
run_func(init=init, before_trading=before_trading, handle_bar=handle_bar, config=config)

# 如果你的函数命名是按照 API 规范来，则可以直接按照以下方式来运行
# run_func(**globals())
