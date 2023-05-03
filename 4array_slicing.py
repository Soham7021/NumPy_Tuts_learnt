#slicing means playing with the element's of the array 

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[5:])
print(a[2::2])
print(a[-3:-1])
print(a[-3:1:-1])

#Slicing in the 2-D array
import numpy as np
b = np.array([[1,2,3],[1,2,3]])
print(b[1,1:3])
print(b[0:1 , 2])
#0:1 will the 2nd elemnt of the 1st row and 2 will print 3rd element in the 2nd row
print(b[0:2,1:3])#here what happend is 0:2 denotes both row means slice 0th and the 1st row form 1 to 3rd element i.e is given by 1:3(this will take 1 to 3rd element's from both the row's)
#we can also acces the element's of the rows at a time using this type of syntax

#only which row has to be sliced is to be mensioned otherwise everything is same as 1-D array

#slicing in the 3-D element's 
import numpy as np
c = np.array([[[1,2,7],[4,5,8]],[[1,2,3],[4,5,6]]])
print(c[1,0:2,2])#this mean's 2rya row cha 2nhi row che 3rd 3rd element's i.e 3 ani 6 print hotil
#this is how we can slice the 3-D array
print(c[0:2,0:2,2])