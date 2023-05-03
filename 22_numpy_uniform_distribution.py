#uniform distribution - if is only made for probability
#parameter's - a(lowr bound),b(upper bound),size

from numpy import random
a = random.uniform(size=(2,3))
print(a)


#visialisation
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(random.uniform(size=1000),hist=False)
plt.show()