class point:
    def __init__(self, position=[0, 0], covered=False, x1=0, x2=0, x3=0):
        """
        初始化方法，用于创建 Point 类的实例对象
        
        参数：
        position : list
            表示点的坐标，例如 [x, y]
        covered : bool
            表示点是否被覆盖，True 表示被覆盖，False 表示未被覆盖
        x1 : float
            表示自身活动值
        x2 : float
            表示周围效应活动值
        x3 : float
            表示方向效应活动值
        """
        self.position = position
        self.covered = covered
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

# 测试示例
if __name__ == "__main__":
    # 创建一个位置为 (1, 2, 3)、未被覆盖、自身活动值为 0.1、周围效应活动值为 0.2、方向效应活动值为 0.3 的点
    pt1 = point([1, 2], False, 0.1, 0.2, 0.3)
    around_points = [point()]
    # 打印结果
    print(type(around_points))
    print(pt1.position[0])  # [1, 2]
    print(pt1.covered)  # False
    print(pt1.x1)  # 0.1
    print(pt1.x2)  # 0.2
    print(pt1.x3)  # 0.3
