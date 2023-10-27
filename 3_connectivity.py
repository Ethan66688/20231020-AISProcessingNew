#这个代码是提取每个港口作为上游港、下游港的时候连接的国家总数
#注意一个国家只计一次

import pandas as pd

df = pd.read_csv('modified_filtered_ship_routes_20km.csv') 

# 从出发港和到达港中提取所有唯一的港口
all_ports = pd.concat([df['depart_port'], df['arrival_port']]).unique()

# 创建一个字典来存储每个港口能通往的国家数量
port_to_countries = {}

for port in all_ports:
    # 找到该港口作为出发港的所有到达国家
    depart_countries = df[df['depart_port'] == port]['arrival_country'].unique()
    
    # 找到该港口作为到达港的所有出发国家
    arrival_countries = df[df['arrival_port'] == port]['depart_country'].unique()
    
    # 合并这两个列表并找到所有唯一的国家
    unique_countries = pd.concat([pd.Series(depart_countries), pd.Series(arrival_countries)]).unique()
    
    # 将结果存储到字典中
    port_to_countries[port] = len(unique_countries)

# 转换字典到DataFrame
result_df = pd.DataFrame(list(port_to_countries.items()), columns=['Port', 'Number of Unique Countries'])

# 将结果保存到CSV文件中
result_df.to_csv('port_to_countries_count_20km.csv', index=False)

print("Results have been saved to 'port_to_countries_count.csv'.")
