import numpy as np
import itertools

def coverage(s, T, r0_coverage, x_current, y_current, X0, Y0, Vth, g1, g4, C, co, ro):
    """
    计算覆盖路径和控制速度。

    参数：
    s : Robot3_class/numpy.ndarray
        Agent到各栅格中心的距离数组。
    T : numpy.ndarray
        地图上的覆盖值数组。
    r0_coverage : float
        传感器的覆盖范围半径。
    x_current : float
        无人机当前位置的 x 坐标。
    y_current : float
        无人机当前位置的 y 坐标。
    X0 : numpy.ndarray
        地图上每个点的 x 坐标数组。
    Y0 : numpy.ndarray
        地图上每个点的 y 坐标数组。
    Vth : float
        无人机当前运行方向的角度。
    g1 : float
        参数 g1。
    g4 : float
        参数 g4。
    C : float
        期望的覆盖值。
    co : list
        障碍物在 x 轴上的索引的数组。
    ro : list
        障碍物在 y 轴上的索引的数组。

    返回：
    T : numpy.ndarray
        更新后的地图覆盖值数组(高程)。
    vxcoverage : float
        x 方向上的覆盖控制速度。
    vycoverage : float
        y 方向上的覆盖控制速度。
    vth : float
        控制速度方向角度。
    """
### 注意障碍物索引/地图覆盖值索引在连续空间，无人机位置索引在离散空间 ###

    # 更新覆盖值
    row1, rol1 = np.where(s <= r0_coverage)  # 寻找无人机探测范围内的栅格中心点
    T[row1, rol1] += r0_coverage  # 给探测范围内的中心点增加 r0_coverage 的覆盖值
    T[T < C] = np.minimum(T[T < C], C)  # 限制覆盖值最高为期望的覆盖值 C

    # 障碍物不会被扫描所干扰，将其覆盖值设置为固定值 10
    for j, i in itertools.product(co, ro):
        if (i > len(ro) / 2 and j < len(co) / 2) or (i < len(ro) / 2 and j > len(co) / 2):
            T[j, i] = 10

    # 更新后无人机探测范围内的覆盖值
    row2, rol2 = np.where(s <= r0_coverage)  # 得到范围内所有网格点的索引
    T0 = T[row2, rol2]  # 将所有点的栅格值存入 T0 数组

    # -------------------------无人机覆盖控制速度-------------------------------%
    [row3, rol3] = np.where(T0 == np.min(T0))  # 覆盖范围内覆盖值最小的点，得到最小值所在的行与列
    Ct = T0[rol3[0]]  # 得到智能体m覆盖范围内最小值的大小
    if Ct != C:  # 当覆盖范围内存在最小值不等于20时
        h3 = len(row3)  # 得到最小值的个数
        th = np.zeros(h3)  # 初始化th，th为到每个最小值点的角度值
        for i in range(h3):
            dx = X0[row2[rol3[i]], rol2[rol3[i]]] - x_current  # X0[row2[j], rol2[j]]为范围内最小值网格点的x坐标
            dy = Y0[row2[rol3[i]], rol2[rol3[i]]] - y_current  # Y0[row2[j], rol2[j]]为范围内最小值网格点的y坐标
            th[i] = np.arctan2(dy, dx)
        th0 = np.abs(th - Vth)  # 网格最小点方向与当前无人机运行方向的角度差
        [row4, rol4] = np.where(th0 == np.min(th0))  # 覆盖值最小点中与上一时刻速度角度差最小的点
        vth = th[rol4[0]]  # 找到角度差最小的点作为牵引点
        dv = C - T[row2[rol3[rol4[0]]], rol2[rol3[rol4[0]]]]  # C减去覆盖值最低且角度差最小的点的覆盖值
        g = g1
    else:  # 当覆盖范围内没有小于C的点时
        [row5, rol5] = np.where(T < C)  # 覆盖范围外覆盖值小于C的点
        if len(row5) == 0:  # 如果数组为空
            dv = 0
            vth = 0
        else:  # 覆盖范围外覆盖值小于C的点不为空
            h4 = len(row5)
            s1 = np.zeros(h4)  # 初始化s1，s1为每个小于C的点的大小
            for i in range(h4):
                s1[i] = s[row5[i], rol5[i]]  # 保存覆盖范围外的覆盖值
            [row6, rol6] = np.where(s1 == np.min(s1))  # 寻找范围外覆盖值最小的点
            dx = X0[row5[rol6[0]], rol5[rol6[0]]] - x_current  # 将范围外最小值点作为牵引点，供下一时刻无人机前往
            dy = Y0[row5[rol6[0]], rol5[rol6[0]]] - y_current
            vth = np.arctan2(dy, dx)  # 得到牵引点到当前点的角度信息

            dv1 = s1[rol6[0]]
            if dv1 < 15:
                dv = 15
            else:
                dv = dv1
        g = g4

    vxcoverage = g * dv * np.cos(vth)
    vycoverage = g * dv * np.sin(vth)

    return T, vxcoverage, vycoverage, vth

# 测试示例
if __name__ == "__main__":
    # 定义参数
    s = np.random.rand(10, 10)  # 示例探测范围内的覆盖值
    T = np.zeros((10, 10))  # 初始化覆盖