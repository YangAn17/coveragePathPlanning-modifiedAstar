import sys
sys.path.append('./code')

from Point import Point
from is_obstacle import is_obstacle
from in_map import in_map

def find_accessible_points(current_point, points, obstacles):
    """
    查找当前点周围可达的点，并返回可达状态的数组
    
    参数：
    current_point : Point
        当前点对象
    points : list of list of Point
        表示地图上的所有点
    obstacles : list
        障碍物的位置坐标
    
    返回：
    arrund_flag : list
        周围可达点的状态数组，1表示可到达，0表示不可到达
    around_points : list of Point
        当前点周围可达的点列表
    """
    around_points = []  # 初始化周围可达的点列表
    arrund_flag = [0] * 8  # 初始化周围可达点的状态数组
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue    # 跳过当前点本身
            x = current_point.position[0] + i
            y = current_point.position[1] + j
            if in_map([x, y], len(points)) and not is_obstacle([x, y], obstacles):
                around_points.append(points[x][y])
                # 计算索引位置
                if i == -1:
                    if j == -1:
                        index = 6
                    elif j == 0:
                        index = 4
                    else:
                        index = 1
                elif i == 0:
                    if j == -1:
                        index = 7
                    elif j == 1:
                        index = 2
                else:
                    if j == -1:
                        index = 8
                    elif j == 0:
                        index = 5
                    else:
                        index = 3
                arrund_flag[index-1] = 1
    return arrund_flag, around_points

# 测试示例
if __name__ == "__main__":
    # 定义地图点
    points = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(Point([i, j]))  # 初始化所有点未覆盖
        points.append(row)

    # 定义障碍物
    obstacles = [[2, 3, 1, 1], [3, 4, 1, 2], [4, 2, 1, 1]]  # 障碍物的位置坐标

    # 定义起点
    start_point = Point([2, 2])

    # 获取当前点周围可达的点及其状态数组
    arrund_flag, around_points = find_accessible_points(start_point, points, obstacles)
    print("周围可达点状态数组：", arrund_flag)
    print("周围可达点：", [p.position for p in around_points])
