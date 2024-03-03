import math
import numpy as np
from Point import Point
from a_star import a_star
from move_rule import move_rule
from is_obstacle import is_obstacle
from all_covered import all_covered
from find_inmap_points import find_inmap_points

def binn(map_size, obstacles):
    """
    实现二进制网络的覆盖路径规划算法。

    参数：
    map_size : int
        地图大小
    obstacles : list
        障碍物信息，二维数组，每行代表一个障碍物，列包括[x, y, length, width]

    返回：
    points : list
        包含地图上所有点信息的二维数组
    path : list
        覆盖路径的点序列
    """
    # 初始化函数所用变量
    points = [[Point() for _ in range(map_size)] for _ in range(map_size)]  # 初始化map

    around_points = []          # 用于存储当前点周围的点
    path = []                   # 用于存储覆盖路径的点序列
    count = 0                   # 用于限制最大循环次数
    around_covered = 1          # 用于检查当前点是否被完全围绕的标志位
    around_flag = [0] * 8       # 用于检查周围8个点是否可通行

    # 设置起始点坐标
    # 如果进行多机协同覆盖，应设置多个起始点
    current_index = [0, 0]

    # 根据障碍物信息将障碍物点标记为已覆盖
    for i in range(map_size):
        for j in range(map_size):
            points[i][j].position = [i, j]
            if is_obstacle(points[i][j].position, obstacles):
                points[i][j].covered = 1

    # 将起始点标记为已覆盖
    points[current_index[0]][current_index[1]].covered = 1

    # 将起始点加入覆盖路径
    path.append(points[current_index[0]][current_index[1]])

    while True:
        # 检查当前点周围的8个点是否存在        
        # 运行方向的索引位置
        # | 2 | 4 | 7 |
        # | 1 | # | 6 |
        # | 0 | 3 | 5 |
        around_flag, around_points = find_inmap_points(points[current_index[0]][current_index[1]], points)

        # 根据周围点的情况设置x1, x2, x3
        if around_points:
            for point in around_points:
                # x1-表示自身影响值
                if point.covered == 0 and not is_obstacle(point.position, obstacles):
                    point.x1 = 100  # 未覆盖点且不是障碍物
                elif point.covered == 1 and not is_obstacle(point.position, obstacles):
                    point.x1 = 0    # 已覆盖点且不是障碍物
                elif is_obstacle(point.position, obstacles):
                    point.x1 = -100 # 障碍物

                # x2-表示距离效应影响值
                point.x2 = -2 * math.sqrt((point.position[0] - points[current_index[0]][current_index[1]].position[0]) ** 2 +
                                          (point.position[1] - points[current_index[0]][current_index[1]].position[1]) ** 2)
                
                # x3-表示方向效应影响值
                point.x3 = -abs(math.atan2(point.position[1] - points[current_index[0]][current_index[1]].position[1], 
                                        point.position[0] - points[current_index[0]][current_index[1]].position[0]))

                # 检查是否在死区
                if point.x1 == 100:
                    around_covered = 0

        # 根据是否在死区采取不同行动
        if around_covered == 1:
            # 找到 A* 路径并执行移动
            print(f"Trapped at [{current_index[0]}, {current_index[1]}], finding A* path...")
            a_star_path, current = a_star(points[current_index[0]][current_index[1]], points, obstacles)
            for point in a_star_path:
                path.append(point)
                points[point.position[0]][point.position[1]].covered = 1
                points[point.position[0]][point.position[1]].x1 = 100

            current_index[0] = current.position[0] # 为什么要加1
            current_index[1] = current.position[1]
        else:
            # 根据 x1 + x2 + x3 的值选择下一步的移动方向
            print(f"Choosing next move at [{current_index[0]}, {current_index[1]}]...")
            max_sum = around_points[0].x1 + around_points[0].x2 + around_points[0].x3
            max_index = 0
            for i in range(1, len(around_points)):
                if around_points[i].x1 + around_points[i].x2 + around_points[i].x3 >= max_sum:
                    max_sum = around_points[i].x1 + around_points[i].x2 + around_points[i].x3
                    max_index = i

            # 自定义运动规则(初始点8方向均可运动)
            if sum(1 for x in around_flag if x > 0) == 8:
                max_index = move_rule(max_index, around_points, current_index, map_size)

            # 移动到下一个点
            current_index[0] = around_points[max_index].position[0]
            current_index[1] = around_points[max_index].position[1] #？为什么要加1
            points[current_index[0]][current_index[1]].covered = 1
            points[current_index[0]][current_index[1]].x1 = 100
            path.append(points[current_index[0]][current_index[1]])

        around_points = []  # 清空周围点的数据
        count += 1  # 循环次数加1
        around_covered = 1  # 是否在死区的标志位置为0

        # 如果循环次数达到2000，停止覆盖并打印失败信息
        if count == 2000:
            print("Failed to cover the map completely.")
            break

        # 如果所有点都被覆盖，停止循环并打印成功信息
        if all_covered(points):
            print("Coverage Path Planning Succeed!")
            break

    return points, path

if __name__ == "__main__":
    # 定义地图大小
    map_size = 10

    # 定义障碍物
    obstacles = [[2, 2, 2, 2], [5, 5, 2, 2], [7, 7, 2, 2]]

    # 调用binn函数
    points, path = binn(map_size, obstacles)

    # 打印路径
    print("Path:")
    for point in path:
        print(point.position)

    import matplotlib.pyplot as plt

    def visualize_path(points, path):
        # 提取所有覆盖点的坐标
        covered_points = [point.position for point in path]

        # 创建地图
        map_grid = [[0] * len(points) for _ in range(len(points))]

        # 将覆盖点标记为1
        for x, y in covered_points:
            map_grid[x][y] = 1

        # 绘制地图
        plt.imshow(map_grid, cmap='Greys', origin='lower')

        # 绘制路径
        path_x = [point.position[1] for point in path]
        path_y = [point.position[0] for point in path]
        plt.plot(path_x, path_y, marker='o', color='r')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Coverage Path')
        plt.grid(color='b', linestyle='--', linewidth=1)
        plt.show()

    # 调用函数绘制路径
    visualize_path(points, path)
