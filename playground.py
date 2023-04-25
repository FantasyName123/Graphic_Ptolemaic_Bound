import matplotlib.pyplot as plt
import numpy as np
from math import dist
from mpl_toolkits import mplot3d  # fürs 3D-Plotten


q = (45, 45)
p1 = (40, 30)
p2 = (56, 30)
p3 = (20, 201)

qp1 = dist(q, p1)
qp2 = dist(q, p2)
qp3 = dist(q, p3)
p1p2 = dist(p1, p2)
p1p3 = dist(p1, p3)
p2p3 = dist(p2, p3)

interesting_constellations = [
    [(45, 30), (40, 30), (56, 30)],  # q horizontal zwischen (eher links), vertikal gleich
    [(45, 35), (40, 30), (56, 30)],  # q horizontal zwischen (eher links), vertikal höher
    [(35, 35), (40, 30), (56, 30)],  # q horizontal links, vertikal höher
    [(30, 30), (22, 30), (38, 30)],  # q mitten auf der Verbindungslinie
    [(42, 30), (40, 30), (56, 30)],  # q sehr nah an einem Pivotelement
    [(12, 35), (40, 30), (42, 30)],  # q horizontal zwischen, vertikal höher
]


def ptolemaic_lower_bound_fixed(op1, op2):
    result = abs(qp2 * op1 - qp1 * op2) / p1p2
    return result


def ptolemaic_lower_bound(qp1, qp2, op1, op2, p1p2):
    result = abs(qp2 * op1 - qp1 * op2) / p1p2
    return result


def ptolemaic_lower_bound_points(q, p1, p2, o):
    qp1 = dist(q, p1)
    qp2 = dist(q, p2)
    p1p2 = dist(p1, p2)
    op1 = dist(o, p1)
    op2 = dist(o, p2)
    result = abs(qp2 * op1 - qp1 * op2) / p1p2
    return result


def ptolemaic_bound_vectorized_point_based(q=q, p=p1, s=p2, linspace_par=(0, 60, 1001)):
    # kann ich den Parameter linspace so weiter untern einsetzen ^^^ ??
    dist_qp = dist(q, p)
    dist_qs = dist(q, s)
    dist_ps = dist(p, s)

    xlist = np.linspace(0, 60, 1001)
    ylist = np.linspace(0, 60, 1001)
    dist_OP, dist_OS = np.meshgrid(xlist, ylist)  # nur zum Initialisieren
    for id_x, x in enumerate(xlist):
        for id_y, y in enumerate(ylist):
            o = (y, x)  # wieso ist es so herum richtig und andersherum nicht? -> wegen meshgrid(indexing='xy') !!!
            dist_OP[id_x][id_y] = dist(o, p)
            dist_OS[id_x][id_y] = dist(o, s)

    Z = ptolemaic_lower_bound(dist_qp, dist_qs, dist_OP, dist_OS, dist_ps)
    return Z


def ptolemy_bound_euclidean_space(q=q, p1=p1, p2=p2):
    xlist = np.linspace(0, 60, 1001)
    ylist = np.linspace(0, 60, 1001)
    dist_P1, dist_P2 = np.meshgrid(xlist, ylist)  # nur zum Initialisieren
    for id_x, x in enumerate(xlist):
        for id_y, y in enumerate(ylist):
            o = (y, x)  # wieso ist es so herum richtig und anders herum nicht? -> wegen meshgrid(indexing='xy') !!!
            dist_P1[id_x][id_y] = dist(o, p1)
            dist_P2[id_x][id_y] = dist(o, p2)

    X, Y = np.meshgrid(xlist, ylist)
    Z = ptolemaic_lower_bound_fixed(dist_P1, dist_P2)
    fig, ax = plt.subplots()
    levels = [0, 1, 2, 3, 4, 10, 20]
    cnt = plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.RdBu)

    fig.colorbar(cnt)

    plt.plot(q[0], q[1], marker='o')
    plt.plot(p1[0], p1[1], marker='o', color='black')
    plt.plot(p2[0], p2[1], marker='o', color='black')

    # plt.imshow(Z, extent=(X.min(), X.max(), Y.min(), Y.max()), origin='lower', cmap=plt.cm.RdBu)
    plt.show()


def ptolemy_bound_pivot_space_2d():
    xlist = np.linspace(0, 50, 1001)
    ylist = np.linspace(0, 50, 1001)
    dist_P1, dist_P2 = np.meshgrid(xlist, ylist)

    X, Y = np.meshgrid(xlist, ylist)
    Z = ptolemaic_lower_bound_fixed(dist_P1, dist_P2)
    fig, ax = plt.subplots()
    levels = [0, 1, 2, 3, 4, 10, 20]
    cnt = plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.RdBu)

    fig.colorbar(cnt)

    plt.plot(dist(q, p1), dist(q, p2), marker='o')
    plt.plot(dist(p1, p1), dist(p1, p2), marker='o', color='black')
    plt.plot(dist(p2, p1), dist(p2, p2), marker='o', color='black')

    # plt.imshow(Z, extent=(X.min(), X.max(), Y.min(), Y.max()), origin='lower', cmap=plt.cm.RdBu)
    plt.show()


def ptolemy_bound_pivot_space_3d():
    xlist = np.linspace(0, 80, 51)
    ylist = np.linspace(0, 80, 51)
    wlist = np.linspace(0, 80, 51)
    dist_P1, dist_P2, dist_P3 = np.meshgrid(xlist, ylist, wlist)

    # testing
    Z_12 = ptolemaic_lower_bound(qp1=qp1, qp2=qp2, op1=dist_P1, op2=dist_P2, p1p2=p1p2)
    Z_13 = ptolemaic_lower_bound(qp1=qp1, qp2=qp3, op1=dist_P1, op2=dist_P3, p1p2=p1p3)
    Z_23 = ptolemaic_lower_bound(qp1=qp2, qp2=qp3, op1=dist_P2, op2=dist_P3, p1p2=p2p3)
    # print(dist_P1)
    # print(dist_P2)
    # print(dist_P3)
    # print(Z_12)
    # Z_max = max([Z_12, Z_13, Z_23])
    Z_plus = Z_12 + Z_13 + Z_23
    if True:
        for id_x in range(len(xlist)):
            for id_y in range(len(ylist)):
                for id_w in range(len(wlist)):
                    Z_plus[id_x][id_y][id_w] = max(Z_12[id_x][id_y][id_w], Z_13[id_x][id_y][id_w], Z_23[id_x][id_y][id_w])
    Z_bound = Z_plus > 2
    print(Z_bound)

    # Creating figure
    fig = plt.figure(figsize=(12, 10))
    ax = plt.axes(projection="3d")

    # Creating plot
    ax.scatter3D(dist_P1, dist_P2, dist_P3, s=0.1, c=Z_bound)
    plt.title("simple 3D scatter plot")


    plt.show()


def ptolemy_bound_pivot_space_3d_naive(range_var=50):
    points = np.random.rand(range_var, 3) * 40
    print(points)

    # Creating figure
    fig = plt.figure(figsize=(12, 10))
    ax = plt.axes(projection="3d")

    # Creating plot
    #  ax.scatter3D(points, s=0.1)
    plt.title("simple 3D scatter plot")


# ---------------------------- Execution ----------------------------
if __name__ == '__main__':
    ptolemy_bound_euclidean_space()
    # ptolemy_bound_pivot_space_3d()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
