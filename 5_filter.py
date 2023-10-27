#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:02:52 2023

@author: yuexiang
"""

import pandas as pd

# 读取数据
file_path = "ship_routes_175km.csv"
df = pd.read_csv(file_path)

# 筛选出depart_port和arrival_port不一样的数据行，并且imo不为0
filtered_df = df[(df['depart_port'] != df['arrival_port']) & (df['imo'] != 0)]

# 保存结果到新文件
filtered_df.to_csv("filtered_ship_routes_175km.csv", index=False)
