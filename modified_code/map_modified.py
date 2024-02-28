import pandas as pd
import matplotlib.pyplot as plt

## 用于生成地图和随机障碍物
#
def map(map_width, map_height, obs_num):
    """
    创建地图并添加障碍物
    
    参数：
    map_width : int
        地图的宽度
    map_height : int
        地图的高度
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

    # 随机生成障碍物
    for i in range(obs_num):
        length = np.random.randint(1, 6)
        width = np.random.randint(1, 5)
        x = np.random.randint(0, map_width - length)  # 障碍物的左下角横坐标（保证不超出地图范围）
        y = np.random.randint(0, map_height - width)  # 障碍物的左下角纵坐标（保证不超出地图范围）
        obstacles.append([x, y, x + length, y + width])  # 将障碍物的左下角和右上角坐标存入obstacles列表
        plt.Rectangle((x, y), length, width, facecolor=[0.3, 0.3, 0.3])  # 创建一个矩形对象表示障碍物
        plt.gca().add_patch(plt.Rectangle((x, y), length, width, facecolor=[0.3, 0.3, 0.3]))  # 将矩形对象添加到当前图形中显示

    # 打印地图的栅格
    for i in range(map_width + 1):
        plt.plot([i, i], [0, map_height], 'k')  # 纵向线
    for i in range(map_height + 1):
        plt.plot([0, map_width], [i, i], 'k')  # 横向线

    plt.axis('equal')  # 设置x和y轴的刻度一致，保证地图比例尺正确
    plt.show()

    return obstacles


## 从CSV文件中读取障碍物信息，并生成地图
#
def map_read(map_width, map_height, csv_file):
    """
    从CSV文件中读取障碍物信息，并生成地图
    
    参数：
    csv_file : str
        包含障碍物信息的CSV文件的路径
    
    返回：
    obstacles : list
        包含障碍物坐标的列表
    """
    plt.figure()  # 创建图窗窗口
    plt.box(True)  # 在坐标区周围显示框轮廓

    # 读取CSV文件
    df = pd.read_csv(csv_file)
    
    # 保存障碍物坐标
    # obstacles列表中每个元素的格式为 [left, bottom, right, top]
    obstacles = []

    # 绘制障碍物
    for index, row in df.iterrows():
        left = row['left']
        bottom = row['bottom']
        right = row['right']
        top = row['top']
        obstacles.append([left, bottom, right, top])  # 将障碍物的左下角和右上角坐标存入obstacles列表
        plt.Rectangle((left, bottom), right - left, top - bottom, facecolor=[0.3, 0.3, 0.3])  # 创建一个矩形对象表示障碍物
        plt.gca().add_patch(plt.Rectangle((left, bottom), right - left, top - bottom, facecolor=[0.3, 0.3, 0.3]))  # 将矩形对象添加到当前图形中显示
    
    # 打印地图的栅格
    for i in range(map_width + 1):
        plt.plot([i, i], [0, map_height], 'k')  # 纵向线
    for i in range(map_height + 1):
        plt.plot([0, map_width], [i, i], 'k')  # 横向线
    
    plt.axis('equal')  # 设置x和y轴的刻度一致，保证地图比例尺正确
    plt.show()

    return obstacles

# 测试示例
if __name__ == "__main__":
    import numpy as np
    # 生成随机障碍物并保存为CSV文件的示例代码
    def generate_obstacles_csv(map_width, map_height, obs_num, file_path):
        obstacles = []
        for i in range(obs_num):
            length = np.random.randint(1, 6)
            width = np.random.randint(1, 5)
            left = np.random.randint(0, map_width - length)
            bottom = np.random.randint(0, map_height - width)
            right = left + length
            top = bottom + width
            obstacles.append([left, bottom, right, top])

        df = pd.DataFrame(obstacles, columns=['left', 'bottom', 'right', 'top'])
        df.to_csv(file_path, index=False)

    # 生成随机障碍物并保存为CSV文件
    generate_obstacles_csv(20, 15, 5, 'modified_code/obstacles.csv')

    # 从CSV文件读取障碍物并创建地图
    obstacles = map_read(20, 15, 'modified_code/obstacles.csv')
    print("障碍物坐标：", obstacles)
