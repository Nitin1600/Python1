import numpy as np
# a = np.array([(1,2,3),(4,5,6)])
# print(a.ndim)

# a = np.array([(1,2,3,4,5,6)])
# print(a.itemsize)
# print(a.dtype)
# print(a.shape)
# print(a.size)

# a = np.array([(1,2,3),(4,5,6)])
# print(a)
# a = a.reshape(3,2)
# print(a)

# import numpy as np
# a = np.array([(1,2,3,4),(3,4,5,6)])
# print(a[1,2])
# print(a[0:,3])

# import numpy as np
# a = np.array([(1,2),(3,4),(5,6)])
# print(a[0:2,1])

# import numpy as np
# a = np.linspace(1,3,10)
# print(a)

# import numpy as np
# a = np.array([(1,2,3)])
# print(a.min())
# print(a.max())
# print(a.sum())

# a = np.array([(1,2,3),(3,4,5)])
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# a = np.array([(1,2,3),(3,4,5)])
# print(np.sqrt(a))
# print(np.std(a))

# import numpy as np
# x = np.array([(1,2,3),(3,4,5)])
# y = np.array([(1,2,3),(3,4,5)])
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

# import numpy as np
# x = np.array([(1,2,3),(3,4,5)])
# y = np.array([(1,2,3),(3,4,5)])
# print(np.vstack((x,y)))
# print(np.hstack((x,y)))

# import numpy as np
# x = np.array([(1,2,3),(3,4,5)])
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
# y = np.tan(x)
# plt.plot(x,y)
# plt.show()

# a = np.array([1,2,3])
# print(np.exp(a))

# import numpy as np
# import matplotlib.pyplot as plt
# a = np.array([1,2,3])
# print(np.log(a))

import numpy as np
import matplotlib.pyplot as plt
a = np.array([1,2,3])
print(np.log10(a))