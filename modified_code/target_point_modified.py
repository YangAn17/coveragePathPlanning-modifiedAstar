import math

def target_point(x, y, number, path):
    """
    根据当前位置和路径信息计算目标点的函数

    参数：
    x : float
        当前位置的横坐标
    y : float
        当前位置的纵坐标
    number : int
        当前路径点的编号
        path : list
    包含路径点信息的列表

    返回：
    Target_x : float
        目标点的横坐标
    Target_y : float
        目标点的纵坐标
    number : int
        更新后的路径点编号
    """

    ### 该目标点更新是在连续空间进行，注意索引和map_size计算 ###
    if number <= len(path) + 2:
        Cover_x = path[number - 1].position[0] + 0.5 - x    # 0.5是为了让目标点在路径点的中心, 但是不能适应所有情况  
        Cover_y = path[number - 1].position[1] + 0.5 - y

        # 如果当前位置到目标点的距离小于0.1，就更新目标点
        if math.sqrt(Cover_x**2 + Cover_y**2) < 0.1:
            number += 1

        Cover_Th = math.atan2(Cover_y, Cover_x)      
        Target_x = 1 * math.cos(Cover_Th)   # 默认1是栅格的大小
        Target_y = 1 * math.sin(Cover_Th)
    else:
        Target_x = 0
        Target_y = 0

    return Target_x, Target_y, number


# 测试示例
if __name__ == "__main__":
    import sys
    sys.path.append('./code')
    
    from Point import Point as PathPoint
    # 构造路径信息
    path = [PathPoint([1, 2]), PathPoint([3, 4]), PathPoint([5, 6])]
    # 当前位置
    x, y = 0, 0
    # 当前路径点编号
    number = 1
    # 路径长度
    Path_length = len(path)

    # 计算目标点
    Target_x, Target_y, number = target_point(x, y, number, path)
    print("目标点坐标：", Target_x, Target_y)
    print("更新后的路径点编号：", number)
