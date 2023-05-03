# creating ndarray using numpy
import numpy as np
x = np.array([1,2,5,4,6,8])
print(x)
print(type(x))
print(x.ndim)
# we can also pas a list, tuple or any array like object with array(). and it will be coverted to ndarray
# it will always change the data type of anyhting in the arrray type if you pass the arrray in the np.array it will convert it into array and display it as array
import numpy as np 
y = np.array((1,2,3,4,6,8))
print(y)
print(type(y))
print(y.ndim)

#Dimension's in the array

# 0-D array
import numpy as np
a = np.array(15)
print(a)
print("Dimension's of the arry : ",a.ndim)

# 1-D array
import numpy as np
b = np.array([1,2,5,4,5,85,5])
print(b) 
print(b.ndim)
print("-_-_-_-_-_-_-_-_-_-_-_")
# 2-D array
import numpy as np
print("This is 2-D array")
c = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(c)
print("Dimension's of the arry : ",c.ndim)

# 3-D array
import numpy as np
print("This is 3-D array")
d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(d)
print("Dimension's of the arry : ",d.ndim)

# Create an array with dimension that you want.
e = np.array([1,2,3],ndmin=5)
print(e)
print("Dimension's of the arry : ",e.ndim)