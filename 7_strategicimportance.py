
import pandas as pd

# 读取数据
data = pd.read_csv("output_ship_routes_with_distance.csv")

# 分别从depart_port和arrival_port收集距离
depart_distances = data[['depart_port', 'distance']].rename(columns={'depart_port': 'port'})
arrival_distances = data[['arrival_port', 'distance']].rename(columns={'arrival_port': 'port'})

# 合并这两个数据集，得到每个港口的所有上下游距离
all_distances = pd.concat([depart_distances, arrival_distances], ignore_index=True)

# 计算每个港口的上下游距离的均值
avg_distances = all_distances.groupby('port').mean().reset_index()

# 计算每个港口距离的10%的平均值
def top_10_percent_avg(distances):
    n = len(distances)
    top_10_percent = sorted(distances)[-int(n*0.1):]
    return sum(top_10_percent) / len(top_10_percent)

top_10_avg = all_distances.groupby('port').agg(top_10_percent_avg).reset_index()
top_10_avg.columns = ['port', 'top_10_avg_distance']

# 合并计算结果
final_data = avg_distances.merge(top_10_avg, on='port')
final_data.columns = ['port', 'avg_distance', 'top_10_avg_distance']

# 计算比值
final_data['ratio'] = final_data['top_10_avg_distance'] / final_data['avg_distance']

# 保存到新的CSV文件
final_data.to_csv("port_avg_distances.csv", index=False)

# 提取指定港口的数据
selected_ports = [
    "shanghai", "singapore", "shenzhen", "ningbo", "busan", "sha tin", "qingdao", "tianjin",
    "jebel ali", "rotterdam", "port klang", "antwerp", "kaohsiung", "xiamen", "dalian", "los angeles",
    "tanjung pelepas", "hamburg", "long beach", "keihin", "tanjung priok", "newyork", "colombo",
    "ho chi minh city", "hanshin"
]
selected_data = final_data[final_data['port'].isin(selected_ports)]

# 保存到新的CSV文件
selected_data.to_csv("selected_port_avg_distances.csv", index=False)
