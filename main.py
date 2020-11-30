import numpy as np
import scipy.integrate as sp
import math
import matplotlib.pyplot as plt


def df(t, x):
    x, y, v_x, v_y = x
    return v_x, v_y, 0, -9.81


def deg_2_rad(deg):
    return deg*math.pi/180.0


def rocket_void():
    t_0 = 0
    y_0 = 0
    t = np.linspace(0, 50, 1000)
    g = 9.81
    start_params = [0, 0, 255 * math.cos(deg_2_rad(50)), 255 * math.sin(deg_2_rad(50))]
    r = sp.odeint(df, start_params, t, tfirst=True)
    # x0 = (0, 0, math.cos(deg_2_rad(50))*225, 255 * math.sin(deg_2_rad(50))), args = (x,y,v_x,v_y))
    r = np.ndarray.transpose(r)

    t_star = np.argmin([abs(a) for a in r[1][1:]])

    r = [row[:t_star] for row in r]

    plt.figure()
    plt.plot(r[0], r[1])
    plt.title("Rocket Location");
    plt.xlabel('x [m]');
    plt.ylabel('y [m]');
    plt.show()


if __name__ == "__main__":
    rocket_void()
