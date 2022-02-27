import numpy as np


a = np.array([1,2])
print(a.shape)

a = np.array( [[1,2,4,5], [3,4,1,2]] )
print(a.shape)  # (2,2)  row , column


# 1 row 1 column
print( a[0][0] )
print( a[0,0] )

print( a[:,0] )
print( a[0,:] )



# more slicing
print( a[0,1:3] )  # start inedx 1 and end 2



print(  a[-1,-1] )  # start last row and last coulumd 
