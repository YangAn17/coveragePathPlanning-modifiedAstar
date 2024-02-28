def is_obstacle(position, obstacles):
    """
    检查给定位置是否处于障碍物范围内
    
    参数：
    position : list
        当前点的二维数组坐标 [x, y]
    obstacles : list of lists
        障碍物信息，每个障碍物是一个列表 [x, y, length, width]
    
    返回：
    bool
        如果在障碍物范围内返回 True，否则返回 False
    """
    for obstacle in obstacles:
        x, y = position
        obstacle_x, obstacle_y, length, width = obstacle
        if x >= obstacle_x and y >= obstacle_y and x < obstacle_x + length and y < obstacle_y + width:
            return True  # 在障碍物范围内
    return False  # 不在障碍物范围内

# 测试示例
if __name__ == "__main__":
    obstacles = [[1, 1, 3, 2], [5, 3, 2, 4], [10, 8, 3, 2]]  # 障碍物信息
    position1 = [2, 2]  # 在第一个障碍物范围内
    position2 = [5, 4]  # 在第二个障碍物范围内
    position3 = [7, 7]  # 不在任何障碍物范围内

    print(is_obstacle(position1, obstacles))  # True
    print(is_obstacle(position2, obstacles))  # True
    print(is_obstacle(position3, obstacles))  # False
