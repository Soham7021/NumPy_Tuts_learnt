#in hyperbolic we use sinh(),cosh(),tanh() and the values are alway's taken in the radian

#here we will find the value of sinh of pi/2 

import numpy as np
a = np.sinh(np.pi/2)
print(a)
#for the array's 

a = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5,])
b = np.cosh(a)
print(b)#we will have the 0.2 difference but the hyperbolic not convinient to use thus just use the simple trignometric function


#finding the angles : 
#here we can also find angles : arcsinh(),arccosh(), and  arctanh() that takes values in radians and produce the corresponding sinh(),cosh and tanh() values 

#we will now find the angles of 1.0 

a = np.arcsinh(1.0)
print(a)

#angles of each tanh() values in an array : 
a = np.array([0.1,0.2,0.5])
b = np.arctanh(a)
print(b) 