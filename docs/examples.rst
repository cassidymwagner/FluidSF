Examples
=============

A sample dataset is provided in ``oceans_sf/examples/sample_data`` which we 
use below to demonstrate OceanSF functionality.

Loading and preparing HDF5 data for OceanSF
*******************************************

.. code-block:: python
   
   import h5py
   
   f = h5py.File('oceans_sf/examples/sample_data/snapshot1.jld2', 'r')
   grid = f['grid']
   snapshots = f['snapshots']

   x = grid['x']
   y = grid['y']
   u = snapshots['u']
   v = snapshots['v']

3rd order longitudinal velocity structure functions
***************************************************

This snippet returns four arrays, the zonal structure function, the 
meridional structure function, the length separations in x and the length 
separations in y.

.. code-block:: python
   
   import oceans_sf as ocsf

   Z, M, XD, YD = ocsf.traditional_velocity(u,v,x,y)

Advective velocity structure functions
**************************************

.. code-block:: python

   Z, M, XD, YD = ocsf.advection_velocity(u, v, x, y)

Advective vorticity structure functions
***************************************

Multiple snapshots of data
**************************

Plotting cascade rates
**********************