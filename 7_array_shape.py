#shape of an array - it gives the no of element in an array in each direction's 

import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)#this will print (2,3) i.e it has 2dimension's and in each dimension it has 3 element's

#cheking for an multi dimensional arrya


import numpy as np 
b = np.array([1,2,3,4,5],ndmin=5)
print(b)
print((b.shape))
#this will print (1,1,1,1,5) that mean's there are 1 element in 5-d 1 in 4-d 1 in 3-d 1 in 2-d and 5 in 1-d