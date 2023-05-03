#reshaping means changing the shape of an array like adding or removing the element

#reshaping from 1-D to 2-D
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(4,3)#the array will be divided into 4 1-D element's with 3 element's each
print(b)

#reshaping from 1-D to 3-D
import numpy as np
c = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d = c.reshape(2,2,3)#the array will be divided into 2 2-D element's with 2 1-D array's with 3 element's each
print(d)

import numpy as np
e = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
f = c.reshape(2,3,2)#the array will be divided into 2 2-D element's with 3 1-D array's with 2 element's each
print(d)

#Return copy or view
import numpy as np
g = np.array([1,2,3,4,5,6,7,8])
print(g.reshape(2,4).base)#if it's view then array will be printed as it is ex: [1,2,3,4,5,6,7,8]

#unknown dimension you are only allowed to have one unknown dimension .pass -1
import numpy as np
h = np.array([1,2,3,4,5,6,7,8])
i = h.reshape(2,2,-1)
print(i) 

#flattering the array by converting multidimensional array in 1-D
import numpy as np 
j = np.array([[1,2,3],[4,5,6]])
k = j.reshape(-1)# this will  bring evry type of array  dimension in one dimension ex : [1,2,3,4,5,6]
print(k)

#there are alot of function's for changing the shapes pf an array in numpy. like flatten, ravel and also rearranging the element rot90,flip,flilr,flipud.they all are actually comes under advanced numpy