import numpy as np
print("1-D output :-")
a = np.array([1,2,3])
for i in a:
    print(i)
#iterate 2-d array
import numpy as np
print("2-D output :-")
b = np.array([[1,2,3],[4,5,6]])
for i in b:
    print(i)#this will output like [1,2,3]
                                # [4,5,60]
import numpy as np
#to acces all the elment from the array
print("2-D elements each by each : ")
c = np.array([[1,2,3],[4,5,6]])

for i in c:
    for j in i:
        print(j)

# iter 3 -D array
import numpy as np
print("3-D array : ")
d = np.array([[[1,2],[1,2]],[[3,4],[3,4]]])
for i in d:
    for j in i:
        for k in j:
            print(k)


#Iterating arrays using the nditer()
print("Direct Iterating using inbuild numpy")
import numpy as np
e = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(e):
    print(i)