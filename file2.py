import numpy as np


a = np.array([1, 2, 3, 4, 5])


# createing and rearange

b = np.arange( 1,11 )
print(b)
print(b.shape)

# reshaping

c = b.reshape((2,5))
print(c)
print(c.shape)

# another shape
d = b.reshape((5,2))
print(d)
print(d.shape)

# list of list

e = b[np.newaxis , :]
print(e)
print(e.shape)