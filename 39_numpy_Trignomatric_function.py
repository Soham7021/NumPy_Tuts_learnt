#Trignometric Fucntion :  we take the values in randian 

#here we will find the sin value of pi/2
import numpy as np
a = np.sin(np.pi/2)
print(a)

#now we will find the sin values of an array

a = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5,])
b = np.sin(a)
print(b)

#conver degree into radian : by default all of the trigno function takes radians as parameter.
#radian's values are pi/180* degree valuess
#here we will convert all the array values to radians : 

a = np.array([90,180,270,360])
b = np.deg2rad(a) #wee have, converted the degree into radian
c = np.sin(b)
print(b)
print(c)


#here we will convert the radian into degree
a = np.array([np.pi/2,np.pi,np.pi,1.5*np.pi,2*np.pi])
b = np.rad2deg(a)
print(b)


#here we can also find the angles : arcsin(),arccos(),arctan() which takes the values i radians and produce the corresponding sin,cos and tan values

#we will now find the angle of 1.0
a = np.arcsin(1.0)
print(a)

# angles of each values in an array : 
a = np.array([1,-1,0.1])
b = np.arcsin(a)
print(b)

#here we can also find the hypotenous using the pythagoras theorem  in numpy
#hypot() function that takes values in radians and produce the correspondig sin,cos and tan values. 

#here we will find hypot for 3 base and 4 perpendicular. 
base = 3
perp = 4
a = np.hypot(base,perp)
print(a)
#this will give the hypoteneous value
