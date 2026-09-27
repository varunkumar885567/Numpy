"""
np.insert(array,index,vaalue,axis=none)
index -
value-
axis=0,row-wise
1 colume wise

"""
import numpy as np
arr = np.array([10,20,30,40,50,60])
new_arr = np.insert(arr,2,25)
print(new_arr)


