from main import *

def min_dis(ux, uy, vx, vy):
    dis_lst = []
    for i in range(len(ux)):
        dis_lst.append((ux[i] - vx[i]) ** 2 + (uy[i] - vy[i]) ** 2)
    min = dis_lst[0]
    for i in range(len(dis_lst)):
        if dis_lst[i] <= min:
            min = dis_lst[i]
    return min


def min_distance_kassam ( theta )
    kassam_x = rocket_void(0, 225, 50, save_file=True)[0]
    kassam_y = rocket_void(0, 225, 50, save_file=True)[1]
    kipa_x = rocket_void(0.75 * kassam_x[-1], 225, theta, save_file=True)[0]
    kipa_y = rocket_void(0.75 * kassam_x[-1], 225, theta, save_file=True)[1]
