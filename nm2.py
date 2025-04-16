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