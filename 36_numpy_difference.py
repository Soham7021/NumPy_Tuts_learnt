#difference : use of diff() fucntion for finding the difference 
#example : [1,2,3,4] the deiscreate diiference of this would be [2-1,3-2,4-3] = [1,1,1] by using diff()

import numpy as np
a = np.array([10,15,25,5])#
b = np.diff(a)
print(b)
