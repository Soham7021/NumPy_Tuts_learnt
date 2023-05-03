#product's : use prod() function for product
#here we will find the product of the element of the below array

import numpy as np
a = np.array([1,2,3,4])
b = np.prod(a)#1*2*3*4 = 24
print(b)

#here will will find the product of the elment in 2 different array: 

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.prod([a,b])# 1*2*3*4*5*6*7*8 = 40,320
print(c)


#product over an axis

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.prod([a,b],axis=1)#it will display the both product of array seperately
print(c) 

#cummulative product : 
#example the partial product of [1,2,3,4] i.2 = [1,1*2,1*2*3,1*2*3*4] = [1,2,6,24] and it is represented by cumprod().a

a = np.array([5,6,7,8])
b = np.cumprod(a)
print(b)