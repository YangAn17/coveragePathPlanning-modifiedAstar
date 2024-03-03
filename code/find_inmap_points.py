from Point import Point
from in_map import in_map

def find_inmap_points(current_point, points):
    """
    查找当前点周围存在的点
    
    参数：
    current_point : Point
        当前点对象
    points : list of list of Point
        表示地图上的所有点
    
    返回：
    around_flag : list
        周围可达点的状态数组，1表示可到达，0表示不可到达
    around_points : list of Point
        当前点周围可达的点列表
    """
    # around_points = [Point() for i in range(8)]  # 初始化周围可达的点列表
    # 运行方向的索引位置
    # | 2 | 4 | 7 |
    # | 1 | # | 6 |
    # | 0 | 3 | 5 |
    around_points = []  # 初始化周围可达的点列表
    around_flag = [0] * 8   # 初始化周围可达点的状态数组
    index = 0   # 初始化索引位置
    for i in range(-1, 2):
        for j in range(-1, 2):
            # 跳过当前点本身
            if i == 0 and j == 0:
                continue
            # 计算周围点坐标
            x = current_point.position[0] + i
            y = current_point.position[1] + j
            # 判断周围点是否在地图内
            if in_map([x, y], len(points)):
                around_points.append(points[x][y])
                around_flag[index] = 1
            index += 1
    
    return around_flag, around_points

# 测试示例
if __name__ == "__main__":
    from Point import Point

    map_size = 5
    # 定义地图点
    points = []
    for i in range(map_size):
        row = []
        for j in range(map_size):
            row.append(Point([i, j]))  # 初始化所有点未覆盖
        points.append(row)

    # 定义起点
    start_point = Point([4, 4])

    # 获取当前点周围可达的点及其状态数组
    around_flag, around_points = find_inmap_points(start_point, points)
    print("周围可达点状态数组：", around_flag)
    print("周围可达点：", [p.position for p in around_points])
