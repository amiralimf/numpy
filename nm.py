import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

b = np.array([[1,2], [3,4]])
print(b)

# shape
print(a.shape, b.shape)

# reshape
c = a.reshape((4,1))
print(c)

# concatenate (convert two list into one list)
b2 = np.array([5,6])
con = np.concatenate((a,b2))
print(con)