import numpy as np 
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b))
d = np.concatenate((b,a))
print(c)
print(d)

#joining of 2-D array's along with axits = 1

import numpy as np
e = np.array([[1,2],[3,4]])
f = np.array([[5,6],[7,8]])
g = np.concatenate((e,f),axis = 1)
print(g)

#joining array using stack
import numpy as np
e = np.array([1,2,3])
f = np.array([4,5,6])
g = np.stack((e,f),axis = 1)
print(g)

#stacking using rows : hstack
print("Result of hstack i.e row major")
import numpy as np
e = np.array([1,2,3])
f = np.array([4,5,6])
g = np.hstack((e,f))
print(g)
#stacking using coloumns : vstack
print("Result of vstack i.e column major")
import numpy as np
e = np.array([1,2,3])
f = np.array([4,5,6])
g = np.vstack((e,f))
print(g)

#stacking along with height depth 
print("Result of dstack i.e height depth major")
import numpy as np
e = np.array([1,2,3])
f = np.array([4,5,6])
g = np.dstack((e,f))
print(g)