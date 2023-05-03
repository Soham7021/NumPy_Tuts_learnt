#copy and view in the numpy
#copy int numpy

import numpy as np 
a = np.array([1,2,3,4,5])
b = a.copy()
b[0] = 8
print(a)
print(b)

#view in the numpy
print("_-__-__-__-__-__-__-__-__-__-__-__-__-_")
print("")
import numpy as np
c = np.array([5,4,7,8,9])
d = c.view()
d[0]=10#in view change the value of any of the c or d it will reflect in  both the arry's i.e c and d
print(c)
print(d)