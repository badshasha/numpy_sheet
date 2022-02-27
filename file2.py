import numpy as np

a  = np.array([1,2,3,4])

# append element
b  = np.array([5,6,7,8])

c = np.concatenate([a, b])
print(c)



# two dementional

array1 = np.array( [[1,2],[3,4]] )
array2 = np.array( [[5,6]] )

array3 = np.concatenate([array1, array2])
print(array3)   # [[1 2]
                 # [3 4]
                 # [5 6]]


array3 = np.concatenate([array1, array2] , axis=None)  # no dementional array shown
print(array3)  # [1 2 3 4 5 6]

# error
array3 = np.concatenate([array1, array2] , axis=1)  # because demention not matching


# transpose
array3 = np.concatenate([array1, array2.T] , axis=1)
print(array3)
