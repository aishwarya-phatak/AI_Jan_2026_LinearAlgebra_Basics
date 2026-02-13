import numpy as np

#vector
v1 = np.array([11, 22, 33])
print(v1)
#matrix
m1 = np.array([[21,23],[24,19]])
print(m1)

m2 = np.array([[19,13],[18,25]])
print(m2)

print(m1 + m2)         #matrix addition

#creating identity matrix without eye function
m3 = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(m3)

#identity matrix
mat_i = np.eye(3, dtype=int)
print(mat_i)

#zeros matrix
mat_z = np.zeros((3,3))
print(mat_z)