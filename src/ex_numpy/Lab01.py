import numpy as np
# a = np.array([1,2,3])
# print(a)

# b = np.array([(1,2,3),(4,5,6)])
# print(b)

# c = np.array([1,2,3,4,5],ndmin=2)
# print(c)

# import numpy as np
# d = np.array([1,2,3,4,5], dtype=complex)
# print(d)

import time
import sys
S = range(1000)
print(sys.getsizeof(5)*len(S))

D=np.arange(1000)
print(D.size*D.itemsize)
