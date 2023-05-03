#Summation : difference: additoin is done between 2 argument's where as summation happend ovr n elemet

import numpy as np
a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.add(a,b)
print(c)

#sum the values in 2-d array : this output's the total sum of the arry of addition
a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.sum([a,b])
print(c)

#summation over an axis : if you specify axis = 1, numpy will sum the number in each array.a
a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.sum([a,b],axis=0)
d = np.sum([a,b],axis=1)
print(c)
print(d)

#cumulative sum : meas partially adding the element in the array. 
# example : [1,2,3,4] this would be [1,1+2,1+2+3,1+2+3+4] = [1,3,6,10]
#and it is represented as cumsum()

a = np.array([1,2,3,4])
b = np.cumsum(a)
print(b)