def is_obstacle(position, obstacles):
    """
    检查给定位置是否处于障碍物范围内
    
    参数：
    position : list
        当前点坐标 [x, y]
    obstacles : list of lists
        障碍物信息，每个障碍物是一个列表 [x, y, length, width]
    
    返回：
    bool
        如果在障碍物范围内返回 True，否则返回 False
    """
    for obstacle in obstacles:
        x , y = position[0] + 0.5, position[1] + 0.5  # 以点的中心为坐标(离散空间换算到连续空间)
        obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2 = obstacle
        if x >= obstacle_x1 and y >= obstacle_y1 and x <= obstacle_x2 and y <= obstacle_y2:
            return True  # 在障碍物范围内
    return False  # 不在障碍物范围内

# 测试示例
if __name__ == "__main__":
    obstacles = [[1, 1, 3, 2], [10, 8, 3, 2]]  # 障碍物信息
    position1 = [1, 1]      # 在第一个障碍物范围内
    position2 = [0, 0]      # 在第一个障碍物范围内
    position3 = [3, 2]      # 不在任何障碍物范围内

    print(is_obstacle(position1, obstacles))  # True
    print(is_obstacle(position2, obstacles))  # True
    print(is_obstacle(position3, obstacles))  # False
