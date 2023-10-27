#这个代码是用来计算每个港口的船舶访问量
#逻辑较为简单

import pandas as pd

# 读取数据
file_path = "filtered_ship_routes_20km.csv"
df = pd.read_csv(file_path)

# 初始化一个字典来存放所有港口的次数
all_ports_counts = {}

# 对每一个imo进行处理
for imo in df['imo'].unique():
    # 选取当前imo的所有数据
    sub_df = df[df['imo'] == imo]
    
    # 获取航线的港口列表
    ports = [sub_df.iloc[0]['depart_port']]
    for idx, row in sub_df.iterrows():
        if row['arrival_port'] != ports[-1]:
            ports.append(row['arrival_port'])

    # 对当前imo的所有港口进行计数
    imo_ports_counts = {}
    for port in ports:
        if port in imo_ports_counts:
            imo_ports_counts[port] += 1
        else:
            imo_ports_counts[port] = 1

    # 将当前imo的港口计数累加到总计数中
    for port, count in imo_ports_counts.items():
        if port in all_ports_counts:
            all_ports_counts[port] += count
        else:
            all_ports_counts[port] = count

# 将结果转换为DataFrame并保存为新的CSV文件
result_df = pd.DataFrame(list(all_ports_counts.items()), columns=['Port', 'Count'])
result_df.to_csv("port_counts_20km.csv", index=False)
