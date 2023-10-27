#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:01:59 2023

@author: yuexiang
"""

import pandas as pd

# 读取数据
file_path = "ship_port_visits_175km.csv"
df = pd.read_csv(file_path)

# 按imo和timestamp排序
df = df.sort_values(by=['imo', 'timestamp'])

# 生成航线数据
routes = {
    'imo': [],
    '上游港口': [],
    '上游国家': [],
    '上游时间': [],
    '下游港口': [],
    '下游国家': [],
    '下游时间': []
}

# 遍历每行数据
for i in range(len(df) - 1):
    # 如果下一行数据的IMO与当前行相同，则这两行数据可以生成一次航线
    if df.iloc[i]['imo'] == df.iloc[i + 1]['imo']:
        routes['imo'].append(df.iloc[i]['imo'])
        routes['上游港口'].append(df.iloc[i]['port_name'])
        routes['上游国家'].append(df.iloc[i]['country_name'])
        routes['上游时间'].append(df.iloc[i]['timestamp'])
        routes['下游港口'].append(df.iloc[i + 1]['port_name'])
        routes['下游国家'].append(df.iloc[i + 1]['country_name'])
        routes['下游时间'].append(df.iloc[i + 1]['timestamp'])

# 将字典转换为DataFrame
routes_df = pd.DataFrame(routes)

# 保存结果
routes_df.to_csv("ship_routes_175km.csv", index=False)
