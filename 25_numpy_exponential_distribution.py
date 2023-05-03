#exponential : it is used for descibing the time till next event
#param : scale(inverse of rate(see lam in poisson dist)),size()

#here we will draw a sample for exponential dist with 2.0 scale and 2*3 size

from numpy import random
a = random.exponential(scale=2,size=(2,3))
print(a)

#visualisation
import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(random.exponential(size=(1000)),hist=False)
plt.show()

#poisson deals with number of occurence and exponential find out probability of time between two event
