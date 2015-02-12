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
from mpl_toolkits.mplot3d import Axes3D


NUMBER_EXPERIMENTS = 10000
DIMENSIONS = 3

def Gaussian_generator(mean=0,stdev=1.0, dimensions = DIMENSIONS):
    return numpy.random.normal(loc=mean, scale=stdev, size = dimensions)

gaussianList = np.array([numpy.zeros(DIMENSIONS)])


for i in range(NUMBER_EXPERIMENTS):
    newpt = np.array([Gaussian_generator()])
    gaussianList = np.concatenate((gaussianList, newpt), axis=0)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = gaussianList[:,0]
ys = gaussianList[:,1]
zs = gaussianList[:,2]

ax.scatter(xs, ys, zs)
plt.show()