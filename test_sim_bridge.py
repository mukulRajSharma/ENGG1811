#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Test file for sim_bridge() 

There are four cases. Use test_num to specify a test to run 

The correct outputs are stored in the file
    test_sim_bridge_ref_data.npz

"""

# %% Import 
import numpy as np 
import matplotlib.pyplot as plt

import sim_bridge as sim 

# %% Default parameter values 
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


# %% Choose a test to run using test_num 
test_num = 0 # 0, 1, 2 or 3 

if test_num == 0:
    # Default parameters are used unless overwritten
    G = 0; C = 0; dis0 = 0.4; vel0 = 0.1;
elif test_num == 1:
    # Default parameters are used unless overwritten
    C = 0;    
elif test_num == 2:
    pass # do nothing. Use default parameters 
elif test_num == 3:
    N = 50
    Omega_array = Omega_array_whole[:50]
    p0 = Phase_array_whole[:50]
    
# Run sim_bridge 
dis_bridge_your,vel_bridge_your,ped_bridge_your \
 = sim.sim_bridge(t_array,M,B,K,G,N,C,Omega_array,dis0,vel0,p0)

# %% Compare with reference 

# Load the reference data 
ref_data = np.load('test_sim_bridge_ref_data.npz',
                   allow_pickle=True)
dis_expected = ref_data['dis_bridge_ref']
vel_expected = ref_data['vel_bridge_ref']
ped_expected = ref_data['ped_bridge_ref']

# %%
# Compare dis_array
print('Checking the array dis_array ...')
if not dis_bridge_your.shape == dis_expected[test_num].shape:
    print('We expect an array of shape', dis_expected[test_num].shape)
    print('but your array has shape',dis_bridge_your.shape)
else: 
    max_abs_diff = np.max(np.abs(dis_bridge_your - dis_expected[test_num]))
    print('The maximum absolute difference is', max_abs_diff)
    # Plot the student's output and the expected output
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t_array,dis_bridge_your,label='Yours')
    plt.xlabel('t')
    plt.ylabel('displacement')
    plt.legend()
    plt.subplot(2,1,2)
    plt.plot(t_array,dis_expected[test_num],label='Expected')
    plt.xlabel('t')
    plt.ylabel('displacement')
    plt.legend()
    plt.show()
    
       
# Compare vel_array
print('Checking the array vel_array ...')
if not vel_bridge_your.shape == vel_expected[test_num].shape:
    print('We expect an array of shape', vel_expected[test_num].shape)
    print('but your array has shape',vel_bridge_your.shape)
else: 
    max_abs_diff = np.max(np.abs(vel_bridge_your - vel_expected[test_num]))
    print('The maximum absolute difference is', max_abs_diff)
    # Plot the student's output and the expected output
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t_array,vel_bridge_your,label='Yours')
    plt.xlabel('t')
    plt.ylabel('velocity')
    plt.legend()
    plt.subplot(2,1,2)
    plt.plot(t_array,vel_expected[test_num],label='Expected')
    plt.xlabel('t')
    plt.ylabel('velocity')
    plt.legend()
    plt.show()
    
# Compare ped_array
if test_num >= 1:
    print('Checking the array ped_array ...')
    if not ped_bridge_your.shape == ped_expected[test_num].shape:
        print('We expect an array of shape', ped_expected[test_num].shape)
        print('but your array has shape',ped_bridge_your.shape)
    else: 
        max_abs_diff = np.max(np.abs(ped_bridge_your - ped_expected[test_num]))
        print('The maximum absolute difference is', max_abs_diff)

        # Plot the student's output and the expected output
        # 
        plt.figure()
        plt.subplot(2,1,1)
        plt.plot(t_array,np.transpose(np.sin(ped_bridge_your)))
        plt.xlabel('t')
        plt.ylabel('Force')
        plt.title('Force per pedestrians')
        plt.subplot(2,1,2)
        plt.plot(t_array,np.transpose(np.sin(ped_expected[test_num])))
        plt.xlabel('t')
        plt.ylabel('Force')
        plt.title('Force per pedestrians')
        plt.show()
            
