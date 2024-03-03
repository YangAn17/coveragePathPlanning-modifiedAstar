import matplotlib.pyplot as plt
import numpy as np

def map(map_size, obs_num):
    """
    创建地图并添加障碍物
    
    参数：
    map_size : int
        地图大小（正方形）
    obs_num : int
        障碍物的数量
    
    返回：
    obstacles : list
        包含障碍物坐标的列表
    """
    plt.figure()  # 创建图窗窗口
    plt.box(True)  # 在坐标区周围显示框轮廓

    # 保存障碍物坐标
    # obstacles列表中每个元素的格式为 [left, bottom, right, top]
    obstacles = []

    # 随机生成障碍物（注释掉的部分）
    ### 障碍生成在连续空间中进行，注意索引和map_size计算 ###
    for i in range(obs_num):
        length = np.random.randint(1, 6)
        width = np.random.randint(1, 5)
        x = np.random.randint(0, map_size - length + 1)  # 障碍物的左下角横坐标（保证不超出地图范围）
        y = np.random.randint(0, map_size - width + 1)   # 障碍物的左下角纵坐标（保证不超出地图范围）
        obstacles.append([x, y, x + length, y + width])  # 存入obstacles列表
        plt.Rectangle((x, y), length, width, facecolor=[0.3, 0.3, 0.3])  # 创建一个矩形对象表示障碍物
        plt.gca().add_patch(plt.Rectangle((x, y), length, width, facecolor=[0.3, 0.3, 0.3]))  # 将矩形对象添加到当前图形中显示

    # 手动添加障碍物
    # obstacles.append([0, 5, 2, 7])
    # plt.gca().add_patch(plt.Rectangle((0, 5), 2, 2, facecolor=[0.3, 0.3, 0.3]))
    # obstacles.append([7, 2, 9, 4])
    # plt.gca().add_patch(plt.Rectangle((7, 2), 2, 2, facecolor=[0.3, 0.3, 0.3]))

    # 打印地图的栅格
    for i in range(map_size + 1):
        plt.plot([0, map_size], [i, i], 'k')  # 横向线
        plt.plot([i, i], [0, map_size], 'k')  # 纵向线

    plt.axis('equal')  # 设置x和y轴的刻度一致，保证地图比例尺正确
    plt.show()

    return obstacles

# 测试示例
if __name__ == "__main__":
    obstacles = map(15, 2)
    print("障碍物坐标：", obstacles)
