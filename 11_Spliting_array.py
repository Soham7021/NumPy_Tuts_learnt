#Spliting array is reversing to joining
import numpy as np 
a = np.array([1,2,3,4,5,6])
b = np.array_split(a, 3)
print("The splited array : ")
print(b)
import numpy as np 
a = np.array([1,2,3,4,5,6])
b = np.array_split(a, 4)
print("The not evenly splited array : ")
print(b)
#this will acces the first element of the array b
print(b[0])

#Spliting 2-D array : 
import numpy as np 
a = np.array([[1,2],[1,2],[1,2],[1,2]])
b = np.array_split(a, 2)
print("The splited array : ")
print(b)