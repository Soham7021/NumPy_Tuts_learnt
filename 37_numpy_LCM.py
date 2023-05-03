# lcm:lowest common multiple
#here we will find the lcm of the 2number's:

import numpy as np
a = 4
b = 6
c = np.lcm(a,b)
print(c)

#finding the lcm in array
a = np.array([3,6,9])
b = np.lcm.reduce(a)#reduce() method will use the ufunc, in thid case the lcm() function on each element and it will reduce the array by 1-d
print(b)
#we will only use reduce() function in array's

#we will find the lcm of all on array where the array contains all integers from 1 to 10. 

a = np.arange(1,11)
b = np.lcm.reduce(a)
print(b)
# print(a)