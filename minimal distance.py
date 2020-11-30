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
    kipa_x = rocket_with_grar(0.75 * kassam_x[-1], 225, theta, save_file=False, c=0.28 )[0]
    kipa_y = rocket_with_grar(0.75 * kassam_x[-1], 225, theta, save_file=False, c=0.28 )[1]
    return math.sqrt(min_dis(kassam_x, kassam_y, kipa_x, kipa_y))


kassam_x = rocket_with_grar(0, 225, 50, save_file=False)[0]

r_me = rocket_with_grar(0.75 * kassam_x[-1], 225, 134.77, save_file=False, c=0.28)
r_oyev = rocket_with_grar(0, 225, 50, save_file=False)



def secant(theta0, theta1):
    theta_nm1 = theta0
    theta_n = theta1

    while True:
        f_div = (min_distance_kassam(theta_n) - min_distance_kassam(theta_nm1)) / (theta_n - theta_nm1)
        theta_np1 = theta_n - min_distance_kassam(theta_n) / f_div

        theta_nm1 = theta_n
        theta_n = theta_np1
        print(abs(theta_nm1 - theta_n))
        if abs(theta_nm1 - theta_n) < 0.1: return theta_n




def secant_for_dest(theta0, theta1, v_0, dest):
    theta_nm1 = theta0
    theta_n = theta1

    while True:
        f_div = (simulate_hit(v_0, theta_n) - simulate_hit(v_0, theta_nm1)) / (theta_n - theta_nm1)
        theta_np1 = theta_n - ((simulate_hit(v_0, theta_n))-dest) / f_div

        theta_nm1 = theta_n
        theta_n = theta_np1
        print(abs(theta_nm1 - theta_n))
        if abs(theta_nm1 - theta_n) < 0.1: return theta_n


def visualization():
    list_of_tetha=[]
    list_of_distances=[]
    for i in range(2001):
        list_of_tetha.append(50+float(i)*0.01)
    for j in range(2001):
        list_of_distances.append(simulate_hit(225, 50+float(j)*0.01))
    plt.scatter(list_of_distances, list_of_tetha)
    plt.xlabel("distance [m]")
    plt.ylabel("Lunching angle [deg]")
    plt.title("Distance vs Lunching Angle")
    plt.grid()
    plt.show()



if __name__=="__main__":
    visualization()
