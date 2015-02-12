# -*- coding: utf-8 -*-
"""
Spike Triggered Average calculator

Input:
stimulus (t)
spike times (t)

output:
averaged stimulus before the spiketime


Created on Wed Feb 11 21:20:00 2015
@author: Richard Decal, decal@uw.edu
"""
import numpy as np

stimulus = np.genfromtxt("gauss_stimulus_3000dim.txt")
STIM_LEN = len(stimulus)
WINDOW_LEN = 5

def gen_rand_spiketimes(number_of_spikes):
    """given stimulus, generate 10 random spikes"""
    rand_spike_times = np.zeros(STIM_LEN)
    timebins = []
    for i in range(number_of_spikes):
        timebin = np.random.randint(low=0, high=STIM_LEN-1)
        rand_spike_times[timebin] = 1
        timebins.append(timebin)
    return rand_spike_times, timebins
        
spikes, times = gen_rand_spiketimes(5)

def window_grabber():
    spike_triggers = []
    for time in times:
        if time > WINDOW_LEN:
            spike_triggers.append(stimulus[time-WINDOW_LEN:time])
        else:
            spike_triggers.append(stimulus[0:time])
    return spike_triggers
    
spike_triggers = window_grabber()
spike_trigger_average = np.average(spike_triggers, axis=0)
