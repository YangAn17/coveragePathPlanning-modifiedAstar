import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_rec_animation(map_size, obstacles, path):
    """
    绘制栅格地图的边线、障碍物和动态输出路径点。

    参数：
    map_size : int
        地图大小
    obstacles : list
        障碍物信息，二维数组，每行代表一个障碍物，列包括[x, y, length, width]
    path : list
        包含路径点信息的列表

    返回：
    无
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # 绘制栅格地图的边线
    ax.plot([0, map_size + 1], [0, 0], color='black')  # 下边线
    ax.plot([0, map_size + 1], [map_size + 1, map_size + 1], color='black')  # 上边线
    ax.plot([0, 0], [0, map_size + 1], color='black')  # 左边线
    ax.plot([map_size + 1, map_size + 1], [0, map_size + 1], color='black')  # 右边线

    # 绘制障碍物
    for obstacle in obstacles:
        x, y, x1, y1 = obstacle
        rect = patches.Rectangle((x, y), x1 - x,  y1 - y, edgecolor='k', facecolor='k')
        ax.add_patch(rect)

    # 绘制路径
    for i in range(len(path) - 1):
        ax.arrow(path[i].position[0], path[i].position[1],
                 path[i + 1].position[0] - path[i].position[0],
                 path[i + 1].position[1] - path[i].position[1],
                 head_width=0.3, head_length=0.3, fc='g', ec='g')
        plt.pause(0.5)
        plt.draw()

    # 动态输出路径点
    for point in path:
        rect_center = patches.Rectangle((point.position[0] + 0.25, point.position[1] + 0.25), 0.5, 0.5,
                                        edgecolor='r', facecolor='r')
        ax.add_patch(rect_center)
        plt.pause(0.1)
        plt.draw()

    plt.show()

# 测试示例
if __name__ == "__main__":
    from map import map_read
    from Point import Point

    # 定义地图大小
    map_size = 81

    # 定义障碍物
    obstacles = map_read(map_size, './data/obstacles_zq.csv')

    # 生成示例路径
    path = [Point((1, 1)), Point((2, 2)), Point((3, 3))]

    # 绘制栅格地图的边线、障碍物和动态输出路径点
    draw_rec_animation(map_size, obstacles, path)
