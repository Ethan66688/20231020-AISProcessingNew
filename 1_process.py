#此代码为最关键的部分，即船舶停泊的判断
#采用了haversine函数遍历处理，每种情况搜索的均为距离最近的港口

import pandas as pd
from haversine import haversine

#首先要将原数据中速度大于1的部分进行清理
ais_data_file = "container_ais_202001.csv"
ais_data = pd.read_csv(ais_data_file, sep="|", header=0)
ais_data = ais_data[ais_data['speed'] <= 1]
ais_data.to_csv("processed_ais_data_202001.csv", sep=",", index=False)

ais_data_file = "processed_ais_data_202001.csv"
ais_data = pd.read_csv(ais_data_file, sep=",", header=0)
print(ais_data.columns)

# 将timestamp转为日期时间格式
ais_data['timestamp'] = pd.to_datetime(ais_data['timestamp'])
print(ais_data.columns)

# 读取港口数据文件
port_data_file = "data_port.csv"
port_data = pd.read_csv(port_data_file, header=0)
port_data.columns = ["id", "port", "country_name", "latitudeDecimal", "longitudeDecimal"]

# 定义计算港口与船舶之间的距离的函数
def filter_port_visits(row):
    imo, timestamp, latitude, longitude = row[0], row[1], row[2], row[3]

    port_distances = []

    for port_row in port_data.itertuples(index=False):
        port_id, port_name, country_name, port_latitude, port_longitude = port_row[0], port_row[1], port_row[2], port_row[3], port_row[4]
        distance = haversine((latitude, longitude), (port_latitude, port_longitude))
        port_distances.append((port_id, port_name, country_name, distance, port_latitude, port_longitude))
    
    # 获取距离最近的港口
    closest_port = min(port_distances, key=lambda x: x[3])

    # 如果距离小于或等于30km，则判断为船舶进入港口
    if closest_port[3] <= 17.5:
        return imo, latitude, longitude, closest_port[0], closest_port[1], closest_port[2], timestamp, closest_port[4], closest_port[5], distance
    else:
        return None

# 过滤与港口距离小于或等于30km的记录
port_visits = [filter_port_visits(row) for row in ais_data.itertuples(index=False) if filter_port_visits(row) is not None]

# 保存港口访问数据
port_visits_df = pd.DataFrame(port_visits, columns=["imo", "latitude","longitude","port_id", "port_name", "country_name", "timestamp", "port_latitude", "port_longitude","distance"])
port_visits_df.to_csv("ship_port_visits_20km.csv", sep=",", index=False)
