# -*- coding: utf-8 -*-
"""
A generalized linear model
Created on Fri Jan 09 15:59:12 2015

@author: Richard
"""

#==============================================================================
# PSEUDO CODE
#==============================================================================
# fxn takes stimulus, stim filter, response filter, nonlinearity
# loop for timestep in t:
#       1. calc filtered signal, convolution of stimulus with its filter to get response r_s
#       2. calc filtered output, apply output filter to r_s.
#       3. r_both = r_s + r_y
#       4. y at next time step y_(ts+1) = g(r_both)  
#==============================================================================
