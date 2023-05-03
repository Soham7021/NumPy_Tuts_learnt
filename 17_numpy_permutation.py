#permutation refers to an arrangement of elements like [3,2,1] to any arrangement like [2,1,3] ........
#the numpy random module provides 2 methos: " shuffle() and permutation()  "
# 
# now let's randomly shuffle the array let's go : 

from numpy import random
import numpy as np
#shuffling method's make's changes in the original array 
print("This is for the Shuffling : ")
a = np.array([1,2,3,4])
print(a)#this will print our given array 
random.shuffle(a)
print(a)#this will print our shuffled array

print("This is for the Permutation : ")
a = np.array([1,2,3,4])
print(a)
random.permutation(a)#this will not change the original array to do so either we have to store it in another variable or direclty print it
print(a)
print(random.permutation(a))#this will give the output correclty withe the different arrangement's
