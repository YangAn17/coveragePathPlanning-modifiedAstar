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
    ### 在地图里判断在离散空间进行，注意索引和map_size计算 ###
    if x >= 0 and y >= 0 and x <= (map_size - 1) and y <= (map_size - 1):
        return True  # 在地图边界内
    else:
        return False  # 不在地图边界内

# 测试示例
if __name__ == "__main__":
    map_size = 10  # 地图边界大小
    point1 = [1, 1]  # 在地图边界内
    point2 = [10, 7]  # 不在地图边界内

    print(in_map(point1, map_size))  # True
    print(in_map(point2, map_size))  # False
