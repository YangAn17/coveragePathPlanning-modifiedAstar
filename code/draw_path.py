import matplotlib.pyplot as plt

def draw_path(path):
    """
    绘制路径并标记节点和连接线。

    参数：
    path : list
        路径节点的列表，每个节点是一个类，包含 'position' 属性表示节点的位置坐标。

    返回：
    无
    """
    plt.figure()
    # 绘制除最后一个节点外的所有节点和连接线
    for i in range(len(path) - 1):
        # 绘制节点
        ### 离散空间位置换算到连续空间，+ 0.25是为了将节点矩形的中心放在栅格中心 ###
        plt.gca().add_patch(plt.Rectangle((path[i]['position'][0] + 0.25, path[i]['position'][1] + 0.25), 0.5, 0.5,
                                            edgecolor='red', facecolor='red', linewidth=2, alpha=0.7))
        # 绘制连接线
        plt.plot([path[i]['position'][0] + 0.5, path[i + 1]['position'][0] + 0.5],
                    [path[i]['position'][1] + 0.5, path[i + 1]['position'][1] + 0.5], color='red', linewidth=2)
    
    # 最后一个节点
    plt.gca().add_patch(plt.Rectangle((path[-1]['position'][0] + 0.25, path[-1]['position'][1] + 0.25), 0.5, 0.5,
                                        edgecolor='blue', facecolor='blue', linewidth=2, alpha=0.7))
    
    plt.axis('equal')
    plt.show()

# 测试示例
if __name__ == "__main__":
    # 定义测试路径节点
    path = [{'position': (1, 1)}, {'position': (2, 2)}, {'position': (3, 3)}, {'position': (4, 4)}]

    # 绘制路径
    draw_path(path)
