#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Template file for find_best_design(). 

"""

import numpy as np 

def find_best_design(sway_array,B_array,K_array):
    
    B_chosen = B_array[np.where(sway_array == np.min(sway_array))[0][0]]
    K_chosen = K_array[np.where(sway_array == np.min(sway_array))[1][0]]
    return B_chosen, K_chosen 


