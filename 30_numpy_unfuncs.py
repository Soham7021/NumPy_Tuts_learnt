# ufunc :  stands for universal function and they are actually numpy function's that operates on the ndarray
#ufunc also takes additionl argument's like where,dtype and out
#vectorization : converting the iterative statement's in the vector based staatement

#example without ufunc here we will use python inbuilt we wil use zip()
#zip is used fo rparallel iteration
x = [1,2,3,4]
y = [4,5,6,7]
z = []
for i, j in zip(x,y):#i.e i for x and j for y is given by the inbuilt function zip
    z.append(i+j)
print("This is wihtout ufunc i.e normal python : ",z)

#now we will do this above code with the help of  ufunc
import numpy as np 
x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print("This is using ufunc i.e using numpy : ",z)