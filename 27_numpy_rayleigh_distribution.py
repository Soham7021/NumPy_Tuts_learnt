#Rayleigh dist: it is used in signal provessing
#param = scale(standard deviation,how flat the distribution is , defauls is 1.0),size()

#we will take a sample with scale of 2.0 and size of 2*3

from numpy import random
a = random.rayleigh(scale=2,size=(2,3))
print(a)


#visualisatrion

import seaborn as sns 
import matplotlib.pyplot as plt
sns.distplot(random.rayleigh(scale=2,size=(1000)),hist=False)
plt.show()

#the curve will be max at the point of sclaing in this example the grapth will ghanta at the point 2