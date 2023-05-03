#rounding the decimal : there are 5 ways of rounding off the dicimal in numpy: truncation,fix rounding ,floor,cell. 

#truncation : trunc() and fix()
#here we are truncating the below array , these command remove the decimals and return the float number closest to zero
#thus we have used the truc though this will round this in float valuess 
#use truc the most it's more convineent
import numpy as np
a = np.trunc([-3.1666,3.667])
print(a)
a = np.fix([-3.1666,3.667])
print(a)


#rounding : the around() function increments the preceding digit or decimal by nearest to 1: n>5=1 or n<5=0

a = np.around(5.64587,3)#the second argument shows the how many digit's will be there after the decimal point
print(a)

#floor() : it will round the decimal to the lower integer
a = np.floor([-3.1666,3.667])
print(a)
#cell(): it rounds the decimal to the upper interger
a = np.ceil([-3.1666,3.667])
print(a)