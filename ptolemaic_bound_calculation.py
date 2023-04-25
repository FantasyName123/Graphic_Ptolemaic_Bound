import numpy as np
from math import dist, sqrt


def ptolemaic_lower_bound(qp, qs, op, os, ps):
    """
    Evaluates the ptolemaic lower bound, based on given distances. The point q is the query, o the object to consider,
    p and s are the pivot objects.

    :param qp: Distance between q and p.
    :param qs: Distance between q and s.
    :param op: Distance between o and p.
    :param os: Distance between o and s.
    :param ps: Distance between p and s. Must not be zero.
    :return: The ptolemaic lower bound.
    """
    result = abs(qs * op - qp * os) / ps
    return result


def ptolemaic_lower_bound_points(q, o, p, s):
    """
    Evaluates the ptolemaic lower bound, based on the given points. The distance used is the euclidean distance.

    :param q: The query object q, as a list (or similar) of its coordinates..
    :param o: The chosen object o, as a list (or similar) of its coordinates.
    :param p: The pivot object p, as a list (or similar) of its coordinates.
    :param s: The pivot object s, as a list (or similar) of its coordinates.
    :return: The ptolemaic lower bound.
    """
    qp = dist(q, p)
    qs = dist(q, s)
    op = dist(o, p)
    os = dist(o, s)
    ps = dist(p, s)
    result = abs(qs * op - qp * os) / ps
    return result


def ptolemaic_bound_vectorized_point_based(q, p, s, distance='euclidean'):
    """
    Creates a grid of 1001x1001 points in the square [0,100]^2. For each point, the ptolemaic lower bound is
    computed, with respect to the query q and the pivots p and s.

    :param q: The query object q, as a list (or similar) of its coordinates.
    :param p: The pivot object p, as a list (or similar) of its coordinates.
    :param s: The pivot object s, as a list (or similar) of its coordinates.
    :param distance: The underlying distance function. Currently possible values are 'euclidean', 'L1' (which is not
        ptolemaic!) and 'sqrt_L1' (the metric obtained by taking the root of the L1 metric, which results in a ptolemaic
        metric). More distance functions could be added.
    :return: A 2-dimensional array containing the ptolemaic lower bound, with respect to q, p and s,
        for 1001x1001 grid points.
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
    objects = np.array(np.meshgrid(xlist, ylist))
    dimension = 2
    objects_re = objects.reshape(-1, order='F').reshape((len(ylist), len(xlist), dimension), order='C')
    if distance == 'euclidean':
        dist_OP = np.sqrt(((objects_re - p) ** 2).sum(axis=2)).T
        dist_OS = np.sqrt(((objects_re - s) ** 2).sum(axis=2)).T
    elif distance == 'L1':
        dist_OP = abs(objects_re - p).sum(axis=2).T
        dist_OS = abs(objects_re - s).sum(axis=2).T
    elif distance == 'sqrt_L1':
        dist_OP = np.sqrt(abs(objects_re - p).sum(axis=2).T)
        dist_OS = np.sqrt(abs(objects_re - s).sum(axis=2).T)

    Z = ptolemaic_lower_bound(dist_qp, dist_qs, dist_OP, dist_OS, dist_ps)
    return Z