#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
import datetime

import sys
import os
os.environ["deepquantsdk_env"] = 'inner'

from deepquant.data.gqclient.hclient import GidHClient
from deepquant.data.gqclient.wsclient import WsClient, SubDataType, MarketType, VarietyCategoryType, BaseMDPushSpi

securities = ['000001.SZ', '600000.SH']

class FactorHandler(BaseMDPushSpi):

    def __init__(self):
        self.time_costs = []
        self.time_cost_sum = 0
        self.time_cost_count = 0
        self.time_max = 0
        self.time_max_data = None
        self.time_inc_first = None

    def on_subscribe_res(self, data, error):
        pass

    def on_index(self, data, error):
        pass

    def on_snapshot(self, data, error, **kwargs):
        print('snapshot'+data)

    def on_execution(self, data, error):
        pass

    def on_order(self, data, error):
        pass

    def on_orderqueue(self, data, error):
        pass

    def on_kline(self, data, error):
        pass

   


if __name__ == '__main__':
    print("实时行情-demo开始运行")
    # 全局标志变量
    keep_running = True

    reqClient = GidHClient()
    reqClient.init('<域用户名>', '<token>')
    # 设置回调函数
    md_handler = FactorHandler()
    # 行情连接客户端
    ws_client = WsClient()
    ws_client.init(reqClient)
    # 添加回调函数
    ws_client.add_md_handler(md_handler)
    # 启动行情连接
    ws_client.start()

    while not ws_client.is_connected:
        time.sleep(1)
        continue
    print("snapshot-发送订阅股票池:", securities)
    # 发送订阅请求
    ws_client.subscribe_md(SubDataType.SNAPSHOT,securities)
    while keep_running:
        time.sleep(1)
