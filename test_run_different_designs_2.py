#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Test file #2 for run_different_designs().

The correct answers are stored in test_run_different_designs_ref_data_2.npz
"""

import numpy as np 
import run_different_designs as run 

# % Parameter values needed 
M = 1.13e5  # kg 
B = 1.10e4  # kg/s 
K = 4.73e6  # kg/s2
G = 30      # kgm/s2  
N = 20   # number of pedestrians 
C = 16      # /m/s , 
dis0 = 0
vel0 = 0
time0 = 0 # integration limits for t
time1 = 20
time_delta = 0.001

Omega_array_whole = np.loadtxt('ped_freq_array.txt')
Omega_array = Omega_array_whole[:N]
Phase_array_whole = np.loadtxt('ped_phase_array.txt')
p0 = Phase_array_whole[:N]

t_array = np.arange(time0, time1, time_delta)

B_min = B
B_max = 3*B
K_min = K
K_max = 3*K
# Note: Use defafault B_num, K_num 

# Call your run_different_designs
B_array_your, K_array_your, sway_array_your = run.run_different_designs(
        t_array,M,G,N,C,Omega_array,dis0,vel0,p0,
        B_min,B_max,K_min,K_max)

# Load reference data for comparison 
ref_data = np.load('test_run_different_designs_ref_data_2.npz')
sway_array_expected = ref_data['sway_BK'] 
B_array_expected = ref_data['B_array']  
K_array_expected = ref_data['K_array'] 

# Compare your array against the reference
# Compare B_array
print('Checking the array B_array ...')
if not B_array_your.shape == B_array_expected.shape:
    print('We expect an array of shape', B_array_expected.shape)
    print('but your array has shape',B_array_your.shape)
else: 
    max_abs_diff = np.max(np.abs(B_array_your - B_array_expected))
    print('The maximum absolute difference is', max_abs_diff)
    
# Compare K_array
print('Checking the array K_array ...')
if not K_array_your.shape == K_array_expected.shape:
    print('We expect an array of shape', K_array_expected.shape)
    print('but your array has shape', K_array_your.shape)
else: 
    max_abs_diff = np.max(np.abs(K_array_your - K_array_expected))
    print('The maximum absolute difference is', max_abs_diff)
    
# Compare sway_array
print('Checking the array sway_array ...')
if not sway_array_your.shape == sway_array_expected.shape:
    print('We expect an array of shape', sway_array_expected.shape)
    print('but your array has shape', sway_array_your.shape)
else: 
    max_abs_diff = np.max(np.abs(sway_array_your - sway_array_expected))
    print('The maximum absolute difference is', max_abs_diff)    
        
