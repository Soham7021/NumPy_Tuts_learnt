# int = randint
# float = rand

import numpy as np
from numpy import random
a = random.randint(100)#it will give any random number till 100
print(a)
b = random.randint(100,200)
print(b)
e = random.randint(100,size=(5))
print(e)#generating random array with size 5
e = random.randint(100,size=(3,5))#this is 2d array with size 5
print(e)
e = random.randint(100,size=(2,3,5))#3d array
print(e)
c = random.rand()#if value is not pass it will only give random value from 0 to 1
print(c)
d = random.rand(10)#it will print any 10 random values from 0 to 1
print(d)

c = random.rand(3,5)
print(c)

a = random.choice([2,5,8,7,2,2,6,8,4,1,5,5,5,5,5,54,4,10])
print(a)#this will print any random values from the above array

b = random.choice([4,5,8,7],size = (3,5))#this will make the array of three rows and 5 coloums containing any random values from the given array
print(b)