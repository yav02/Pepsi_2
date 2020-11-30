import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sp


def df_void(t, x):
    x, y, v_x, v_y = x
    return v_x, v_y, 0, -9.81


def df_grar(t, x, rho=1.184, m=35, c=0.4, g=-9.81, a=math.pi * 0.001125):
    x, y, v_x, v_y = x

    mekadem = (c * a * rho * math.sqrt(v_x ** 2 + v_y ** 2)) / m
    new_v_x = -mekadem * v_x
    new_v_y = g - mekadem * v_x
    return v_x, v_y, new_v_x, new_v_y


def deg_2_rad(deg):
    return deg * math.pi / 180.0


def rocket_void(v_0, angle, save_file=True):
    t = np.linspace(0, 50, 1000)
    start_params = [0, 0, v_0 * math.cos(deg_2_rad(angle)), v_0 * math.sin(deg_2_rad(angle))]
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


def simulate_hit(v_0, angle):
    r = rocket_with_grar(0, v_0, angle, save_file=False)
    return r[0][-1]


def rocket_with_grar(x_0, v_0, angle, save_file=True, rho=1.184, m=35, c=0.4, g=-9.81, a=math.pi * 0.001125, sample_num=2000):
    t = np.linspace(0, 50, sample_num)
    start_params = [x_0, 0, v_0 * math.cos(deg_2_rad(angle)), v_0 * math.sin(deg_2_rad(angle))]
    r = sp.odeint(df_grar, start_params, t, tfirst=True, args=(rho,m,c,g,a))
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
    plt.close()

    return r


def convergence():
    samples = np.logspace(2, 5, 100)
    results = [[],[]]
    for i in samples:
        results[0].append(rocket_with_grar(0, 225, 50, save_file=False, sample_num=int(i))[0][-1])
        results[1].append((50/i))
    plt.figure()
    plt.plot(results[1],results[0])
    plt.xlabel("dt [s]")
    plt.ylabel("distance [m]")
    plt.xscale("log")
    plt.title("Convergence Test For The Algorithm")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    convergence()

