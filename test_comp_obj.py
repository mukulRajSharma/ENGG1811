#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Test file for comp_obj(). 
"""

# import 
import numpy as np
import comp_obj as obj

# %% Use test_num to choose the test
test_num = 0 # 0, 1, 2, 3 or 4 

if test_num == 0:
    dis_array = np.array([-1.1, 2.1,3.1])
    vel_array = np.array([-4.1,-2.1,1.3])
    K = 1.1
    M = 4.2
   
elif test_num == 1:
    dis_array = np.array([-1.1, 2.1, 3.1])
    vel_array = np.array([ 1.3,-4.1,-2.1])
    K = 3.2
    M = 4.1

elif test_num == 2:
    dis_array = np.array([-1.1, 2.1, 3.1])
    vel_array = np.array([-2.1, 1.3,-4.1])
    K = 6.9
    M = 3.9

elif test_num == 3:
    ref_data = np.load('test_comp_obj_3.npz',
               allow_pickle=True)
    dis_array = ref_data['dis_array']
    vel_array = ref_data['vel_array']  
    M = 1.13e5   
    K = 4.73e6  
    
elif test_num == 4:
    ref_data = np.load('test_comp_obj_4.npz',
               allow_pickle=True)
    dis_array = ref_data['dis_array']
    vel_array = ref_data['vel_array']  
    M = 1.13e5   
    K = 3.43e6  
    
# Compute the objective value     
obj_value_your = obj.comp_obj(dis_array, vel_array, M, K)  

# Compare against the reference
# Load the correct answer
ref_file = np.load('test_comp_obj_ref_data.npz')
obj_value_array_ref = ref_file['obj_value_ref']
# Calculate the difference between your output and the reference output
diff_obj = np.abs(obj_value_your - obj_value_array_ref[test_num])
print('The absolute difference between your output and the reference output is: ',diff_obj)


      
