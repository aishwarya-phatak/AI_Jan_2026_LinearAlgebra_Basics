import numpy as np

tensor_1 = np.array([[[1,1,1],[2,2,2]],[[1,1,1],[2,2,2]]])
tensor_2 = np.array([[[1,1,1],[2,2,2]],[[1,1,1],[2,2,2]]])
print(tensor_1 + tensor_2)
print(np.shape(tensor_1))   #shape of tensor

A = np.array([[1,2],[1,2]])
B = np.array([[1,2],[1,2]])

print(A + B)

print(np.dot(A, B))