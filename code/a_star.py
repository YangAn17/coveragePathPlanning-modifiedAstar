import math
from is_obstacle import is_obstacle
from in_map import in_map
from a_star_function import a_star_function
from Point import Point

def a_star(current_point, points, obstacles):
    count = 0
    current = Point()       # 初始化返回点
    target_point = Point()  # 初始化目标点
    around_points = []      # 初始化周围点
    last_position = [0, 0]  # 初始化最后的位置

    path = [current_point]  # 将当前点添加到路径中
    min_dis = len(points)**2  # 初始化当前点到目标点的最小距离
    current_point.covered = True  # 将Agent当前点的covered设置为1（表示已覆盖）
    points[current_point.position[0]][current_point.position[1]].covered = True  # 将Map当前点的covered设置为1（表示已覆盖）

    # 找到最近的未覆盖点作为目标点
    for i in range(len(points[0])):
        for j in range(len(points[1])):
            if not is_obstacle(points[i][j].position, obstacles) and points[i][j].covered == 0:
                dis = math.sqrt((current_point.position[0] - points[i][j].position[0])**2 +
                                (current_point.position[1] - points[i][j].position[1])**2)
                if dis < min_dis:
                    min_dis = dis
                    target_point = points[i][j]

    print("find a target [{}, {}], try to fetch...".format(target_point.position[0], target_point.position[1]))

    while True:
        # 检查当前点周围的八个点是否可达
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if in_map([current_point.position[0] + i, current_point.position[1] + j], len(points)):
                    if not is_obstacle([current_point.position[0] + i, current_point.position[1] + j], obstacles):
                        around_points.append(points[current_point.position[0] + i][current_point.position[1] + j])

        if around_points:
            # 找到最小代价的点
            f_min = a_star_function(current_point.position, around_points[0].position, target_point.position)
            min_index = 0
            for i in range(1, len(around_points)):
                f = a_star_function(current_point.position, around_points[i].position, target_point.position)
                if f < f_min:
                    f_min = f
                    min_index = i

            last_position = current_point.position
            current_point = around_points[min_index]
            current_point.covered = True
            points[current_point.position[0]][current_point.position[1]].covered = True
            path.append(current_point)
            print("choose [{}, {}] as next point".format(current_point.position[0], current_point.position[1]))
        else:
            print("around points are all unaccessible")
            break

        around_points.clear()
        count += 1

        if count == 3000:
            current = current_point
            print("time is up, fail to arrive target")
            break

        if current_point.position == target_point.position:
            current = target_point
            print("arrive target")
            break

    return path, current

# 测试示例
if __name__ == "__main__":
    from Point import Point
    # 定义障碍物
    obstacles = [[2, 3, 1, 1], [3, 4, 1, 2], [4, 5, 2, 1]]  # 障碍物的位置坐标

    # 定义地图点
    points = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(Point([i, j]))  # 初始化所有点未覆盖
        points.append(row)

    # 定义起点
    start_point = Point([2, 2])

    # 调用 A* 算法函数
    path, current = a_star(start_point, points, obstacles)

    # 打印路径
    print("Path:")
    for point in path:
        print(point.position)
