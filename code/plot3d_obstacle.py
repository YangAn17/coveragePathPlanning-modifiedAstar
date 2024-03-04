import numpy as np

def plot3d_obstacle(obstacles, T0):
    """
    根据障碍物的位置绘制3D地图，并将障碍物区域的高度设置为10。

    参数：
    obstacles: list of lists
        包含障碍物坐标的列表。
    T0: list of lists
        二维数组，表示地图的高度。

    返回值：
    co: list
        包含障碍物的 x 轴索引的数组。
    ro: list
        包含障碍物的 y 轴索引的数组。
    T0: ;list of lists
        更新后的地图高度数组。
    """
    co = []
    ro = []

    # 设置障碍物区域的高度
    ### 障碍设置在连续空间中进行，注意索引和map_size计算 ###
    for obs in obstacles:
        x1, y1, x2, y2 = obs
        T0[x1:x2+1, y1:y2+1] = 10   # 设置障碍物区域的高度为10
        co.extend(list(range(x1, x2+1)))
        ro.extend(list(range(y1, y2+1)))

    return co, ro, T0

# 测试示例
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D as ax
    # 创建一个地图并获取障碍物列表和地图高度数组
    map_size = 10
    obstacles = [[0, 2, 1, 3]]
    T0 = np.zeros((map_size + 1, map_size + 1))

    # 调用函数绘制3D地图并更新地图高度
    co, ro, T0 = plot3d_obstacle(obstacles, T0)

    # 创建网格
    X, Y = np.meshgrid(range(map_size + 1), range(map_size + 1))

    # 绘制3D地图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(Y, X, T0, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Height')
    plt.title('3D Obstacle Map')
    plt.show()

    print("障碍物在 x 轴上的索引：", co)
    print("障碍物在 y 轴上的索引：", ro)

