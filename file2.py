import numpy as np


a = np.array([1, 2, 3, 4, 5])
print(a)

# fanci indexing
b = [1,2,3]
print(a[b])


c  =np.argwhere(a%2==0).flatten() # indexing
print(c) # indexing

print(f'argwhere  {a[c]}')


print(f'other way { a[a%2==0] }')
