#这部分代码是为了删除所有上下游港口一致的数据
#这样就避免了所有的交通拥堵造成的误判

import pandas as pd

# 读取数据
file_path = "ship_routes_175km.csv"
df = pd.read_csv(file_path)

# 筛选出depart_port和arrival_port不一样的数据行，并且imo不为0
filtered_df = df[(df['depart_port'] != df['arrival_port']) & (df['imo'] != 0)]

# 保存结果到新文件
filtered_df.to_csv("filtered_ship_routes_20km.csv", index=False)
