#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:54:52 2023

@author: yuexiang
"""

import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("filtered_ship_routes_20km.csv")

# 替换 'yangshan' 和 'waigaoqiao' 为 'shanghai' 在第二列和第五列
df['depart_port'] = df['depart_port'].replace(['yangshan', 'waigaoqiao'], 'shanghai')
df['arrival_port'] = df['arrival_port'].replace(['yangshan', 'waigaoqiao'], 'shanghai')

# 保存修改后的数据到新的 CSV 文件
df.to_csv("modified_filtered_ship_routes_20km.csv", index=False)
