#logistic distribution - descibe growth and it is basically imp in regression and neaural network
#parameter's - loc(mean-0),scale(standard deviation 1) size

#draw 2*2 smaples of logistic with mean at 1 and scale 2

from numpy import random
a = random.logistic(loc=1,scale=2,size=(2,3))
print(a)


import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(random.logistic(size=1000),hist=False)
plt.show()