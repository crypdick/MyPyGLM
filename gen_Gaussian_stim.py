# -*- coding: utf-8 -*-
"""
Generate multivariate gaussian stimulus

for dimension 2, generate coord pair using selection from Gaussian fxn. 
repeat for as many points that you want

Created on Wed Feb 11 19:45:33 2015
@author: Richard Decal, decal@uw.edu
"""

    
import numpy as np
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


NUMBER_EXPERIMENTS = 1
DIMENSIONS = 3000

def Gaussian_generator(mean=0,stdev=1.0, dimensions = DIMENSIONS):
    return np.random.normal(loc=mean, scale=stdev, size = dimensions)

#initialize list with a row of zeros
gaussianList = np.array([np.zeros(DIMENSIONS)])


for i in range(NUMBER_EXPERIMENTS):
    """make a new row of length DIMENSIONS for each experiment"""
    newpt = np.array([Gaussian_generator()])
    gaussianList = np.concatenate((gaussianList, newpt), axis=0)

#==============================================================================
#plot the gaussian cloud
#the [1:, skips the first row of the data, which is just a hack to skip all the zeros
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#xs = gaussianList[1:,0]
#ys = gaussianList[1:,1]
#zs = gaussianList[1:,2]
#ax.scatter(xs, ys, zs)
#plt.show()
#==============================================================================


#==============================================================================
####### store the numpy array
#np.savetxt("gauss_stimulus_3000dim.txt", gaussianList[1:,:])
#==============================================================================
