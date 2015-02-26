# -*- coding: utf-8 -*-
"""
Filter generator, currently just making one shaped like a right triangle

Created on Wed Feb 11 21:13:11 2015
@author: Richard Decal, decal@uw.edu
"""
import numpy as np
import matplotlib.pyplot as plt

TIMESTEPS = 100
MAX = 1.0

#make the filter a line of slope 1 from x = (0,100)
filter = np.arange(0, MAX, 1./TIMESTEPS)
xs = [i for i in range(len(filter))]

#show filter
fig = plt.plot(xs, filter)
plt.show()

#==============================================================================
####### store the numpy array
#np.savetxt("straight_filter_100times.txt", filter)
#==============================================================================
