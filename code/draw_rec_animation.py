import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_rec_animation(path):
    """
    根据路径绘制矩形动画。

    参数：
    path : list
        包含矩形位置信息的路径。

    返回：
    无
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for i in range(len(path)):
        # 绘制矩形
        rect = patches.Rectangle((path[i]['position'][0], path[i]['position'][1]), 1, 1, edgecolor='b', facecolor='none')
        ax.add_patch(rect)
        plt.pause(0.1)
        rect.remove()

        # 绘制中心矩形
        rect_center = patches.Rectangle((path[i]['position'][0] + 0.25, path[i]['position'][1] + 0.25), 0.5, 0.5,
                                        edgecolor='r', facecolor='r')
        ax.add_patch(rect_center)
        plt.pause(0.1)
        rect_center.remove()

# 测试示例
if __name__ == "__main__":
    # 生成示例路径
    path = [{'position': [1, 1]}, {'position': [2, 2]}, {'position': [3, 3]}, {'position': [4, 4]}]

    # 绘制动画
    draw_rec_animation(path)
    plt.show()
