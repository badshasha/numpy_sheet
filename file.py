# import numpy library
import numpy as np

a = np.array([1,2,3,4])

print(a)
print(a.shape)  # shape of the array base on tuple   (4,)
print(a.dtype)  # contain variable type ( int64 , float)    (int64)
print(a.ndim)   # demention of                        (1)
print(a.size)   # size of the array base              (4)
print(a.itemsize) # size of the byte of one element   (8)


# access numbers

print(a[0])   # access first element of the list
print(a[:5])  #  access firstelment to fouth element of the list

# assign vlaue to array element

a[0] = 10
a[1] = 20

b = a * np.array([1,2,3,4])  #  [ 1*1 , 2*2 , 3*3, 4*4 ]
print(b)
