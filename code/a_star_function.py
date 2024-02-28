import math

def a_star_function(point1, point2, target_point):
    """
    计算 A* 算法的代价函数值
    
    参数：
    point1 : list
        当前点的坐标 [x, y]
    point2 : list
        当前点附近的周围点的坐标 [x, y]
    target_point : list
        目标点的坐标 [x, y]
    
    返回：
    f : float
        A* 算法的代价函数值
    """
    # 计算当前点到当前周围点的距离
    g = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    # 计算当前周围点到目标点的距离
    h = math.sqrt((point2[0] - target_point[0])**2 + (point2[1] - target_point[1])**2)
    # 计算 A* 算法的代价函数值
    f = g + h
    return f

# 测试示例
if __name__ == "__main__":
    point1 = [1, 1]  # 当前点的坐标
    point2 = [3, 4]  # 当前周围点的坐标
    target_point = [10, 10]  # 目标点的坐标

    print(a_star_function(point1, point2, target_point))  # 输出 A* 算法的代价函数值
