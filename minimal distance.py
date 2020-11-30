def min_dis(ux, uy, vx, vy):
    dis_lst = []
    for i in range(len(ux)):
        dis_lst.append((ux[i] - vx[i]) ** 2 + (uy[i] - vy[i]) ** 2)
    min = dis_lst[0]
    for i in range(len(dis_lst)):
        if dis_lst[i] <= min:
            min = dis_lst[i]
    return min


