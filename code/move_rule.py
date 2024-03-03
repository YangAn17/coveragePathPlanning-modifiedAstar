def move_rule(current_index, around_points, current_postion, map_size):
    """
    根据移动规则确定下一步的索引位置。

    参数：
    current_index: int
        当前运动方向索引。
    around_points: list
        周围点的信息，包括位置和状态。
    current_postion: tuple
        当前点的位置。
    map_size: int
        地图的大小。

    返回值：
    index: int
        根据移动规则确定的下一步的索引位置。
    """

    # 运行方向的索引位置
    # | 2 | 4 | 7 |
    # | 1 | # | 6 |
    # | 0 | 3 | 5 |
    # 默认情况下保持当前运动方向
    index = current_index

    # 100 表示未覆盖，0 表示已覆盖 -100表示障碍物
    # 检查下方非空 && 右下方非空 && 左侧为空
    if around_points[3].x1 != 100 and around_points[5].x1 != 100 and around_points[1].x1 == 100:
        index = 1

    # 检查左上方非空 && 上方非空 && 左侧为空
    elif around_points[2].x1 != 100 and around_points[4].x1 != 100 and around_points[1].x1 == 100:
        index = 1

    # 检查右下角非空 && 右方为空 
    elif around_points[5].x1 != 100 and around_points[6].x1 == 100:
        index = 6

    # 检查左方非空 && 左下方非空 && 下方是为空
    elif around_points[1].x1 != 100 and around_points[0].x1 != 100 and around_points[3].x1 == 100:
        index = 3

    # 检查左方非空 && 左下方非空 && 下方非空 && 右方为空
    elif around_points[1].x1 != 100 and around_points[0].x1 != 100 and around_points[3].x1 != 100 and around_points[6].x1 == 100:
        index = 6

    # 检查左方非空 && 下方为空
    elif around_points[1].x1 != 100 and around_points[3].x1 == 100:
        index = 3

    # 检查右方非空 && 下方为空
    elif around_points[6].x1 != 100 and around_points[3].x1 == 100:
        index = 3

    # 检查左下方非空 && 下方非空 && 左侧为空
    elif around_points[0].x1 != 100 and around_points[3].x1 != 100 and around_points[1].x1 == 100:
        index = 1

    # 丁字路口处理
    ### 丁字路口处理在离散空间进行，注意索引和map_size计算 ###
    if around_points[0].x1 != 100 and around_points[3].x1 != 100 and around_points[5].x1 != 100 \
            and around_points[1].x1 == 100 and around_points[6].x1 == 100:
        if current_postion[0] == (map_size - 1) or current_postion[0] == 0: 
            if current_postion[1] >= (map_size - 1) / 2:
                index = 4
            else:
                index = 3

    return index

# 测试示例
if __name__ == "__main__":
    class Point:
        def __init__(self, x1):
            self.x1 = x1

    # 创建周围点的信息，包括位置和状态
    around_points = [Point(0) for _ in range(9)]
    around_points[6].x1 = 100

    # 设定当前点的位置和地图大小
    current_postion = (10, 10)
    map_size = 10

    # 测试移动规则
    next_index = move_rule(8, around_points, current_postion, map_size)
    print("根据移动规则确定的下一步索引位置：", next_index)
