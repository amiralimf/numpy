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

# math things or brodcasting
x = ([10])
i = x * b2
print(i)

# slice
a2 = a[1:3]
print(a2)
a3 = a[0:3:2]
print(a3)

b3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b4 = b3[b3>3]
b5 = b3[b3<4]
print(b4)
print(b5)