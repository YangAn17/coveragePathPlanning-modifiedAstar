import numpy as np

def repulsion(n, x, y, X, Y, r, R, g2, g3, d, t):
    """
    计算无人机受到的斥力，以避免与其他无人机和墙壁碰撞。

    参数：
    n: int
        无人机数量。
    x, y: double
        当前无人机的坐标。
    X, Y: list
        所有无人机的坐标列表。
    r: double 
        无人机距离地图边缘的最小距离。
    R: douoble
        无人机之间的最小距离。
    g2: double
        与墙壁碰撞斥力系数。
    g3: double
        与其他无人机碰撞斥力系数。
    d: 
        地图的大小。
    t: double
        时间参数，用于判断是否进行碰撞避免计算。

    返回值：
    vxrepulsion, vyrepulsion: double
        无人机受到的斥力在横向和纵向上的分量。
    """
    vxcol0 = np.zeros(n)  # 无人机与无人机斥力在横坐标的分量
    vycol0 = np.zeros(n)  # 无人机与无人机斥力在纵坐标的分量
    vxwall, vywall = 0, 0  # 无人机与墙壁斥力在横纵坐标的分量

    # 避免无人机与无人机碰撞速度（采用半弹簧方法）
    for i in range(n):
        if np.sqrt((x - X[i]) ** 2 + (y - Y[i]) ** 2) < R and (x - X[i]) != 0 and (y - Y[i]) != 0:
            threp = np.arctan2(y - Y[i], x - X[i])
            vxcol0[i] = g3 * np.cos(threp) * (R - np.sqrt((x - X[i]) ** 2 + (y - Y[i]) ** 2))
            vycol0[i] = g3 * np.sin(threp) * (R - np.sqrt((x - X[i]) ** 2 + (y - Y[i]) ** 2))

    vxcol, vycol = np.sum(vxcol0), np.sum(vycol0)
    dv = np.sqrt(vxcol ** 2 + vycol ** 2)

    # 避免无人机与墙壁碰撞速度（采用半弹簧方法）
    if dv == 0:
        vxwall, vywall = 0, 0
    else:
        if x < r:
            vxwall = g2 * (r - x)
        elif x > (d - r):
            vxwall = g2 * (d - r - x)
        if y < r:
            vywall = g2 * (r - y)
        elif y > (d - r):
            vywall = g2 * (d - r - y)

    # 无人机避免碰撞速度和
    if t == 0:
        vxrepulsion, vyrepulsion = 0, 0
    else:
        vxrepulsion, vyrepulsion = vxcol + vxwall, vycol + vywall

    return vxrepulsion, vyrepulsion

# 测试示例
if __name__ == "__main__":
    n = 3  # 无人机数量
    x, y = 0.15, 0.3  # 当前无人机坐标
    X = [0.5, 3, 4]  # 其他无人机横坐标
    Y = [0.5, 4, 5]  # 其他无人机纵坐标
    r = 1  # 无人机距离地图边缘的最小距离
    R = 1  # 无人机之间的最小距离
    g2 = 0.1  # 与墙壁碰撞斥力系数
    g3 = 0.2  # 与其他无人机碰撞斥力系数
    d = 10  # 地图大小
    t = 1  # 时间参数

    # 计算无人机受到的斥力
    vxrepulsion, vyrepulsion = repulsion(n, x, y, X, Y, r, R, g2, g3, d, t)
    print("无人机受到的斥力：", "{:.6f}".format(vxrepulsion), "{:.6f}".format(vyrepulsion))
