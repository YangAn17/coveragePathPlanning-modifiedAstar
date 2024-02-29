import math

def point_parameter(path, points, map_size):
    """
    计算路径的各种参数，包括路径长度、转弯次数和重复率。

    参数：
    path: list of lists
        包含路径点的列表。
    points: list of lists
        包含地图点信息的二维列表。
    map_size: int
        地图的大小。

    返回值：
    nice_path: int
        最优决策路径的数量，即重复率为0的路径的数量。
    path_length: int
        路径长度。
    turn_number: int
        转弯次数。
    """
    path_length = 0
    last_direction_flag = 0 # 上一个时刻的运行方向索引
    turn_number = 0
    nice_path = 0

    # 计算路径长度和转弯次数
    for i in range(len(path) - 1):
        x_diff = path[i + 1].position[0] - path[i].position[0]
        y_diff = path[i + 1].position[1] - path[i].position[1]
        path_length += math.sqrt(x_diff ** 2 + y_diff ** 2)
        
        now_direction_flag = math.atan2(x_diff, y_diff)
        if last_direction_flag != now_direction_flag:
            turn_number += 1
        last_direction_flag = now_direction_flag

    # 计算最优路径数量
    for x in range(map_size):
        for y in range(map_size):
            if points[x][y].x1 == 100:
                nice_path += 1

    # 输出路径信息
    print("Nice path =", nice_path)
    print("Path length =", path_length)
    print("Turn number =", turn_number)
    if nice_path == 0:
        print("Repeat rate =", 1)
    else:
        print("Repeat rate =", (path_length - nice_path) / nice_path)

    return nice_path, path_length, turn_number

# 测试示例
if __name__ == "__main__":
    from Point import Point
    # 创建一个包含路径点的列表
    path = [Point([0, 0]), Point([0, 1]), Point([1, 1]), Point([1, 2]), Point([2, 2])]
    # 创建一个包含地图点信息的二维列表
    points = [[Point([0, 0]) for _ in range(5)] for _ in range(5)]
    # 设置地图的大小
    map_size = 5

    # 调用函数计算路径参数
    nice_path, path_length, turn_number = point_parameter(path, points, map_size)
