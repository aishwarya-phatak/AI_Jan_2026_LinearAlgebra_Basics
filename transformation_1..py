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

#Rank of matrix
mat_1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(np.linalg.matrix_rank(mat_1))

#reflection on X-Axis
vect_1 = np.array([2,2])
refl_x = np.array([[1,0],[0,-1]])
res_ref_x = refl_x @ vect_1
print(res_ref_x)
print("------------------------")
#reflection on Y-Axis
refl_y = np.array([[-1,0],[0,1]])
res_ref_y = np.dot(refl_y, vect_1)
print(res_ref_y)