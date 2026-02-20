import numpy as np

#vector
v1 = np.array([11, 22, 33])
print(v1)
#matrix
m1 = np.array([[1,1],[1,1]])
print(m1)

m2 = np.array([[2,2],[2,2]])
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

print("-----------------")
#matrix multiplication - dot product
mat_mul_res = np.dot(m1,m2)
print(mat_mul_res)

#implementation of ML simple algorithm -- linear regression
X = np.array([[13,19],[16,15]])
print(X)
Y = np.array([2,0.05])
b = 0
prediction1 = np.dot(X,Y) + b
print("--------------")
print(prediction1)


A = np.array([[1,1],[1,1]])
result = 3 * A
print(result)
print("-------------------------")
print("-------------------------")

#matrix shape calculation and multiplication
matrix_1 = np.array([[12,13,14],[15,18,10]])
print(matrix_1)

vec_weights = np.array([60,20,20])
print(vec_weights)
print("-------------------------")
result_1 = np.dot(matrix_1, vec_weights)
print("-------------------------")
result_2 = matrix_1 @ vec_weights

print(np.shape(matrix_1))
print(np.shape(vec_weights))
print(np.shape(result_1))
print(np.shape(result_2))
