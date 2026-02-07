import numpy as np

#vector
a = np.array([2,1])
b = np.array([5,6])

print(a + b)            # vector addition

#vector multiplication  -- dot product
resultant = np.dot(a,b)
print(resultant)
print(np.linalg.norm(a))            #calculates magnitude/length of a vector
print(np.linalg.norm(b))

#example in terms of ML
#linera regression model
#sushant - subject1
features1 = np.array([100,23,33])     # three features -attendance,assignments,assessments
weights1 = np.array( [0.2,0.4,0.4])   # weights - weightage for attendance, assignment, assessment
b = 0
y = np.dot(features1,weights1) + b
print("prediction score : {}".format(y))

#subject 2 - Pallavi
features2 = np.array([43,80,65])
y1 = np.dot(features2,weights1) + b
print("prediction score : {}".format(y1))