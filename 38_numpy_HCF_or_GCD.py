#finding the hcf highest common factor

import numpy as np
a = 6
b = 9
c = np.gcd(a,b)#we use gcd for finding out the highest common factor
print(c)

#finding the GCD in an array
#reduce() method will use the ufunc, in thid case the gcd() function on each element and it will reduce the array by 1-d

a = np.array([20,8,32,16,36,26])
b = np.gcd.reduce(a)
print(b)