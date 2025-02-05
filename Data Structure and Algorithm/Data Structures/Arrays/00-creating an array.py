# Using array module

from array import array

arr = array('i')
print(type(arr))

arr1 = array('i', [1, 2, 3, 4, 5])
print(arr1[1])



#using numpy module

import numpy as np

np_arr = np.array([], dtype=int)
print(np_arr)

np_arr1 = np.array([1, 3, 5, 7, 9, 11])
print(np_arr1)