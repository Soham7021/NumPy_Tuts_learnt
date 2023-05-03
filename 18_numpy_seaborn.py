#seaborn is a subpart of the or the one module of the matpltolib 
#matplotlib(pyplot)- seaborn
#it is used to plot the graph's 

#Distplot - distribution plot(curve plot - histogram)

import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot([0,1,2,3,4,5])#we can use displot instead of distplot as it is going to be removed in future update of the python
plt.show()


#ploting the distplot without histogram
sns.distplot([0,1,2,3,4,5],hist=False)#this will remove the histogram from the graph
plt.show()