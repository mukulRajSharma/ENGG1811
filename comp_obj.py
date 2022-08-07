#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Template file for comp_obj(). 
"""
import numpy as np 

def comp_obj(dis_array,vel_array,M,K): 
    return np.max((dis_array**2 + (M/K)*vel_array**2)**0.5)


