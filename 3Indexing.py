#indexing in the numpy
#it is same as the list indexing 
#indexing in the 1-D array
import numpy as np 
a =  np.array([1,2,3,4])
print(a[0])
print(a[1]+a[3])

#indexing in the 2-D array
import numpy as np
b = np.array([[1,2,3],[1,2,3]])
print(b[1,2])
#we can also acces it like this
print(b[1][2])
print(b[0,1] + b[1,2])
#we can also write it like this
print(b[0][1] + b[1][2])


#indexing in the 3-D array
import numpy as np 
c = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(c)
print(c[0,1,2])
#we can also acces it like this
print(c[1][0][2])
print(c[0,1,2]+ c[1,1,2])