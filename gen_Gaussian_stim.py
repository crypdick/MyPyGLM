# -*- coding: utf-8 -*-
"""
Generate multivariate gaussian stimulus

for dimension 2, generate coord pair using selection from Gaussian fxn. 
repeat for as many points that you want

Created on Wed Feb 11 19:45:33 2015
@author: Richard Decal, decal@uw.edu
"""

numberlist = []

for i in range(100):
    numberlist.append( numpy.random.normal(loc=0, scale=1.0, size = None) )
    
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# example data
mu = 0 # mean of distribution
sigma = 10 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.show()