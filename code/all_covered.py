def all_covered(points):
    """
    检查地图上的所有点是否都被覆盖了。

    参数：
        points: list of Point class
        表示地图上的所有点。

    返回值：
        bool: bool
        表示所有点是否都被覆盖了。
    """
    all_covered = True  # 初始化为True，表示所有点都被覆盖了
    for row in points:
        for point in row:
            if point.covered == 0:  # 如果有任何一个点未被覆盖，则将all_covered设置为False
                all_covered = False
                break
        if not all_covered:  # 如果发现未被覆盖的点，直接跳出外层循环
            break
    return all_covered

# 测试示例
if __name__ == "__main__":
    from Point import point
    # 创建一个简单的地图，表示3x3的网格，所有点都被覆盖了
    points_covered = [[point(covered=1) for _ in range(3)] for _ in range(3)]
    print("所有点都被覆盖了：", all_covered(points_covered))

    # 创建一个简单的地图，表示3x3的网格，其中一个点未被覆盖
    points_uncovered = [[point(covered=1) for _ in range(3)] for _ in range(3)]
    points_uncovered[1][1].covered = 0  # 将一个点的covered属性设置为0，表示未被覆盖
    print("存在未被覆盖的点：", all_covered(points_uncovered))
    