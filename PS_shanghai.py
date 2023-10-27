#这次在筛选数据时没有直接替换yangshan和waigaoqiao为shanghai。因此在处理后才补充了一个代码来替换
#之后会合并到“filter”的代码中

import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("filtered_ship_routes_20km.csv")

# 替换 'yangshan' 和 'waigaoqiao' 为 'shanghai' 在第二列和第五列
df['depart_port'] = df['depart_port'].replace(['yangshan', 'waigaoqiao'], 'shanghai')
df['arrival_port'] = df['arrival_port'].replace(['yangshan', 'waigaoqiao'], 'shanghai')

# 保存修改后的数据到新的 CSV 文件
df.to_csv("modified_filtered_ship_routes_20km.csv", index=False)
