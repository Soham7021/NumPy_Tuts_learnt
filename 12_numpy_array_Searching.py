# Searching an element's in the array using inbuilt where in numpy

import numpy as np 
a = np.array([1,2,3,4,4,4,5,6,5,4,4])
b = np.where(a == 4)#this will give the index of 4 present in the a
print(b)

import numpy as np 
c = np.array([1,2,3,4,4,4,5,6,5,4,4])
d = np.where(c%2==0)#this will give the index of 4 present in the a
print(d)

#searchsorted () - performs the binary search in array
import numpy as np
e = np.array([2,5,6,3,5,9,5,8,4,2,2])
b = np.searchsorted(e, 9)
print(b)


import numpy as np
e = np.array([2,9,6,3,5,8,5,8,4,2,2])
b = np.searchsorted(e, 9,side="right")#this will give indexing from the right side
print(b)

# searching multiple values :-
# inserting the values 
#liitle bit complex to understand
import numpy as np
g = np.array([1,4,5,8,7,2,6])
h = np.searchsorted(g, [2,4,6])
print(h)