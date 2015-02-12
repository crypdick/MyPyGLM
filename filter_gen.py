# -*- coding: utf-8 -*-
"""
Filter generator

makes a filter

Created on Wed Feb 11 21:13:11 2015
@author: Richard Decal, decal@uw.edu
"""
import numpy as np

TIMESTEPS = 100
MAX = 1.0

filter = np.arange(0, MAX, 1./TIMESTEPS)

#==============================================================================
####### store the numpy array
#np.savetxt("straight_filter_100times.txt", filter)
#==============================================================================
