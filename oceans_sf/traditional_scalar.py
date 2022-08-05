import numpy as np

def traditional_scalar(scalar, x, y, boundary="Periodic",order=3):
    """
    Add docstring
    """

    s = scalar

    if boundary == "Periodic":
        sep = range(int(len(s) / 2))
    else:
        sep = range(int(len(s)))

    SF_z = np.zeros(np.shape(sep))
    SF_m = np.zeros(np.shape(sep))
    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x, i, axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y, i, axis=0) - y))[len(sep)]

        dz = np.roll(s, i, axis=1) - s
        dm = np.roll(s, i, axis=0) - s
        dz3 = dz**order
        dm3 = dm**order
        SF_z[i] = np.nanmean(dz3)
        SF_m[i] = np.nanmean(dm3)

    return (SF_z, SF_m, xd, yd)
