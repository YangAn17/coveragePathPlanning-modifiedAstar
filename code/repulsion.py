import numpy as np

def repulsion(number_uav, x_current, y_current, X_uavs, Y_uavs, r_wall, R_uav, g2, g3, map_size, t):
    """
    计算无人机受到的斥力，以避免与其他无人机和墙壁碰撞。

    参数：
    number_uav: int
        无人机数量。
    x_current, y_current: float
        当前无人机的坐标。
    X_uavs, Y_uavs: list
        所有无人机的坐标列表。
    r_wall: float 
        无人机距离地图边缘的最小距离。
    R_uav: douoble
        无人机之间的最小距离。
    g2: float
        与墙壁碰撞斥力系数。
    g3: float
        与其他无人机碰撞斥力系数。
    mao_size: int
        地图的大小。
    t: float
        时间参数，用于判断是否进行碰撞避免计算。

    返回值：
    vxrepulsion, vyrepulsion: float
        无人机受到的斥力在横向和纵向上的分量。
    """
    vxcol0 = np.zeros(number_uav)  # 无人机与无人机斥力在横坐标的分量
    vycol0 = np.zeros(number_uav)  # 无人机与无人机斥力在纵坐标的分量
    vxwall, vywall = 0, 0  # 无人机与墙壁斥力在横纵坐标的分量

    # 避免无人机与无人机碰撞速度（采用半弹簧方法）
    for i in range(number_uav):
        # 计算无人机与无人机之间的距离
        distance_uavs = np.sqrt((x_current - X_uavs[i]) ** 2 + (y_current - Y_uavs[i]) ** 2)
        if distance_uavs < R_uav and (x_current - X_uavs[i]) != 0 and (y_current - Y_uavs[i]) != 0:
            threp = np.arctan2(y_current - Y_uavs[i], x_current - X_uavs[i])
            vxcol0[i] = g3 * np.cos(threp) * (R_uav - distance_uavs)
            vycol0[i] = g3 * np.sin(threp) * (R_uav - distance_uavs)

    vxcol, vycol = np.sum(vxcol0), np.sum(vycol0)
    dv = np.sqrt(vxcol ** 2 + vycol ** 2)

    # 避免无人机与墙壁碰撞速度（采用半弹簧方法）
    ### wall避碰是在连续空间进行，注意索引和map_size计算 ###
    if dv == 0:
        vxwall, vywall = 0, 0
    else:
        if x_current < r_wall:
            vxwall = g2 * (r_wall - x_current)
        elif x_current > (map_size - r_wall):
            vxwall = g2 * (map_size - r_wall - x_current)
        if y_current < r_wall:
            vywall = g2 * (r_wall - y_current)
        elif y_current > (map_size - r_wall):
            vywall = g2 * (map_size - r_wall - y_current)

    # 无人机避免碰撞速度和
    if t == 0:
        vxrepulsion, vyrepulsion = 0, 0
    else:
        vxrepulsion, vyrepulsion = vxcol + vxwall, vycol + vywall

    return vxrepulsion, vyrepulsion

# 测试示例
if __name__ == "__main__":
    n = 3  # 无人机数量
    x, y = 0.3, 0.3  # 当前无人机坐标
    X = [0.5, 3, 4]  # 其他无人机横坐标
    Y = [0.4, 4, 5]  # 其他无人机纵坐标
    r = 1  # 无人机距离地图边缘的最小距离
    R = 1  # 无人机之间的最小距离
    g2 = 0.1  # 与墙壁碰撞斥力系数
    g3 = 0.2  # 与其他无人机碰撞斥力系数
    d = 10  # 地图大小
    t = 1  # 时间参数

    # 计算无人机受到的斥力
    vxrepulsion, vyrepulsion = repulsion(n, x, y, X, Y, r, R, g2, g3, d, t)
    print("无人机受到的斥力：", "{:.6f}".format(vxrepulsion), "{:.6f}".format(vyrepulsion))
