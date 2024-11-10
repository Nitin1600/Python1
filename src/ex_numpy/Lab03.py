# import numpy as np
# a = np.array([(1,2,3),(4,5,6)])
# print(a.ndim)

# import numpy as np
# b = np.array([(1,2,3)])
# print(b.itemsize)

# import numpy as np
# c = np.array([(1,2,3)])
# print(c.dtype)

# import numpy as np
# a = np.array([(1,2,3,4,5,6)])
# print(a.size)
# print(a.shape)
#
# import numpy as np
# a = np.array([(8,9,10),(11,12,13)])
# print(a)
# a = a.reshape(3,2)
# print(a)

# import numpy as np
# a = np.array([(1,2,3,4),(5,6,7,8)])
# print(a[0,2])
# print(a[0:,2])
#
# import numpy as np
# a = np.array([(1,2),(3,4),(5,6)])
# print(a[0:1,1])

# import numpy as np
# a = np.linspace(1,3,10)
# print(a)

# import numpy as np
# a = np.array([(1,2,3)])
# print(a.max())
# print(a.min())
# print(a.sum())

# import numpy as np
# a = np.array([(1,2,3),(4,5,6)])
# print(a.sum(axis=1))

# import numpy as np
# a = np.array([(1,2,3),(4,5,6)])
# print(np.sqrt(a))
# print(np.std(a))

# import numpy as np
# x = np.array([(1,2,3),(4,5,6)])
# y = np.array([(7,8,9),(10,11,12)])
# # print(x+y)
# # print(x-y)
# # print(x*y)
# # print(x/y)
# print(np.vstack((x,y)))
# print(np.hstack((x,y)))
# print(x.ravel())

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0,3*np.pi,0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0,3*np.pi,0.1)
# y= np.tan(x)
# plt.plot(x,y)
# plt.show()

# import numpy as np
# a = np.array([1,2,3])
# print(np.exp(a))

import numpy as np
import matplotlib.pyplot as plt
a = np.array([1,2,3])
print(np.log(a))

import numpy as np
import matplotlib.pyplot as plt
a = np.array([1,2,3])
print(np.log10(a))
