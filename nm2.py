import numpy as np

a = np.ones(5)
b = np.zeros(3)
c = np.empty(2)
print(a)
print(b)
print(c)

t = np.arange(5)
print(t)

t = np.arange(2, 10, 2)
print(t)

# you say you want 5 number between 0 and 10
s = np.linspace(0, 10, num=5)
print(s)


# matrix 2 spaces 
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print("a -----------")
print(a.ndim)
print(a.size)
print(a.shape)

# tensor spaec more than 2 
b = np.array([
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ],
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]
])
print("b -----------")
print(b.ndim)
print(b.shape)
print(b.size)
