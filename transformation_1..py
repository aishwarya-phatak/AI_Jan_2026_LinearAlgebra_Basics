import numpy as np

#scaling of matrix
v_scale = np.array([2,2])
A = np.array([[1,1],[1,1]])
A_scaled = A @ v_scale
print(A_scaled)

#rotation of matrix
v_rot = np.array([1,1])
A_rot_1 = np.array([[0,-1],[1,0]]) #90 deg counterclockwise
print(A_rot_1 @ v_rot)

A_rot_2 = np.array([[-1,0],[0,-1]]) #180 deg counterclockwise
print(A_rot_2 @ v_rot)