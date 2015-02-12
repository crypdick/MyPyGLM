# -*- coding: utf-8 -*-
"""
Generate multivariate gaussian stimulus

for dimension 2, generate coord pair using selection from Gaussian fxn. 
repeat for as many points that you want

Created on Wed Feb 11 19:45:33 2015
@author: Richard Decal, decal@uw.edu
"""

    
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

NUMBER_EXPERIMENTS = 15
DIMENSIONS = 3

def Gaussian_generator(mean=0,stdev=1.0, dimensions = DIMENSIONS):
    return numpy.random.normal(loc=mean, scale=stdev, size = dimensions)

gaussianList = []

for i in range(NUMBER_EXPERIMENTS):
    gaussianList = np.concatenate((gaussianList, Gaussian_generator()), axis=0)

print gaussianList

#num_bins = 50
# the histogram of the data
#n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
#plt.show()