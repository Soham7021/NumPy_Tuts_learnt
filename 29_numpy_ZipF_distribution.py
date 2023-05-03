#ZipF : it used to find out for example a common word in english has occurs nearly 1/5 time as of the most hindi words this meas apan log 5 hindi word's ke bichme 1k english word nikal hi dete he uski probability find out kiyi jati he

#param : a(dist param),size
#sample with the a = 2 and size as 2*3
from numpy import random
a = random.zipf(a=2,size=(2,3))
print(a)


#visuualisation

import seaborn as sns
import matplotlib.pyplot as plt
s = random.zipf(a=2,size=1000)
# sns.distplot(random.zipf(a=2.size=(1000)),hist=False) ->we cant do this directly in the zipf as like other distribution we will have to store it first in another variable i.e shown as stored in variable s
sns.distplot(s,kde=False,label="not_deep")
plt.show()
#we can more deep analysis it mean's we can analysis with only the values between 0 to 10 it means it will show the block between the 0 to 10 only 
sns.distplot(s[s<10],kde=False,label="deep")
plt.show()