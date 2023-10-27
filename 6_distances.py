
import pandas as pd
import math

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine公式 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r

# 读取数据
ship_routes = pd.read_csv("modified_filtered_ship_routes_20km.csv")
port_data = pd.read_csv("data_port.csv")


# 创建一个新列来存放距离
ship_routes["distance"] = 0.0

for index, row in ship_routes.iterrows():
    depart_lat = port_data[port_data["port"] == row["depart_port"]]["latitudeDecimal"].values[0]
    depart_lon = port_data[port_data["port"] == row["depart_port"]]["longitudeDecimal"].values[0]
    filtered_data = port_data[port_data["port"] == row["arrival_port"]]
    if not filtered_data.empty:
        arrival_lat = filtered_data["latitudeDecimal"].values[0]
    else:
        print(f"Warning: Port {row['arrival_port']} not found in port_data.")
        continue

    arrival_lat = port_data[port_data["port"] == row["arrival_port"]]["latitudeDecimal"].values[0]
    arrival_lon = port_data[port_data["port"] == row["arrival_port"]]["longitudeDecimal"].values[0]
    ship_routes.at[index, "distance"] = haversine(depart_lon, depart_lat, arrival_lon, arrival_lat)

# 输出到新的CSV文件
ship_routes.to_csv("output_ship_routes_with_distance.csv", index=False)
