import numpy as np
import matplotlib.pyplot as plt

from ptolemaic_bound_calculation import *


def ptolemy_bound_vector_space(q, p, s, distance='euclidean'):
    """
    Visualizes the ptolemaic lower bound in the square [0,100]^2, with respect to the query q and the pivot objects p
    and s. Uses grid points with a resolution of 10 points per unit.

    :param q: The query object q, as a list (or similar) of its coordinates.
    :param p: The pivot object p, as a list (or similar) of its coordinates.
    :param s: The pivot object s, as a list (or similar) of its coordinates.
    :param distance: The underlying distance function. Currently possible values are 'euclidean', 'L1' (which is not
        ptolemaic!) and 'sqrt_L1' (the metric obtained by taking the root of the L1 metric, which results in a ptolemaic
        metric). More distance functions could be added.
    :return: None.
    """
    Z = ptolemaic_bound_vectorized_point_based(q=q, p=p, s=s, distance=distance)

    fig, ax = plt.subplots()
    xlist = np.linspace(0, 100, 1001)
    ylist = np.linspace(0, 100, 1001)
    X, Y = np.meshgrid(xlist, ylist)
    levels = [0, 1, 2, 3, 4, 10, 20]
    cnt = plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.RdBu)
    fig.colorbar(cnt)

    # Markers
    plt.plot(q[0], q[1], marker='o')
    plt.plot(p[0], p[1], marker='o', color='black')
    plt.plot(s[0], s[1], marker='o', color='black')

    plt.show(block=True)


def ptolemy_bound_vector_space_triple(q, p1, p2, p3, distance='euclidean'):
    """
    Using three pivots objects, three pairs of pivots objects can be obtained, and hence three ptolemaic lower bounds
    can be computed for every possible point. This method creates a 1001x1001 grid in the square [0,100]^2 and,
    for each point, picks the maximum of the three ptolemaic bounds. The result is visualized.

    :param q: The query object q, as a list (or similar) of its coordinates.
    :param p1: The pivot object p1, as a list (or similar) of its coordinates.
    :param p2: The pivot object p2, as a list (or similar) of its coordinates.
    :param p3: The pivot object p3, as a list (or similar) of its coordinates.
    :param distance: The underlying distance function. Currently possible values are 'euclidean', 'L1' (which is not
        ptolemaic!) and 'sqrt_L1' (the metric obtained by taking the root of the L1 metric, which results in a ptolemaic
        metric). More distance functions could be added.
    :return: None.
    """
    Z_12 = ptolemaic_bound_vectorized_point_based(q=q, p=p1, s=p2, distance=distance)
    Z_13 = ptolemaic_bound_vectorized_point_based(q=q, p=p1, s=p3, distance=distance)
    Z_23 = ptolemaic_bound_vectorized_point_based(q=q, p=p2, s=p3, distance=distance)

    array_collection = np.array([Z_12, Z_13, Z_23])
    Z = array_collection.max(axis=0)

    fig, ax = plt.subplots()
    xlist = np.linspace(0, 100, 1001)
    ylist = np.linspace(0, 100, 1001)
    X, Y = np.meshgrid(xlist, ylist)
    levels = [0, 1, 2, 3, 4, 10, 20]
    cnt = plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.RdBu)
    fig.colorbar(cnt)

    # Markers
    plt.plot(q[0], q[1], marker='o')
    plt.plot(p1[0], p1[1], marker='o', color='black')
    plt.plot(p2[0], p2[1], marker='o', color='black')
    plt.plot(p3[0], p3[1], marker='o', color='black')

    plt.show()


def ptolemy_bound_pivot_space(q, p, s, distance='euclidean'):
    """
    Visualizes the ptolemaic lower bound in the pivot space. (The distances to the pivot objects form the dimensions of
    this vector space.) Since two points the the square [0,100]^2 can have a distance up to sqrt(200), a greater side
    length of 150 is used.

    :param q: The query object q, as a list (or similar) of its coordinates.
    :param p: The pivot object p, as a list (or similar) of its coordinates.
    :param s: The pivot object s, as a list (or similar) of its coordinates.
    :param distance: The underlying distance function. Currently possible values are 'euclidean', 'L1' (which is not
        ptolemaic!) and 'sqrt_L1' (the metric obtained by taking the root of the L1 metric, which results in a ptolemaic
        metric). More distance functions could be added.
    :return: None.
    """
    if distance == 'euclidean':
        dist_qp = dist(q, p)
        dist_qs = dist(q, s)
        dist_ps = dist(p, s)
    elif distance == 'L1':
        dist_qp = abs(np.array(q) - np.array(p)).sum()
        dist_qs = abs(np.array(q) - np.array(s)).sum()
        dist_ps = abs(np.array(p) - np.array(s)).sum()
    elif distance == 'sqrt_L1':
        dist_qp = sqrt(abs(np.array(q) - np.array(p)).sum())
        dist_qs = sqrt(abs(np.array(q) - np.array(s)).sum())
        dist_ps = sqrt(abs(np.array(p) - np.array(s)).sum())
    else:
        raise ValueError(f"{distance} is not a valid distance")

    xlist = np.linspace(0, 100, 1001)
    ylist = np.linspace(0, 100, 1001)
    dist_P1, dist_P2 = np.meshgrid(xlist, ylist)

    X, Y = np.meshgrid(xlist, ylist)

    Z = ptolemaic_lower_bound(qp=dist_qp, qs=dist_qs, op=dist_P1, os=dist_P2, ps=dist_ps)
    fig, ax = plt.subplots()
    levels = [0, 1, 2, 3, 4, 10, 20]
    cnt = plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.RdBu)

    fig.colorbar(cnt)

    plt.plot(dist_qp, dist_qs, marker='o')
    plt.plot(0, dist_ps, marker='o', color='black')
    plt.plot(dist_ps, 0, marker='o', color='black')

    # plt.imshow(Z, extent=(X.min(), X.max(), Y.min(), Y.max()), origin='lower', cmap=plt.cm.RdBu)
    plt.show()