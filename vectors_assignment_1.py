import numpy as np

#vectors

v1 = np.array([1, 2])
v2 = np.array([3, 4])

#addition
#v1 + v2

print(v1 + v2)

#magnitude calculation
print(np.linalg.norm(v2))
print(np.linalg.norm(v1))


#dot product
y = np.dot(v1,v2)
print(y)