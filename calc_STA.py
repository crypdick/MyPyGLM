# -*- coding: utf-8 -*-
"""
Spike Triggered Average calculator

Input:
stimulus (t)
spike spikeTimes (t)
    if no spiketimes, generate randoms

output:
averaged stimulus before the spiketime


Created on Wed Feb 11 21:20:00 2015
@author: Richard Decal, decal@uw.edu
"""

import numpy as np
import matplotlib.pyplot as plt

def gen_rand_spiketimes(number_of_spikes, STIM_LEN):
    """given stimulus length and stim count, generate 10 random spikes
    
    TODO: make this a poisson process
    TODO: don't have random spiketimes: spike when convolution tells you to!"""
    rand_spike_times = np.zeros(STIM_LEN)
    timebins = []
    for i in range(number_of_spikes):
        timebin = np.random.randint(low=0, high=STIM_LEN-1)
        rand_spike_times[timebin] = 1
        timebins.append(timebin)
    return rand_spike_times, timebins

def window_grabber(stimulus, spikeTimes, WINDOW_LEN):
    """"when we have a spike, grab the window
    
    return an array of each window
    TODO: instead of discarding spikes at beginning, make vector with leading zeros??"""
    spike_trigger_windows = []
    for time in spikeTimes:
        if time > WINDOW_LEN: #discard spikes that are too close to the beginning.
            spike_trigger_windows.append(stimulus[time-WINDOW_LEN:time])
    spike_trigger_windows = np.array(spike_trigger_windows)
    return spike_trigger_windows

def spike_trigger_averager(spike_trigger_windows):
    """given a list of TODO, return a single averaged vector"""    
    spike_trigger_average = np.average(spike_trigger_windows, axis=0)
    return spike_trigger_average

def figplotter(WINDOW_LEN, spike_trigger_average):
    plt.plot(range(0,WINDOW_LEN), spike_trigger_average)
    plt.show()

def main(stimulus = np.genfromtxt("gauss_stimulus_3000dim.txt"), WINDOW_LEN = 50):
    """"
    default imports vector of len(3000) of pts drawn from a gaussian dist w/ mean=0,stdev=1.0
    
    TODO: allow input of spikes and spikeTimes, generate if none are available"""
    STIM_LEN = len(stimulus)
    spikes, spikeTimes = gen_rand_spiketimes(1000, STIM_LEN) #TODO: replace with calculated spiketimes
    spike_trigger_windows = window_grabber(stimulus, spikeTimes, WINDOW_LEN)
    spike_trigger_average = spike_trigger_averager(spike_trigger_windows)
    spike_trigger_windows
    return spike_trigger_average, WINDOW_LEN
    

if __name__ == "__main__":
    spike_trigger_average, WINDOW_LEN  = main()
    figplotter(WINDOW_LEN, spike_trigger_average)