import numpy as np
from map import map_read
from binn import binn
from Robot3 import robot3
from point_parameter import point_parameter
from draw_rec_animation import draw_rec_animation
from draw_path_animation import draw_path_animation

# --------------------------------------------主程序-------------------------------------------- #

map_size = 81   # 地图大小
M = 2           # UAV数量
d = map_size    # 地图大小
C = 5           # 期望覆盖值
r = 1           # 与墙排斥距离
r0 = 1          # 侦察半径
R = 0.5         # 机间排斥距离
t0 = 0.1        # 时间步长
t = 0           # 全局时间
number = 1      # 全覆盖时间索引
g1 = 0.05       # 速度系数
g2 = 0.04       # 与墙排斥系数
g3 = 0.04       # 机间排斥系数
g4 = 0.05       # 覆盖吸引系数
vth = np.pi / 2 * np.ones(M)    # 速度方向

# UAV起始坐标
x = np.zeros(M)
y = np.zeros(M)

# 生成M个UAV
x0 = np.arange(0.5, map_size, 0.5)
y0 = np.arange(0.5, map_size, 0.5)
X0, Y0 = np.meshgrid(x0, y0)
L = len(x0)
T0 = np.zeros((L, L))

f = [robot3() for _ in range(M)]
for i in range(M):
    f[i].x = 0.5 + i
    f[i].y = 0.5
    f[i].X0 = X0
    f[i].Y0 = Y0
    f[i].L = L

# 存放UAV每个时间段的坐标
X = np.zeros((M, 2000))
Y = np.zeros((M, 2000))

# RGB颜色
a = [0, 1, 0, 0, 1, 1, 0.6350, 0.4940, 0.9290]
b = [1, 0, 0, 1, 0, 1, 5.078, 0.1840, 0.6940]
c = [0, 0, 1, 1, 1, 0, 0.1840, 0.5560, 0.1250]

# ----------------------------------------全覆盖搜索算法---------------------------------------- #
obstacles = map_read(map_size, './data/obstacles_zq.csv')  # 障碍物设置
points, path = binn(map_size, obstacles)  # 全覆盖路径规划
Nice_path, Path_length, turn_number = point_parameter(path, points, map_size)  # 全覆盖算法性能参数
draw_rec_animation(map_size, obstacles, path)
# draw_path_animation(path)

