# to crate your own ufunc , you have to difine a funciton like you do in normal function in pythohn, then you add this function to the numpy function with frompyfucn() method
#arguments of frompyfunc(): function ,input's , outputs

#crate your own unfunc for addition

import numpy as np
def myadd(x,y):
    return x+y
myadd =  np.frompyfunc(myadd, nin=2, nout=1)#where nin and nout are not values this are the array's i.e 2 dimention array with out in one array
print(myadd([1,2,3,4], [5,6,7,8]))

#checking if this fucntion is ufunc or not

import numpy as np
print(type(np.add))#this will output type as ufunc i,e this is the ufucc

#concatenate() it also do the work of ufunc let's see it's type
print(type(np.concatenate))#this will show it is only a funciton it is not a ufunc

#what if ufunc does not exist
"""print(type(np.sdffsad))"""#use an if statement to check if the funcitons is a ufuc
if type(np.add) == np.ufunc:
    print("yes, this fucniton is ufucn")
else:
    print("this fucntion is not an ufunc")