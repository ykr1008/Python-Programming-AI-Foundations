a = [[1, 2], [3, 4]]
b = a
c = a[:]

import copy
d = copy.deepcopy(a)

a[0][0] = 99

print(b[0][0], c[0][0], d[0][0])

# prediction is 99 99 1

# c = a[:] creates a shallow copy, which creates a new outer list but keeps references 
# to the same inner lists. Therefore, changing a[0][0] also changes c[0][0] to 99, while 
# d, created using copy.deepcopy(a), keeps its independent value of 1.