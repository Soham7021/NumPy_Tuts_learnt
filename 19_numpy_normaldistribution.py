#normall distribution is also caled as gaussian distribution
#we use normal.random() parameter-loc scale size

#we will generate a random normal distribution of size 2*3
from numpy import random
a = random.normal(size=(2,3))
print(a)#this is normal analysis

#we will gnerate normal distribution of size same and mean i.e loc(mean) 1

a = random.normal(loc=(1),scale=5,size=(2,3))
print(a)#this is deep analysis

#visualizaton of normal distribution

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=(1),scale=5,size=1000),hist=False)
plt.show()

#the curbe of the normal disst is also called as bell curv
