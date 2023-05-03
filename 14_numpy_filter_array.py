#getting some ele out of the existing array and storing it in another array is called as filtering
#boolean index list is an list of boolean corresponding to indexes in the array i.e true and false
#create an array from the element on index 0 to 2
import numpy as np
a = np.array([2,4,5,6])
b = np.array([True,False,True,True])
c = a[b]#this is like injective marking i.e assining the boolean values to the upper array i.e 2->True,4->False.......
print(c)#this will now only print the only true values i.e 2,5,6 i.e only true values are printed


#let's creat an filter array wich will print the values greater than 6
a = np.array([5,7,2,6,9,8,4,2,6,5,1,45])
empt = []
for i in a:
    if(i>6):
        empt.append(True)#we are not directly appeding the element in the filter array instead we are passing the boolean value
    else:
        empt.append(False)
c = a[empt]
print(empt)#this will print the boolean array 
print(c)#this will print the actual filtered array


#now directly filtering above without for loop
print('_-_-____-_-_-____--_--')
a = np.array([5,7,2,6,9,8,4,2,6,5,1,45])
empt = a>6
c = a[empt]
print(empt)
print(c)
print("_-_-_-_-_-_-____-_____-_-_-___-_______-_-_-_-_-")
#let's play
a = np.array([4,5,9,6,2,5,7,8])
b = []
for i in a:
    if(i%2==0):
        b.append(True)
    else:
        b.append(False)
print(b)
c = a[b]
print(c)