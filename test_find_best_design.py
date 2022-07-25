#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T2 Assignment 2 

Test file for find_best_design(). 

There are 6 tests. Tests 3-5 need the following data files:
    test_find_best_design_ref_data_3.npz
    test_find_best_design_ref_data_4.npz
    test_find_best_design_ref_data_5.npz

"""

import numpy as np 
import find_best_design as best

# %% Use test_num to choose the test
test_num = 2 # 0, 1, 2, 3, 4 or 5

if test_num == 0:
    sway_array = np.array([[3.1, 2.1, 1.1],
                           [4.1, 1.6, 2.4],
                           [2.2, 3.2, 3.6],
                           [1.5, 2.5, 3.5]])
    B_array = np.array([3.7, 4.7, 5.7, 6.7])
    K_array = np.array([1.5, 1.8, 2.1])
    B_expected = B_array[0]
    K_expected = K_array[2]

   
elif test_num == 1:
    sway_array = np.array([[3.1, 2.1, 2.9],
                           [4.1, 1.7, 2.7],
                           [2.2, 3.2, 3.6],
                           [1.5, 0.9, 1.9]])
    B_array = np.array([3.7, 4.0, 4.3, 4.6])
    K_array = np.array([1.5, 1.8, 2.1])
    B_expected = B_array[3]
    K_expected = K_array[1]

elif test_num == 2:
    sway_array = np.array([[3.1, 2.1, 2.9, 4.1],
                           [4.1, 2.7, 0.7, 3.6],
                           [2.2, 3.2, 3.6, 9.9]])
    B_array = np.array([2.7, 3.1, 3.5])
    K_array = np.array([6.5, 6.8, 7.1, 7.4])
    B_expected = B_array[1]
    K_expected = K_array[2]

elif test_num == 3: 
    ref_data = np.load('test_find_best_design_ref_data_3.npz')
    sway_array = ref_data['sway_BK'] # (3,4) 
    B_array = ref_data['B_array']  
    K_array = ref_data['K_array'] 
    B_expected = ref_data['B_new']
    K_expected = ref_data['K_new']
    
elif test_num == 4:
    ref_data = np.load('test_find_best_design_ref_data_4.npz')
    sway_array = ref_data['sway_BK'] # (6,4)
    B_array = ref_data['B_array']  
    K_array = ref_data['K_array'] 
    B_expected = ref_data['B_new']
    K_expected = ref_data['K_new']
    
elif test_num == 5:
    ref_data = np.load('test_find_best_design_ref_data_5.npz')
    sway_array = ref_data['sway_BK'] # (5,10)
    B_array = ref_data['B_array']  
    K_array = ref_data['K_array'] 
    B_expected = ref_data['B_new']
    K_expected = ref_data['K_new']    
      
# Compute the objective value     
B_your, K_your = best.find_best_design(sway_array, B_array, K_array)  

# Compare against the reference

# Calculate the difference between your output and the reference output
diff_B = np.abs(B_your - B_expected)
print('B: The absolute difference between your output and the reference output is: ',diff_B)

diff_K = np.abs(K_your - K_expected)
print('K: The absolute difference between your output and the reference output is: ',diff_K)  

    
