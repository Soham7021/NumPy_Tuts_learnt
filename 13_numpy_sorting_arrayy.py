#using sort sorting the array

import numpy as np
a=np.array([5,1,8,3,4])
b = np.sort(a)
print(b)#this method is like copy

# sorting the array alphabetically
c = np.array(["nasdlkf","sldkdf","dfler","sdkfld","defiof","reddsd"])
print(np.sort(c))

#sorting the 2-d array
a = np.array([[2,5,9,3],[4,8,3,2]])
print(np.sort(a))