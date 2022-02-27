import numpy as np


a = np.array([1,2])
print(a.shape)

a = np.array( [[1,2], [3,4]] )
print(a.shape)  # (2,2)  row , column


# 1 row 1 column
print( a[0][0] )
print( a[0,0] )

print( a[:,0] )
print( a[0,:] )

print(a.T)
