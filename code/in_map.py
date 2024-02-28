def in_map(point, map_size):
    """
    检查点是否在地图边界内
    
    参数：
    point : list
        点的坐标 [x, y]
    map_size : int
        地图边界大小
    
    返回：
    bool
        如果点在地图边界内返回 True，否则返回 False
    """
    x, y = point
    if x >= 1 and y >= 1 and x <= map_size and y <= map_size:
        return True  # 在地图边界内
    else:
        return False  # 不在地图边界内

# 测试示例
if __name__ == "__main__":
    map_size = 10  # 地图边界大小
    point1 = [5, 5]  # 在地图边界内
    point2 = [11, 7]  # 不在地图边界内

    print(in_map(point1, map_size))  # True
    print(in_map(point2, map_size))  # False
