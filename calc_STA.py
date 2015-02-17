# -*- coding: utf-8 -*-
"""
Spike Triggered Average calculator

Input:
stimulus (t)
spike times (t)
    if no spiketimes, generate randoms

output:
averaged stimulus before the spiketime


Created on Wed Feb 11 21:20:00 2015
@author: Richard Decal, decal@uw.edu
"""

import numpy as np
import matplotlib.pyplot as plt

def gen_rand_spiketimes(number_of_spikes, STIM_LEN):
    """given stimulus, generate 10 random spikes"""
    rand_spike_times = np.zeros(STIM_LEN)
    timebins = []
    for i in range(number_of_spikes):
        timebin = np.random.randint(low=0, high=STIM_LEN-1)
        rand_spike_times[timebin] = 1
        timebins.append(timebin)
    return rand_spike_times, timebins

def window_grabber(stimulus, times, WINDOW_LEN):
    """"when we have a spike, grab the window
    
    TODO: instead of discarding spikes at beginning, make vector with leading zeros??"""
    spike_trigger_windows = []
    for time in times:
        if time > WINDOW_LEN: #discard spikes that are too close to the beginning.
            spike_trigger_windows.append(stimulus[time-WINDOW_LEN:time])
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
    TODO: allow input of spikes and times, generate if none are available"""
    STIM_LEN = len(stimulus)
    spikes, times = gen_rand_spiketimes(1000, STIM_LEN)
    spike_trigger_windows = window_grabber(stimulus, times, WINDOW_LEN)
    spike_trigger_average = spike_trigger_averager(spike_trigger_windows)
    figplotter(WINDOW_LEN, spike_trigger_average)
    

if __name__ == "__main__":
    main()