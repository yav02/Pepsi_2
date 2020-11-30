from main import *
import math
import numpy as np


def min_dis(ux, uy, vx, vy):
    dis_lst = []
    for i in range(min(len(ux), len(vx))):
        dis_lst.append((ux[i] - vx[i]) ** 2 + (uy[i] - vy[i]) ** 2)
    min1 = dis_lst[0]
    for i in range(len(dis_lst)):
        if dis_lst[i] <= min1:
            min1 = dis_lst[i]
    return min1


def min_distance_kassam(theta):
    kassam_x = rocket_with_grar(0, 225, 50, save_file=False)[0]
    kassam_y = rocket_with_grar(0, 225, 50, save_file=False)[1]
    kipa_x = rocket_with_grar(0.75 * kassam_x[-1], 225, theta, save_file=False, c=0.28)[0]
    kipa_y = rocket_with_grar(0.75 * kassam_x[-1], 225, theta, save_file=False, c=0.28)[1]
    return math.sqrt(min_dis(kassam_x, kassam_y, kipa_x, kipa_y))


r_oyev = rocket_with_grar(0, 225, 50, save_file=False)
r_me = rocket_with_grar(0.75 * r_oyev[0][-1], 225, 134.77, save_file=False)

index = 0
for i in range(len(r_me[0])):
    if np.abs(r_me[0][i] - r_oyev[0][i])<5:
        index = i
        break


plt.figure()
plt.plot(r_me[0][:index], r_me[1][:index], label="Iron Dome")
plt.plot(r_oyev[0][:index], r_oyev[1][:index], label='Kasam')
plt.legend()
plt.ylim([0, 1500])
plt.xlim([0, 4500])
plt.xlabel("x [m]")
plt.title("Iron Dome vs Kasam")
plt.ylabel("Height [m]")
plt.show()


def secant(theta0, theta1):
    theta_nm1 = theta0
    theta_n = theta1

    while True:
        f_div = (min_distance_kassam(theta_n) - min_distance_kassam(theta_nm1)) / (theta_n - theta_nm1)
        theta_np1 = theta_n - min_distance_kassam(theta_n) / f_div

        theta_nm1 = theta_n
        theta_n = theta_np1
        print(abs(theta_nm1 - theta_n))
        if abs(theta_nm1 - theta_n) < 0.1:
            return theta_n

# print(secant(30, 70))
