#data types in python : string, interger, float, boolean, complex
#data type in numpy : 
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for String
# U for unicode string
# v - memory

#cheking the data type of the numpy array -dtype

import numpy as np 
a = np.array([1,2,3,4,5])
print(a.dtype)

# cheking for the string
import numpy as np
b = np.array(['soham','is','good','boy'])
print(b.dtype)#This is unicode string

#Creating thr array with a defined data type

import numpy as np
c = np.array([1,-2,-3,4],dtype="S")
#S is used to convert any datatype into the string
print(c)
print(c.dtype)

#converting data type in existing array using *astype()*
import numpy as np
check = np.array([1.5,2.3,5.6,-7])
check1 = check.astype('i')
check2 = check.astype(bool)
print(check1)
print(check2)
print(check.dtype)
print(check1.dtype)
print(check2.dtype)


