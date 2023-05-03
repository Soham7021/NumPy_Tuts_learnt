#arithmatic operator's : +,-,/,*
#by using ufunc additional argument's like, where,dtype and out
#here now we will use add()

import numpy as np
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
c = np.add(a,b)
print(c) 

#similarly we will do it for substraction
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
c = np.subtract(b,a)
print(c)

#example of the multiplication
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
c = np.multiply(a,b)
print(c)

#example of the multiplication
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
c = np.divide(b,a)
print(c)
#above are the basic operation )

#now we will some extra
#power() this funciton raises the valuse from the 1st array to the power of the values of the 2nd array and return trhe results in a new array

a = np.array([10,20,30,40,50])
b = np.array([3,4,5,6,7])
c = np.power(a,b)
c = c.astype('int32')
print(c)

#remainder() : 1)mod() and 2)remainder() funciton return the remainder of the 1st array corrosponding to the 2nd array,and result in the new array. 

a = np.array([10,20,30,40,50])
b = np.array([3,4,5,6,7])
c = np.mod(a,b)
print(c)
d = np.remainder(a,b)
print(d)

#quotient and mod()re,remainder
#the divmod() function return both the quotient and mod.
a = np.array([10,20,30,40,50])
b = np.array([3,4,5,6,7])
c = np.divmod(a,b)#it display's both quotient and remainder
print(c)

#absolute() and abs() do the same operation but here we should use absolute() to avoid the confusion with python inbuilt function math.abs()

a = np.array([-10,-20,-30,-40,-50])
b = np.absolute(a)
print(b)