# data distribution is a list of all possible values and how often each value occur's
# such list are imp when working with statistic's and data science
#Randdom distribution : Probability Function

# " Now we will generate 1-d array with 100 values where each value has to be 3,5,7,9



# the Probability for the values 3 is set to be 0.1
# the Probability for the values 5 is set to be 0.3

# the Probability for the values 7 is set to be 0.6

# the Probability for the values 9 is set to be 0.0
#always remenber "The sum of probabitlity must be 1 alway's i.e 0.1+0.3+0.6+0.0 == 1"

from numpy import random
a = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=100)#if you want to probability to the 0 then assign it like 0.0 i.e in float value
print(a)#this will print 100 values containing 3,5,7,9 according to probability repitation 

#similarly crate an 2-d array 
a = random.choice([4,7,8,9],p=[0.1,0.4,0.3,0.2],size=(3,5))
print(a)