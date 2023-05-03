#Set
#for creating teh set we use numpy's unique() method to find the unique element's from anu array: 

#here we will convert the array with repeted element's to a set

import numpy as np
a = np.array([1,2,3,3,4,5,6,6])
b = np.unique(a)
print(b)

#to find the unique values of 2 1-D array, we will use union1d() method.

a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
c = np.union1d(a,b)
print(c)

#finding the intersection values 
#we will use intersect1d()
a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
c = np.intersect1d(a, b,assume_unique=True)#if set is truw then the computation speed will be very high by using the assume_unique=True
print(c)

#to find the only values that are in 1st set and not present in the 2nd set : use setdiff1d

a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
c = np.setdiff1d(a, b,assume_unique=True)
print(c) 


#to find the only values that are not  present in both the sets use setxorld() method :

a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
c = np.setxor1d(a, b,assume_unique=True)
print(c)