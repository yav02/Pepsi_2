import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sp


def df_void(t, x):
    x, y, v_x, v_y = x
    return v_x, v_y, 0, -9.81


def df_grar(t, x):
    rho = 1.184
    m = 35
    c = 0.4
    g = -9.81
    A = math.pi * 0.001125
    x, y, v_x, v_y = x

    mekadem = (c * A * rho * math.sqrt(v_x ** 2 + v_y ** 2)) / m
    new_v_x = -mekadem * v_x
    new_v_y = g - mekadem * v_x
    return v_x, v_y, new_v_x, new_v_y


def deg_2_rad(deg):
    return deg * math.pi / 180.0


def rocket_void(x_0, v_0, angle, save_file=True):
    t = np.linspace(0, 50, 1000)
    start_params = [x_0, 0, v_0 * math.cos(deg_2_rad(angle)), v_0 * math.sin(deg_2_rad(angle))]
    r = sp.odeint(df_void, start_params, t, tfirst=True)
    r = np.ndarray.transpose(r)

    t_star = np.argmin([abs(a) for a in r[1][1:]])

    r = [row[:t_star] for row in r]

    plt.figure()
    plt.plot(r[0], r[1])
    plt.title("Rocket Location")
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.grid()
    if save_file:
        plt.savefig(f'rocket_void_v_0_{v_0}_angle_{angle}.pdf', dpi=200, bbox_inches='tight')

    return r


def rocket_with_grar(v_0, angle, save_file=True):
    t = np.linspace(0, 50, 1000)
    start_params = [0, 0, v_0 * math.cos(deg_2_rad(angle)), v_0 * math.sin(deg_2_rad(angle))]
    r = sp.odeint(df_grar, start_params, t, tfirst=True)
    r = np.ndarray.transpose(r)

    t_star = np.argmin([abs(a) for a in r[1][1:]])

    r = [row[:t_star] for row in r]

    plt.figure()
    plt.plot(r[0], r[1])
    plt.title("Rocket Location (with friction)");
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.grid()
    if save_file:
        plt.savefig(f'rocket_friction_v_0_{v_0}_angle_{angle}.pdf', dpi=200, bbox_inches='tight')

    return r


if __name__ == "__main__":
    # rocket_void(225,50)
    rocket_with_grar(225, 50)
