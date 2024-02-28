class Robot3:
    def __init__(self):
        """
        初始化方法，用于创建Robot3类的实例对象
        
        属性：
        x : float
            代表Agent的横坐标
        y : float
            代表Agent的纵坐标
        L : int
            代表Map长度
        X0 : list
            代表Map栅格中心横坐标集合
        Y0 : list
            代表Map栅格中心纵坐标集合
        """
        self.x = 0
        self.y = 0
        self.L = 0
        self.X0 = []
        self.Y0 = []

    @property
    def s(self):
        """
        计算点到中心的距离
        
        返回：
        list
            包含点到中心的距离的二维列表
        """
        s = []
        for i in range(self.L):
            row = []
            for j in range(self.L):
                distance = ((self.X0[i][j] - self.x) ** 2 + (self.Y0[i][j] - self.y) ** 2) ** 0.5
                row.append(distance)
            s.append(row)
        return s

# 测试示例
if __name__ == "__main__":
    import numpy as np

    # 生成小网格中心的横坐标和纵坐标
    x0 = np.arange(0, 1.0, 0.0625)
    y0 = np.arange(0, 1.0, 0.0625)
    # 创建坐标网格
    X0, Y0 = np.meshgrid(x0, y0)
    # 创建一个Robot3对象
    robot = Robot3()
    # 设置属性值
    robot.x = 0
    robot.y = 0
    robot.L = len(x0)
    robot.X0 = X0
    robot.Y0 = Y0
    # 计算点到中心的距离
    distances = robot.s
    # 打印结果
    print("点到中心的距离：")
    for row in distances:
        print(row)
