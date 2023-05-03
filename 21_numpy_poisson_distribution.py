# poisson distribution - it tells how many time the event can occur
#parameters -> lam(the no of times the event can ocur),size

#gnerate of random 1*10 distribution of occurence 2

from numpy import random
a = random.poisson(lam=2,size=10)
print(a)

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()


#finding the difference in normal and poisson distribution

sns.distplot(random.normal(loc=50,scale=7,size=1000),hist=False,label="normal")
sns.distplot(random.poisson(lam=50,size=1000),hist=False,label="poisson")

plt.show()