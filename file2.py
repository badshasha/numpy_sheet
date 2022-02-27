import numpy as np



a = np.arange(1,5)
b = np.arange(5,9)


#hstack   horizontal stack

c =np.hstack((a,b))
print(c)


#vstack  virttically stack
d   = np.vstack((a,b))
print(d)
