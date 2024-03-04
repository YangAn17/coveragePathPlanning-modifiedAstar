import matplotlib.pyplot as plt
import matplotlib.animation as animation

def draw_path_animation(path, map_size):
    """
    绘制路径动画并标记节点和连接线。

    参数：
    path : list
        路径节点的列表，每个节点是一个字典，包含 'position' 键表示节点的位置坐标。
    map_size : int
        地图大小
    
    返回：
    无
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    plt.xlim(0, map_size)  # 根据实际情况调整坐标范围
    plt.ylim(0, map_size)

    def update(frame):
        ax.clear()
        # 绘制节点和连接线
        for i in range(frame + 1):
            # 绘制节点
            ax.add_patch(plt.Rectangle((path[i]['position'][0] + 0.4375, path[i]['position'][1] + 0.4375), 0.125, 0.125,
                                        edgecolor='red', facecolor='red', linewidth=1, alpha=0.6))
            # 绘制连接线
            if i < len(path) - 1:
                ax.plot([path[i]['position'][0] + 0.5, path[i + 1]['position'][0] + 0.5],
                        [path[i]['position'][1] + 0.5, path[i + 1]['position'][1] + 0.5], color='red', linewidth=1, alpha=0.6)

    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=100, repeat=False)
    plt.show()

# 测试示例
if __name__ == "__main__":
    # 定义测试路径节点
    path = [{'position': (1, 1)}, {'position': (2, 1)}, {'position': (3, 2)}, {'position': (4, 4)}]

    # 绘制路径动画
    draw_path_animation(path, 20)
