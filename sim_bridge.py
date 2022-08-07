#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Template file for sim_bridge(). 
"""

import numpy as np 

def sim_bridge(t_array,M,B,K,G,N,C,Omega_array,dis0,vel0,ped0): 

    # Time increment 
    dt = t_array[1] - t_array[0]

    # Initialise dis_array, vel_array, ped_array 
    dis_array = np.zeros_like(t_array)
    vel_array = np.zeros_like(t_array)
    ped_array = np.zeros((N,len(t_array)))

    # Initialise for index 0 
    dis_array[0] = dis0
    vel_array[0] = vel0
    ped_array[:,0] = ped0
    
    # Compute Y_0 (Eq 4)
    Y_0 = np.sqrt(K/M)

    # Your code to compute the entries in dis_array, vel_array, ped_array
    # 
    # Hint: Should use arctan2() from the numpy library to calculate Psi(t)

    for i in range(1, len(t_array)):
        dis_array[i] = dis_array[i-1] + vel_array[i-1]*dt
        
        summation = 0
        for p in range(0, N):
            summation += np.sin(ped_array[p][i-1])
        vel_array[i] = vel_array[i-1] + (-(B/M)*vel_array[i-1] - (K/M)*dis_array[i-1] + (G/M)*summation)*dt

        phase = np.arctan2(Y_0*dis_array[i], vel_array[i])

        for j in range(0, N):
            ped_array[j][i] = ped_array[j][i-1] + (Omega_array[j] + C*np.cos(phase - ped_array[j][i-1]))*dt

    # BEGIN: Supplied code  ************************************
    # Return the array    
    return dis_array, vel_array, ped_array
    # END: Supplied code  ************************************


