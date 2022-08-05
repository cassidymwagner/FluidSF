import numpy as np


def calculate_scalar_advection(scalar, par_u, par_v, x, y):
    """_summary_

    Parameters
    ----------
    scalar : _type_
        _description_
    par_u : _type_
        _description_
    par_v : _type_
        _description_
    x : _type_
        _description_
    y : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    u = par_u
    v = par_v
    s = scalar

    dx = np.abs(x[0] - x[1])
    dy = np.abs(y[0] - y[1])

    s_ip1 = np.roll(s, -1, axis=1)
    s_im1 = np.roll(s, 1, axis=1)
    s_jp1 = np.roll(s, -1, axis=0)
    s_jm1 = np.roll(s, 1, axis=0)

    dsdx = (s_ip1 - s_im1) / (2 * dx)
    dsdy = (s_jp1 - s_jm1) / (2 * dy)

    advection = u * dsdx + v * dsdy

    return (advection)
