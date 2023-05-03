#pareto : it is called as 80:20 ration in which 20%factor cause 80% outcome or result(20% ki mehenat 80 percent ka result deti he)

#param-a(shape),size

#sample will be with a i.e shape as 2 and size 2*3
from numpy import random
a = random.pareto(a=2,size=(2,3))
print(a)


#visualisation

import seaborn as sns 
import matplotlib.pyplot as plt
sns.distplot(random.pareto(2,size=(1000)),hist=False)#we can also do kede = false for building of graphs
plt.show()
#this graph will be max at the scaling 2