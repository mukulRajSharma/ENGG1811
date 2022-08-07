#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Template file for run_different_designs(). 

"""

import numpy as np
import sim_bridge as sim 
import comp_obj as obj

def run_different_designs(t_array,M,G,N,C,Omega_array,dis0,vel0,ped0,
                          B_min,B_max,K_min,K_max,B_num=5,K_num=10):

    B_array = np.linspace(B_min, B_max, B_num)
    K_array = np.linspace(K_min, K_max, K_num)

    sway_array = np.zeros((len(B_array),len(K_array)))
    for i in range(0, len(B_array)):
        for j in range (0, len(K_array)):
            dis_array, vel_array, ped_array = sim.sim_bridge(t_array,M,B_array[i],K_array[j],G,N,C,Omega_array,dis0,vel0,ped0)
            max_val = obj.comp_obj(dis_array,vel_array,M,K_array[j])
            sway_array[i][j] = max_val

    return B_array, K_array, sway_array  
