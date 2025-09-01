# -*- coding: utf-8 -*-

from deepquant.quest import run_file

config = {
  "base": {
    "data_bundle_path": "E:/Work/Coding/temp67/bundle",
    "start_date": "2016-06-01",
    "end_date": "2016-12-01",
    "benchmark": "000300.SH",
    "accounts": {
      "stock": 100000
    }
  },
  "extra": {
    "log_level": "verbose",
  },
  "mod": {
    "sys_analyser": {
      "enabled": True,
      "plot": True
    }
  }
}

strategy_file_path = "./buy_and_hold.py"

run_file(strategy_file_path, config)
