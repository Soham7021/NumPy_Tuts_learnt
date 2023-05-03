#chi square : it is basically used as a basis to verify the hypothesis
#param : def(degree of freedom),size(shape of returned array
# sample for chi squared dist with dof = 2 with size 2*3


from numpy import random
a = random.chisquare(2,size=(2,3))
print(a)

#visualisation
import seaborn as sns 
import matplotlib.pyplot as plt
sns.distplot(random.chisquare(1,size=(1000)),hist=False)
plt.show()