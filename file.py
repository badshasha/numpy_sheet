# import numpy library
import numpy as np

a = np.array([1,2,3,4])

print(a)
print(a.shape)  # shape of the array base on tuple   (4,)
print(a.dtype)  # contain variable type ( int64 , float)    (int64)
print(a.ndim)   # demention of                        (1)
print(a.size)   # size of the array base              (4)
print(a.itemsize) # size of the byte of one element   (8)
