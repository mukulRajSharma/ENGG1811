#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

This file (run_all.py) will run all the four files that you have written to 
obtain a new design of the bridge. It will then simulate the new design 
and compare it the original design. 

"""

# %% Import 
import numpy as np 
import matplotlib.pyplot as plt

import run_different_designs as run
import find_best_design as best
import sim_bridge as sim 

# %% Original design of the bridge  
# Bridge and pedestrian parameters (Taken from Ref [2] of the assignment spec)
M = 1.13e5  # kg 
B = 1.10e4  # kg/s 
K = 4.73e6  # kg/s2
G = 30      # kgm/s2  
N = 20      # number of pedestrians 
C = 16      # /m/s  

# Initial condition  
dis0 = 0
vel0 = 0

# Start time, end time, and time increment 
time0 = 0 
time1 = 20
time_delta = 0.001
# time array 
t_array = np.arange(time0, time1, time_delta)

# Walking frequency of pedestrians are stored in Omega_whole 
# Extract the array according to the number of pedestrains
Omega_array_whole = np.loadtxt('ped_freq_array.txt')
Omega_array = Omega_array_whole[:N]
# Phase of the walking are stored in Phase_array_whole 
# Extract the array according to the number of pedestrains
Phase_array_whole = np.loadtxt('ped_phase_array.txt')
p0 = Phase_array_whole[:N]


# %% Run different designs and find the best design 
# Design parameters 
B_min = B
B_max = 4*B
K_min = K
K_max = 3*K
B_num = 8
K_num = 4

# Call your run_different_designs
B_array, K_array, sway_array = run.run_different_designs(
        t_array,M,G,N,C,Omega_array,dis0,vel0,p0,
        B_min,B_max,K_min,K_max,B_num,K_num)

B_new, K_new = best.find_best_design(sway_array, B_array, K_array)  
   
#%%  Simulate the original and new designs

# Original design 
dis_array_ori,vel_array_ori,ped_array_ori \
 = sim.sim_bridge(t_array,M,B,K,G,N,C,Omega_array,dis0,vel0,p0)

# New design 
dis_array_new,vel_array_new,ped_array_new \
 = sim.sim_bridge(t_array,M,B_new,K_new,G,N,C,Omega_array,dis0,vel0,p0)


# %% Plot the new and original displacements and velocities
plt.figure()
plt.subplot(2,1,1)
plt.plot(t_array,dis_array_ori,label='Original')
plt.plot(t_array,dis_array_new,label='New')
plt.xlabel('t')
plt.ylabel('displacement')
plt.legend()
plt.subplot(2,1,2)
plt.plot(t_array,vel_array_ori,label='Original')
plt.plot(t_array,vel_array_new,label='New')
plt.xlabel('t')
plt.ylabel('velocity')
plt.legend()
plt.show()

