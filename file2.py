import numpy as np


a = np.array([[1,2],[3,4],[6,7]])
print( f'origianl np array \n {a}' )


# user booliean
bool_array = a >= 2  # RETURN THE BOOLEAN ARRAY
print( bool_array )

# another way ==> (1)
print( a[a>2] )

# another way2 ==> (2)
print( a[bool_array] )


# TAKE ARRAY WISAME SAME SIZE

b = np.where( a > 2 , a , -1 )  # meaning is the boolean true vlaue get from a
                                # if it's fales then value should be -1
print(b)
