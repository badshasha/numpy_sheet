# import numpy library
import numpy as np
from timeit import default_timer as  timer


l = [1,2,3]
a = np.array(l)

# same functionalities are same some are different
# [!] numpy havent got [append] functionalities


l = l + [4]
a = a + np.array([4])

print(l,a)

# [1, 2, 3, 4]  [5 6 7]



l = l * 2
a = a * 2

print(l,a)
# [1, 2, 3, 4, 1, 2, 3, 4]  python list
# [10 12 14]  np.array


# apply matematicall funcition element view not based on array or lis t
# eg
print(np.sqrt(a))
print(np.log(a))

# dot product different

start_time = timer()

l1 = [1,2,3]
l2 = [1,2,3]

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)



end_time = timer()
different = end_time - start_time
print(f'time {different}')


# with numpy
start_time = timer()

l1 = np.array(l1)
l2 = np.array(l2)

# one way
# print(np.sum(l1 * l2))  # why i need sum because index wise operation

# best way

print(np.dot(l1,l2))
end_time = timer()
different2 = end_time - start_time
print(f'time {different2}')

# suppoer best
print( l1 @ l2 ) # support for new version only please refere the documentation


print(f'ration  { different2 / different } ')
print(f'ration  { different / different2 } ')
