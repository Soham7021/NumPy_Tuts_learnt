# binomial distribution - discreate distribution - binary output
#param - n(number of trial's ) p(probability) size(shape)

#given 10 trials of coin's which will gnereate 10 data point's 

from numpy import random
a = random.binomial(n=10, p=0.5,size=10)
print(a)

#visualization of binomial 

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(random.binomial(n=10, p=0.5,size=1000),hist=True,kde=False)#kde brings the little bit of difference in the width of the buildings in the  graph
plt.show()

#difference between normal and binomial distribution
#normal(continues)   -    binomial(discreate)
#teacher uses 500 data point's for the binomial and under 100 data point's for the normal distribution