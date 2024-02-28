def move_rule(max_index, around_points, current_index, map_size):
    """
    根据移动规则确定下一步的索引位置。

    参数：
        max_index: int
        最大索引，用于指示当前点的索引位置。
        around_points: list
        周围点的信息，包括位置和状态。
        current_index: tuple
        当前点的索引。
        map_size: int
        地图的大小。

    返回值：
        index: int
        根据移动规则确定的下一步的索引位置。
    """
    # 默认情况下保持当前位置
    index = max_index

    # 检查左下方非空 && 下方非空 && 左侧为空
    if around_points[6].x1 != 100 and around_points[7].x1 != 100 and around_points[3].x1 == 100:
        index = 4

    # 检查左上方非空 && 上方非空 && 左侧为空
    elif around_points[0].x1 != 100 and around_points[1].x1 != 100 and around_points[3].x1 == 100:
        index = 4

    # 检查右下角非空 && 右方为空 
    elif around_points[7].x1 != 100 and around_points[4].x1 == 100:
        index = 5

    # 检查左方非空 && 左下方非空 && 下方是为空
    elif around_points[3].x1 != 100 and around_points[5].x1 != 100 and around_points[6].x1 == 100:
        index = 7

    # 检查左方非空 && 左下方非空 && 下方非空 && 右方为空
    elif around_points[3].x1 != 100 and around_points[5].x1 != 100 and around_points[6].x1 != 100 and around_points[7].x1 == 100:
        index = 5

    # 检查左方非空 && 下方为空
    elif around_points[3].x1 != 100 and around_points[6].x1 == 100:
        index = 7

    # 检查右方非空 && 下方为空
    elif around_points[4].x1 != 100 and around_points[6].x1 == 100:
        index = 7

    # 检查左下方非空 && 下方非空 && 左侧为空
    elif around_points[0].x1 != 100 and around_points[3].x1 != 100 and around_points[7].x1 == 100:
        index = 7

    # 丁字路口处理
    if around_points[0].x1 != 100 and around_points[3].x1 != 100 and around_points[5].x1 != 100 \
            and around_points[1].x1 == 100 and around_points[6].x1 == 100:
        if current_index[0] == map_size or current_index[0] == 0:
            if current_index[1] >= map_size / 2:
                index = 2
            else:
                index = 7

    return index

# 测试示例
if __name__ == "__main__":
    class Point:
        def __init__(self, x1):
            self.x1 = x1

    # 创建周围点的信息，包括位置和状态
    around_points = [Point(1) for _ in range(9)]
    around_points[6].x1 = 100

    # 设定当前点的索引和地图大小
    current_index = (3, 3)
    map_size = 10

    # 测试移动规则
    next_index = move_rule(8, around_points, current_index, map_size)
    print("根据移动规则确定的下一步索引位置：", next_index)
