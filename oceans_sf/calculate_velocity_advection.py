import numpy as np


def calculate_velocity_advection(u, v, x, y, dx=None, dy=None, grid_type="uniform"):
    """
    Calculate the velocity advection components (eastward and northward).

    Args:
    ----
        u (ndarray): The u-component of velocity.
        v (ndarray): The v-component of velocity.
        x (ndarray): The x-coordinates of the grid.
        y (ndarray): The y-coordinates of the grid.
        dx (float or ndarray, optional): The grid spacing in the x-direction.
        Defaults to None.
        dy (float or ndarray, optional): The grid spacing in the y-direction.
        Defaults to None.
        grid_type (str, optional): The type of grid. Defaults to "uniform".

    Returns:
    -------
        tuple: A tuple containing the eastward advection and northward advection
        components.

    """
    if grid_type == "latlon":
        xcoords = dx.cumsum()
        ycoords = dy.cumsum()

        dudy, dudx = np.gradient(u, xcoords, ycoords, axis=(0, 1))
        dvdy, dvdx = np.gradient(v, xcoords, ycoords, axis=(0, 1))

    else:
        dx = np.abs(x[0] - x[1])
        dy = np.abs(y[0] - y[1])

        dudy, dudx = np.gradient(u, dx, dy, axis=(0, 1))
        dvdy, dvdx = np.gradient(v, dx, dy, axis=(0, 1))

    eastward_advection = u * dudx + v * dudy
    northward_advection = u * dvdx + v * dvdy

    return (eastward_advection, northward_advection)
