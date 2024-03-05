import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax

from map import map
from binn import binn
from Robot3 import robot3
from coverage import coverage
from repulsion import repulsion
from target_point import target_point
from point_parameter import point_parameter
from plot3d_obstacle import plot3d_obstacle

# 主程序
map_size = 10   # 地图大小
M = 1           # UAV数量
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

G = np.zeros((M, 10000))    # 最多迭代10000次
h = [plt.plot([], [])[0] for _ in range(M)] # 创建空的轨迹对象

# RGB颜色
a = [0, 1, 0, 0, 1, 1, 0.6350, 0.4940, 0.9290]
b = [1, 0, 0, 1, 0, 1, 5.078, 0.1840, 0.6940]
c = [0, 0, 1, 1, 1, 0, 0.1840, 0.5560, 0.1250]

# 全覆盖搜索算法
obs_num = 1
obstacles = map(map_size, obs_num)
points, path = binn(map_size, obstacles)  # 全覆盖路径规划
Nice_path, Path_length, turn_number = point_parameter(path, points, map_size)  # 全覆盖算法性能参数

# 创建窗口1：显示二维轨迹和地图
plt.figure(1)
plt.clf()
plt.Rectangle((0, 0), map_size, map_size)  # 绘制出运动区域
plt.axis([0, map_size, 0, map_size])  # 显示的画面大小
plt.axis('equal')

# 绘制网格线
for i in range(map_size + 1):
    plt.plot([0, map_size], [i, i], color='k')
    plt.plot([i, i], [0, map_size], color='k')

# 绘制障碍物区域
for i in range(obs_num):
    plt.Rectangle((obstacles[i][0], obstacles[i][1]), obstacles[i][2] - obstacles[i][0],
                    obstacles[i][3] - obstacles[i][1], facecolor=(0.3, 0.3, 0.3))

# 绘制UAV和感知范围
uav_markers = []
for i in range(M):
    uav_marker = plt.plot(f[i].x, f[i].y, 'o', markersize=8, color=(a[i], b[i], c[i]))  # 绘制无人机
    uav_markers.append(uav_marker)
    circle = plt.Circle((f[i].x, f[i].y), r0, color=(a[i], b[i], c[i]), fill=False)  # 创建感知范围圆形
    plt.gca().add_patch(circle)  # 将圆形添加到图形对象

plt.draw()
plt.pause(0.01)

# 创建窗口2：显示三维高程覆盖
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')

# 绘制障碍物区域
co, ro, T0 = plot3d_obstacle(obstacles, T0)
s = ax.plot_surface(Y0, X0, T0, cmap='viridis')
fig.colorbar(s, shrink=0.5, aspect=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')
plt.title('3D Obstacle Map')

plt.draw()
plt.pause(0.01)

# 控制UAV的运动并更新显示
for i in range(10000):
    t = t + t0
    for m in range(M):
        vxrepulsion, vyrepulsion = repulsion(M, f[m].x, f[m].y, x, y, r, R, g2, g3, d, t)
        T0, vxcoverage, vycoverage, th = coverage(f[m].s, T0, r0, f[m].x, f[m].y, X0, Y0, vth[m], g1, g4, C, co, ro)
        target_x, target_y, number = target_point(f[m].x, f[m].y, path, number, Path_length)  # 全覆盖牵引速度
        vx = vxrepulsion + target_x     # 使用全覆盖牵引速度
        vy = vyrepulsion + target_y
        v = np.sqrt(vx ** 2 + vy ** 2)
        Vth = np.arctan2(vy, vx)
        vth[m] = Vth  # 当前无人机速度朝向

        if np.max(T0) == np.min(T0):  # 完全覆盖后无人机停止运行
            break
        else:
            G[m, i] = v * t0  # 无人机m在t0时刻的移动距离
            dx = G[m, i] * np.cos(Vth)  # 无人机m移动距离差的X轴、Y轴分量
            dy = G[m, i] * np.sin(Vth)
            X[m, i] = f[m].x + dx  # 无人机m移动后的横坐标、纵坐标
            Y[m, i] = f[m].y + dy
            f[m].x = X[m, i]  # 更新无人机m的横坐标、纵坐标
            f[m].y = Y[m, i]
            x[m] = X[m, i]  # 更新全部无人机的横坐标、纵坐标

            # 更新轨迹对象的数据并绘制路径
            h[m].set_xdata(np.append(h[m].get_xdata(), X[m, i]))
            h[m].set_ydata(np.append(h[m].get_ydata(), Y[m, i]))

            # 更新UAV位置
            uav_markers[m][0].set_data(f[m].x, f[m].y)

            # 清除先前的图形并重新绘制新的障碍物区域和地图数据
            ax.collections.clear()
            co, ro, T0 = plot3d_obstacle(obstacles, T0)
            s = ax.plot_surface(Y0, X0, T0, cmap='viridis', alpha=0.5)  # 降低地图的透明度，以显示UAV的覆盖效果
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Height')
            plt.title('3D Obstacle Map')

    plt.draw()
    plt.pause(0.01)
    if np.max(T0) == np.min(T0):  # 完全覆盖后，程序结束
        break
