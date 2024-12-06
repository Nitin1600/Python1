# # Single Dimensional array
import numpy as np
# a = np.array([1,2,3])
# print(a)
#
# Multi-Dimensional array
# a = np.array([(1,2,3),(4,5,6)])
# print(a)

#Minimum Dimensional array:
# a = np.array([1,2,3,4,5], ndmin=2)
# print(a)

#d-type array:
# a = np.array([1,2,3,4,5],dtype=complex)
# print(a)

# import numpy as np
# import time
# import sys
#
# S = range(1000)
# print(sys.getsizeof(5)*len(S))
#
# D = np.arange(1000)
# print(D.size*D.itemsize)

import sys
import time
SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start = time.time()
result = A1+A2
print((time.time()-start)*1000)